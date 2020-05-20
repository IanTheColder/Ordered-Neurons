import data_ptb
import re

corpus = data_ptb.Corpus('treebank_3/parsed/mrg/WSJ')

#constituents = ['NP', 'VP', 'S', 'PP', 'QP', 'SBAR', 'ADJP', 'ADVP', 'FRAG', 'SQ', 'SINV', 'SBARQ', 'PRN', 'X', 'WHNP', 'UCP', 'INTJ', 'NAC', 'WHADVP', 'NX', 'WHADJP', 'WHPP', 'RRC', 'CONJP']

constituents = ['LS',
 'DT',
 'INTJ',
 'WP',
 'CC',
 'VBP',
 'ADVP',
 'VBD',
 'WRB',
 'VBG',
 'CONJP',
 'LST',
 'NX',
 'NN',
 'SBAR',
 'ADJP',
 'SINV',
 'WHPP',
 'SQ',
 'CD',
 'PRN',
 'NAC',
 'FRAG',
 'NNPS',
 'UCP',
 'RBR',
 'JJR',
 'JJS',
 'WHNP',
 'QP',
 'S',
 'UH',
 'IN',
 'WHADJP',
 'NP',
 'VBN',
 'POS',
 'RB',
 'SBARQ',
 'VB',
 'PRP',
 'VP',
 'RP',
 'RBS',
 'SYM',
 'JJ',
 'X',
 'NNP',
 'WHADVP',
 'WDT',
 'EX',
 'PDT',
 'VBZ',
 'FW',
 'NNS',
 'PP',
 'TO',
 'PRT',
 'MD']
regex = {constituent:'\('+constituent+'[\s-]' for constituent in constituents}

counter = {constituent:[] for constituent in constituents}

f_out = open('cons_sent_len.txt','w')
for i in range(len(corpus.test_nltktrees)):
	sent = corpus.test_nltktrees[i]
	for constituent in constituents:
		if re.search(regex[constituent],str(sent))!=None:
			counter[constituent].append(len(corpus.test_sens[i])-2)
f_out.write(str({cons:sum(counter[cons])/len(counter[cons]) for cons in counter}))	
f_out.close()	
