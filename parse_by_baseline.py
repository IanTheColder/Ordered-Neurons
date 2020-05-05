from baselines import randomize, balance
MODELS = {'random':randomize,'balance':balance}
DATA = 'data/penn/test.txt'

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('model',type=str)
args = parser.parse_args()

model = MODELS[args.model]

for i in range(5):
    with open('baseline_'+args.model+'_'+str(i),'w') as f_out:
        with open(DATA,'r') as f_in:
            for line in f_in:
                f_out.write(model(line.rstrip())+'\n')

