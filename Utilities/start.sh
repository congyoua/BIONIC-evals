#!/bin/bash
NUM=`ls /scratch/congyoua/BIONIC/Configs|wc -l`
NUM=$((NUM-1))
echo $NUM
for TRIAL in $( seq 0 $NUM )
do
    echo $TRIAL
    sbatch run_sbatch.sh $TRIAL
done
