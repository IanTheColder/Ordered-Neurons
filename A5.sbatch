#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=168:00:00
#SBATCH --mem=10GB
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=yz4135@nyu.edu
#SBATCH --output=A5.out
#SBATCH --gres=gpu:v100:1

module purge
module load anaconda3/5.3.1
source activate nlu_env

python ./mainS.py     --batch_size 20     --dropout 0.45     --dropouth 0.3     --dropouti 0.5     --wdrop 0.45     --chunk_size 10     --seed 192     --epochs 40     --save A5.pt     --data data/allnli
    