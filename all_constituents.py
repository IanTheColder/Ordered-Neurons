import data_ptb
import re

corpus = data_ptb.Corpus('treebank_3/parsed/mrg/WSJ')

constituents = set()

for i in range(len(corpus.test_nltktrees)):
	sent = corpus.test_nltktrees[i]
	constituents.update([result[1:-1] for result in re.findall('\([A-Z]+[\s-]',str(sent))])
	if 'LS' in str(sent):
		print(sent)
print(constituents)

