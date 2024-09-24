#!/bin/bash


for env in BabyAI-MixedTrainLocal-v0/goto BabyAI-MixedTrainLocal-v0/pickup BabyAI-MixedTrainLocal-v0/open BabyAI-MixedTrainLocal-v0/putnext BabyAI-MixedTrainLocal-v0/pick_up_seq_go_to 
do
    for seed in 0 1 2 3 4
    do
    python -m nle_demo.envs.babyai.record_babyai --env=$env --seed=$seed --demodir=demos/babyai_demo
    done
done