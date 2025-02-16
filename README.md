# coPylot
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

_coPylot_ is a python app to control the lightsheet microscopes
we build here at @czbiohub
.
Support for controling other microscopes planned to be added.

It can be started up by running `copylot/gui/gui.py`.


## Installation

Using an environment manager is highly recommended. 
Instructions below using [Anaconda](https://www.anaconda.com/distribution/)
but you can pick your favorite environment manager and do not forget to
have `pip`.


#### Clone coPylot Repository

```
git clone https://github.com/royerlab/coPylot.git
```

#### Create Conda Environment and Install coPylot 

We currently have no release on pypi, so you can follow the steps below to 
install editable version of coPylot with help of `pip`:

```
conda create -n coPylot python=3.9
conda activate coPylot
pip install -e .
```

## Documentation

coPylot documentation can be found [here](https://royerlab.github.io/coPylot/).


## Contributing

All contributions are welcome here! Please take a look at our 
[contributing guideline](CONTRIBUTING.md) first.
