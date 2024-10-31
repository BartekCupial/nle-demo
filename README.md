# NLE DEMO

## Installation

```bash
# nle dependencies
apt-get install -yq autoconf libtool pkg-config libbz2-dev

conda create -n nle_demo python=3.10
conda activate nle_demo

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
python -c "import sys,os,subprocess,minihack; subprocess.run([sys.executable, os.path.join(os.path.dirname(minihack.__file__), 'scripts', 'download_boxob
an_levels.py')])"
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