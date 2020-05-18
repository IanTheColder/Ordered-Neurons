import data_ptb

corpus = data_ptb.Corpus('treebank_3/parsed/mrg/WSJ')

f_out = open('wsj10.txt','w')
for i in range(len(corpus.train_sens)):
	sent = corpus.train_sens[i]
	if len(sent)<=12:
		f_out.write(' '.join(sent[1:-1])+'\n')
f_out.close()	
