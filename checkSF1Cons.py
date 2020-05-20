import data_ptb
import re

corpus = data_ptb.Corpus('treebank_3/parsed/mrg/WSJ')

print(len(corpus.test_nltktrees))

for i in range(len(corpus.test_nltktrees)):
	sent = corpus.test_nltktrees[i]
	#if i in [87,1749,1765,1775,1783,2103]:
	if i in [68, 74, 136, 157, 210, 251, 270]:
		print(sent,end='\n\n')

