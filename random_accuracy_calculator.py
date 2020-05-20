import re

import nltk

import data_ptb

from parse_comparison import corpus_stats_labeled

def MRG_labeled(tr):
    if isinstance(tr, nltk.Tree):
        if tr.label() in word_tags:
            return tr.leaves()[0] + ' '
        else:
            s = '(%s ' % (re.split(r'[-=]', tr.label())[0])
            for subtr in tr:
                s += MRG_labeled(subtr)
            s += ') '
            return s
    else:
        return ''

def getGold(filePath):
    gold_trees = []
    corpus = data_ptb.Corpus(filePath)
    print(len(corpus.test_nltktrees))
    for sen_nltktree in corpus.test_nltktrees:
            gold_trees.append(MRG_labeled(sen_nltktree))
    return gold_trees

def getPred(filePath):
    return [sent.rstrip('\n') for sent in open(filePath,'r').readlines()]

getAll = True

def accuracy(correct,total):
    acc = {cons:0 for cons in total}
    if getAll:
        consList = total.keys()
        getAll=False
    for cons in correct:
        acc[cons] = correct[cons]/total[cons]
    return acc

def mean(l):
    return sum(l)/len(l)

def meanStd(accs):
    import statistics
    result = {}
    for cons in consList:
        acc5 = [acc[cons] for acc in accs]
        result[cons] = (mean(acc5),statistics.pstdev(acc5))

if __name__=='__main__':
    accs = []
    gold = getGold('treebank_3/parsed/mrg/WSJ')
    corpus_ref = {i: gold[i] for i in range(len(gold))}
    for i in range(5):
        pred = getPred('random_MRG/random{}.txt'.format(i))
        corpus_sys = {i: pred[i] for i in range(len(pred))}
        #print(len(corpus_sys),len(corpus_ref))
        #print(corpus_sys[5])
        correct, total = corpus_stats_labeled(corpus_sys, corpus_ref)
        accs.append(accuracy(correct,total))
    
    print(meanStd(accs))
    #output_trees = [tree.replace('\n','') for tree in sen_nltktrees]
    


