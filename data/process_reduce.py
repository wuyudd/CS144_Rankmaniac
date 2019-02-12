#!/usr/bin/env python

import sys
import heapq
#
# This program simply represents the identity function.
#
def readline(line):
	s = line.split('\t')
	fir = s[0].split('@')
	sec = s[1].split(',')
	itr = fir[0]
	node = fir[1].split(':')[-1]
	curr_pr,prev_pr = sec[0],sec[1]

	return int(node), float(curr_pr), float(prev_pr),int(itr)

all_curr_pr = []
all_prev_pr = []
itr = 0
out = []
for line in sys.stdin:
	node, curr_pr, prev_pr,itr = readline(line)
	all_curr_pr.append((curr_pr,node))
	all_prev_pr.append((prev_pr,node))
	out.append(line)

klargest_cur = heapq.nlargest(20,all_curr_pr)
klargest_prev = heapq.nlargest(20,all_prev_pr)
if  itr == 50 or klargest_cur == klargest_prev:
	for rank,node in klargest_cur:
		#sys.stdout.write('FinalRank:'+str(rank)+'\t'+str(node)+'\n')
		sys.stdout.write('FinalRank:'+str(rank)+'\t'+str(node)+", iter=" + str(itr) + '\n')
else:
	for line in out:
		sys.stdout.write(line)








