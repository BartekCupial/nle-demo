# NLE DEMO

## Installation

```bash
# nle dependencies
apt-get install -yq autoconf libtool pkg-config libbz2-dev

conda create -n nle_demo python=3.10
conda activate nle_demo
conda update -n base -c defaults conda
conda install -yq cmake flex bison lit
conda install -yq pybind11 -c conda-forge

git submodule update --init --recursive
python minihack/scripts/download_boxoban_levels.py
pip install -e external/Grounding_LLMs_with_online_RL/babyai-text
pip install -e external/Grounding_LLMs_with_online_RL/babyai-text/babyai
pip install -e external/Grounding_LLMs_with_online_RL/babyai-text/gym-minigrid
pip install -e external/minihack
pip install -e external/nle
pip install -e external/nle_utils
pip install textworld
pip install crafter
pip install git+https://github.com/nacloos/baba-is-ai.git
pip install -e .[dev]
pre-commit install
```

## Record

record nethack
```bash 
python -m nle_demo.envs.nethack.record_nethack \
    --env=nethack_challenge \
    --seed=0 \
    --demodir=nethack_demo
```

record minihack
```bash 
python -m nle_demo.envs.minihack.record_minihack \
    --env=corridor3 \
    --seed=0 \
    --demodir=minihack_demo
```

## View

view nethack
```bash 
python -m nle_demo.envs.nethack.view_nethack \
    --env=nethack_challenge \
    --seed=0 \
    --demodir=nethack_demo
```

view minihack
```bash 
python -m nle_demo.envs.minihack.view_minihack \
    --env=corridor3 \
    --seed=0 \
    --demodir=minihack_demo
```