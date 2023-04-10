#!/bin/bash

# create a temporary directory for the conda environment
temp_dir=$(mktemp -d)
cd $temp_dir

# download and install miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p ./miniconda

# activate the conda environment
source ./miniconda/etc/profile.d/conda.sh
conda activate base

# create a new conda environment with the required packages
conda create -y -n mytempenv uproot numpy ROOT matplotlib mplhep tqdm json

# activate the new environment
conda activate mytempenv

# run your code here

# deactivate the environment
conda deactivate

# remove the temporary directory and all its contents
# cd ..
# rm -rf $temp_dir
