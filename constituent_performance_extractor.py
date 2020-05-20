import re
from statistics import pstdev
seeds = ['pilot_reproduction','random1WSJ','random2WSJ','random3WSJ','random4WSJ']

reports = []
for seed in seeds:
	counters = []
	text = open('parse_'+seed+'.out','r').read()
	for line in text.splitlines():
		if re.search('Counter\({',line):
			counters.append(eval(line.lstrip('Counter(').rstrip(')\n')))
	reports.append((counters[2],counters[3]))

print(len(reports))
print('constituent counts:',reports[0][1])
'''
for report in reports:
	print(report)
'''
result = {}

for constituent in reports[0][1]:
	for i in range(len(seeds)):
		if constituent not in reports[i][0]:
			reports[i][0][constituent]=0
	accuracies = [reports[i][0][constituent]/reports[i][1][constituent] for i in range(len(seeds))]
	mean = sum(accuracies)/len(accuracies)
	pstd = pstdev(accuracies)
	result[constituent] = (mean,pstd)

print('accuracies and std:',result)
	
			

	
