#pragma once

#include "gs_def.h"
#include "cusha256.h"
#include "cudagol.h"

#define minibatch 20000

namespace apg {

    std::vector<uint64_t> GpuSearcher::pump(std::string seed, uint64_t epoch) {

        int maxgen = 18000;

        hash_container *hc = (hash_container*) this->xhc;
        uint4 *multiverse = (uint4*) this->xmc;

        cudaSetDevice(this->device);

        hc->create_hashes(seed, epoch);

        for (int sb = 0; sb < 1000000; sb += minibatch) {

            uint32_t* hi = hc->interesting + sb;
            uint32_t* hh = hc->d_B + sb * 8;

            exhaustFirstTile<<<(minibatch >> 2),  128>>>(hh, hi, multiverse);

            exhaustMultipleTiles< 8><<<minibatch, 128>>>(2,  hi, hc->topology, multiverse, maxgen);
            exhaustMultipleTiles<20><<<minibatch, 128>>>(8,  hi, hc->topology, multiverse, maxgen);
            exhaustMultipleTiles<38><<<minibatch, 256>>>(20, hi, hc->topology, multiverse, maxgen);
            exhaustMultipleTiles<62><<<minibatch, 384>>>(38, hi, hc->topology, multiverse, maxgen);
            exhaustMultipleTiles<92><<<minibatch, 384>>>(62, hi, hc->topology, multiverse, maxgen);

            exhaustMultipleTilesUltimate<92, 128><<<minibatch, 384>>>(92, hi, hc->topology, multiverse, maxgen);
        }

        auto vec = hc->extract_gems(epoch, 1000000);
        std::cout << "Interesting universes: " << vec.size() << " out of 1000000" << std::endl;

        cudaError_t err = cudaGetLastError();
        if (err != cudaSuccess) { std::cerr << "Error: " << cudaGetErrorString(err) << std::endl; }

        return vec;
    }

    GpuSearcher::GpuSearcher(int dev, int num_universes, std::string symmetry) {
        this->num_universes = num_universes;
        this->symstring = symmetry;
        this->device = dev;
        auto hc = new hash_container();

        cudaMalloc((void**) &(this->xmc), minibatch * 65536);

        this->xhc = (void*) hc;

        cudaSetDevice(dev);

        hc->spin_up(true, num_universes);
    }

    GpuSearcher::~GpuSearcher() {
        hash_container *hc = (hash_container*) this->xhc;

        cudaSetDevice(this->device);

        hc->tear_down();
        cudaFree(this->xmc);

        delete hc;
    }

}
