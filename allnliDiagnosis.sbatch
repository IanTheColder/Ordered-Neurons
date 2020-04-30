#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=168:00:00
#SBATCH --mem=10GB
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=yz4135@nyu.edu
#SBATCH --output=allnliDiagnosis.out
#SBATCH --gres=gpu:1

module purge
module load anaconda3/5.3.1
source activate nlu_env

CUDA_LAUNCH_BLOCKING=1 python mainS.py     --batch_size 20     --dropout 0.45     --dropouth 0.3     --dropouti 0.5     --wdrop 0.45     --chunk_size 10     --seed 141     --epochs 1000     --save allnliDiagnosis.pt     --data data/allnli
