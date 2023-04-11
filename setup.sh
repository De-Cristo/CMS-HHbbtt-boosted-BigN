#!/bin/bash
source /gwdata/users/lzhang/public/miniconda3/bin/activate
conda activate my_root_env

# conda create --prefix ./my_root_env --file environment.yml
# source activate ./my_root_env

export PYTHONPATH=$PYTHONPATH:$PWD
