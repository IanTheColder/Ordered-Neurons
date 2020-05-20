import re

import nltk

import data_ptb

from parse_comparison import corpus_stats_labeled

def getSent(filePath):
    gold_trees = []
    corpus = data_ptb.Corpus(filePath)
    print(len(corpus.test_nltktrees))
    for sen_nltktree in corpus.test_nltktrees:
            gold_trees.append(str(sen_nltktree))
    return gold_trees

def process(sent):
    puncts=".?,:;><>"
    extra = [" ('' '')", " (`` `)", " (: --)", " (`` ``)"," (-LRB- -LCB-)"," (-RRB- -RCB-)"," (-LRB- -LRB-)"," (-RRB- -RRB-)"]
    #" (JJ >)", " (JJ <)", " (-LRB- -LCB-)", " (-RRB- -RCB-)"," (VBP <)"," (VBP >)"," (VBD >)"," (VBD <)"," (VBZ <)"]
    sent = re.sub(' \([\.\?,:;><"A-Z]+ [\.\?,:;><"]\)','',sent)
    if sent.startswith('(TOP'):
        sent = sent.rstrip('\n')[5:-1]
    for to_replace in extra:
        sent = sent.replace(to_replace,'')
    return sent

if __name__=='__main__':
    nsens = 0
    corpus_sys = {}
    for filename in ['output_synconst_0.txt','output_synconst_1.txt','output_synconst_2.txt']:
        with open(filename,'r') as f_in:
            for line in f_in:
                corpus_sys[nsens] = process(line)
                nsens+=1
    #gold = getSent('treebank_3/parsed/mrg/WSJ')
    gold = [ process(line) for line in open('/Users/ianzhang/Desktop/Courses/mllu/neural-parser/LAL-Parser/data/23.auto.clean','r').readlines()]
    corpus_ref = {i: gold[i] for i in range(len(gold))}

    print(len(corpus_sys),len(corpus_ref))
    print(corpus_sys[5])
    correct, total = corpus_stats_labeled(corpus_sys, corpus_ref)
    print(correct)
    print(total)
    
    #output_trees = [tree.replace('\n','') for tree in sen_nltktrees]
    


