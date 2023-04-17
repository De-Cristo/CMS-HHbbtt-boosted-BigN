#!/bin/bash

Location = '/gwpool/users/lzhang/private/bbtt/CMS-HHbbtt-boosted-BigN/'

source ${Location}/setup.sh

python ${Location}/scripts/analyzer.py -m $1 -s $2 -o $3
