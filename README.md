# BALROG DEMO

## Installation

```bash
conda create -n demo python=3.10
conda activate demo

git submodule update --init --recursive
pip install https://github.com/BartekCupial/nle/releases/download/balrog/nle-0.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
pip install git+https://github.com/facebookresearch/minihack
pip install textworld
pip install crafter
pip install git+https://github.com/nacloos/baba-is-ai.git
pip install git+https://github.com/BartekCupial/Minigrid.git
pip install -e external/nle_utils
pip install -e .[dev]
pre-commit install

# to download minihack boxoban levels
python -c "import sys,os,subprocess,minihack; subprocess.run([sys.executable, os.path.join(os.path.dirname(minihack.__file__), 'scripts', 'download_boxoban_levels.py')])"
```

## Record

record nethack
```bash 
python -m balrog_demo.envs.nethack.record_nethack \
    --env=NetHackChallenge-v0 \
    --seed=0 \
    --demodir=demos/nethack_demo
```

record minihack
```bash 
python -m balrog_demo.envs.minihack.record_minihack \
    --env=MiniHack-Corridor-R3-v0 \
    --seed=0 \
    --demodir=demos/minihack_demo
```

## View

view nethack
```bash 
python -m balrog_demo.envs.nethack.view_nethack \
    --env=NetHackChallenge-v0 \
    --seed=0 \
    --demodir=demos/nethack_demo
```

view minihack
```bash 
python -m balrog_demo.envs.minihack.view_minihack \
    --env=MiniHack-Corridor-R3-v0 \
    --seed=0 \
    --demodir=demos/minihack_demo
```

## Troubleshooting pygame

    export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6

https://stackoverflow.com/questions/71010343/cannot-load-swrast-and-iris-drivers-in-fedora-35/72200748#72200748