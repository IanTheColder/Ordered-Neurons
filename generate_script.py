import argparse
import random

parser = argparse.ArgumentParser()

parser.add_argument('--id', type=str)

parser.add_argument('--finetuning', type=int)

args = parser.parse_args()

template = '''#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
#SBATCH --mem=10GB
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=yz4135@nyu.edu
#SBATCH --output={}.out
#SBATCH --gres=gpu:v100:1

module purge
module load anaconda3/5.3.1
source activate nlu_env

python ./main.py \
    --batch_size 20 \
    --dropout 0.45 \
    --dropouth 0.3 \
    --dropouti 0.5 \
    --wdrop 0.45 \
    --chunk_size 10 \
    --seed 141 \
    --epochs 1000 \
    --save {} \
    --finetuning {}'''

with open(args.id+'.sbatch','w') as script:
    script.write(template.format(args.id, args.id+'.pt', args.finetuning))

