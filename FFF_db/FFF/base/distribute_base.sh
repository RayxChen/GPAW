#!/bin/bash


for species in `ls -d */ | grep -v -E 'all_OH|all_OOH'`; do
    cd ${species}
    for m in `ls -d */`; do
        cd ${m}
        cp ../../last.py .
        mv *.traj a1.traj
        echo ${species}${m}
        python last.py
        rm last.py
        cd ../
        echo "${species} save last frame"
    done
    cd ../
done

