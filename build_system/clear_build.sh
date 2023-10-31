#!/bin/bash

cd ../

## Clear the python package built files

# First check if the package folders [dist build txm.egg-info] exists

if [ -d dist ] && [ -d build ] && [ -d txm.egg-info ]; then
    rm -rf dist build txm.egg-info
else
    echo "No package files to clear"
fi

## Clear logs
# First check if the log files exists

if [ -f *.log ]; then
    rm *.log
else
    echo "No log files to clear"
fi
