#!/bin/bash

python scripts/analyzer.py -m 100 -s 1 -re True

python scripts/analyzer.py -m 100 -s 2 -o slimmed_ntuple_test

python scripts/analyzer.py -m 100 -s 123 -o slimmed_ntuple_test
