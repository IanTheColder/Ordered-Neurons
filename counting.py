import data_ptb
import re

corpus = data_ptb.Corpus('treebank_3/parsed/mrg/WSJ')

#constituents = ['NP', 'VP', 'S', 'PP', 'QP', 'SBAR', 'ADJP', 'ADVP', 'FRAG', 'SQ', 'SINV', 'SBARQ', 'PRN', 'X', 'WHNP', 'UCP', 'INTJ', 'NAC', 'WHADVP', 'NX', 'WHADJP', 'WHPP', 'RRC', 'CONJP']

constituents = ['NP', 'VP', 'S', 'PP', 'SBAR', 'ADJP', 'QP', 'ADVP', 'SINV', 'PRN', 'NX', 'FRAG', 'WHNP', 'UCP', 'NAC', 'WHPP', 'CONJP', 'SQ', 'SBARQ', 'WHADVP', 'X', 'WHADJP', 'INTJ']
regex = {constituent:'\('+constituent+'[\s-]' for constituent in constituents}

counter = {constituent:0 for constituent in constituents}

f_out = open('Constituents_occurances.txt','w')
for i in range(len(corpus.test_nltktrees)):
        sent = corpus.test_nltktrees[i]
        for constituent in constituents:
                counter[constituent]+=len(re.findall(regex[constituent],str(sent)))
        if 'INTJ' in str(sent):
                print(sent)
                print(counter)
f_out.write(str(counter))
f_out.close()
~