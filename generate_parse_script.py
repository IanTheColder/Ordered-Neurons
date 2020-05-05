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

python test_phrase_grammar.py --cuda --checkpoint {}.pt --data treebank_3/parsed/mrg/WSJ

python test_phrase_grammar.py --cuda --checkpoint {}.pt --data treebank_3/parsed/mrg/WSJ --wsj10'''

for job in ['random2WSJ','random3WSJ','random4WSJ','pilot_reproduction']:
	with open('parse_'+job+'.sbatch','w') as f:
		f.write(template.format(job,job,job))

