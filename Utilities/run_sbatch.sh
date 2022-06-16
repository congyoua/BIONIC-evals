#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=40
#SBATCH --time=20:00:00
#SBATCH --mail-type=FAIL
#SBATCH --mem=24G

TRIAL=$1
cd $HOME/projects/def-gbader/congyoua/
source BIONIC/bin/activate

module load scipy-stack

echo $TRIAL

cd ./BIONIC-evals/

python Run_BIONIC_evals.py -t $TRIAL