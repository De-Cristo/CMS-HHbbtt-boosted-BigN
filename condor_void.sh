#!/bin/bash

hours=$1
interval=3600

for ((i=1; i<=$hours; i++))
do
    echo "Current time: $(date)"
    sleep $interval
done
