#!/bin/bash

# 1. mamba env create and activate
mamba create -n stereohub python=3.8
mamba activate stereohub

# 1.1 shiny
mamba install -c conda-forge shiny=1.0.0 shinywidgets=0.3.2 IPython=8.12.2 ipywidgets=8.1.3

# 1.2 utils
mamba install -c conda-forge numpy=1.23.5 pandas=1.5.3 matplotlib=3.7.1 faicons=0.2.2

# 1.3 stereopy
mamba install stereopy=1.3.1 -c stereopy -c grst -c numba -c conda-forge -c bioconda -c fastai -c defaults