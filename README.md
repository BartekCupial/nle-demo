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
pip install -e external/nle
pip install -e external/nle_utils
pip install -e .[dev]
pre-commit install
```