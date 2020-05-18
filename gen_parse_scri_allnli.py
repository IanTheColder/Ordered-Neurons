template = '''#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00
#SBATCH --mem=10GB
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=yz4135@nyu.edu
#SBATCH --output=parse_{}.out
#SBATCH --gres=gpu:1

module purge
module load anaconda3/5.3.1
source activate nlu_env

python test_phrase_grammar_random_input.py --cuda --checkpoint {}.pt --data data/allnli/test.txt
'''

for job in ['A1','A2','A3','A4','A5']:
	with open('parse_'+job+'.sbatch','w') as f:
		f.write(template.format(job,job))

