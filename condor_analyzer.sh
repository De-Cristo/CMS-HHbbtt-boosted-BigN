#!/bin/bash

Location='/gwpool/users/lzhang/private/bbtt/CMS-HHbbtt-boosted-BigN/'

source ${Location}/setup.sh
echo $PYTHONPATH
ls | xargs -n 1 echo $1 

python ${Location}/scripts/analyzer_condor.py -m $1 -s $2 -o $3
