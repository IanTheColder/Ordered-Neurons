#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
#SBATCH --mem=10GB
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=yz4135@nyu.edu
#SBATCH --output=GPUTest.out
#SBATCH --gres=gpu:1
#SBATCH --partition=k80_8

module purge
module load anaconda3/5.3.1
source activate nlu_env

python ./main.py     --batch_size 20     --dropout 0.45     --dropouth 0.3     --dropouti 0.5     --wdrop 0.45     --chunk_size 10     --seed 141     --epochs 1000     --save GPUTest.pt     --finetuning 500
