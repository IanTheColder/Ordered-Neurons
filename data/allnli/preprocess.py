#author: Yian Zhang; data: 04/25/2020

import json

#train
with open('snli_1.0_train.jsonl','r') as fin:
    sentences = set()
    line = fin.readline()
    while line!= '':
        sentences.add(' ' + json.loads(line)['sentence1']+'\n')
        sentences.add(' ' + json.loads(line)['sentence2']+'\n')
        line = fin.readline()

with open('multinli_1.0_train.jsonl','r') as fin:
    line = fin.readline()
    while line!= '':
        sentences.add(' ' + json.loads(line)['sentence1']+'\n')
        sentences.add(' ' + json.loads(line)['sentence2']+'\n')
        line = fin.readline()

open('allnli_train.txt','w').close()
with open('allnli_train.txt','a') as fout:
    for sent in sentences:
        fout.write(sent)


#dev

with open('snli_1.0_dev.jsonl','r') as fin:
    sentences = set()
    line = fin.readline()
    while line!= '':
        sentences.add(' ' + json.loads(line)['sentence1']+'\n')
        sentences.add(' ' + json.loads(line)['sentence2']+'\n')
        line = fin.readline()

with open('multinli_1.0_dev_matched.jsonl','r') as fin:
    line = fin.readline()
    while line!= '':
        sentences.add(' ' + json.loads(line)['sentence1']+'\n')
        sentences.add(' ' + json.loads(line)['sentence2']+'\n')
        line = fin.readline()

open('allnli_dev.txt','w').close()
with open('allnli_dev.txt','a') as fout:
    for sent in sentences:
        fout.write(sent)
    

