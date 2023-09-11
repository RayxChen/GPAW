#!/bin/bash


for species in `ls -d */ | grep -v -E 'all_base'`; do
    cd ${species}
    cp ../last.py .
    echo ${species}
#    mv *.traj a1.traj
    python last.py
    rm last.py
    cd ../
    echo "${species} copied"
done

