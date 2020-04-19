#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00
#SBATCH --mem=32GB
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=yz4135@nyu.edu
#SBATCH --output=parse.out
#SBATCH --gres=gpu:1

module purge
module load anaconda3/5.3.1
source activate nlu_env

python test_phrase_grammar.py --cuda --checkpoint 15871632805262651.pt --data treebank_3/
