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

k = 40
all_curr_pr = []
all_prev_pr = []
itr = 0
out = []
for line in sys.stdin:
	node, curr_pr, prev_pr,itr = readline(line)
	all_curr_pr.append((curr_pr,node))
	all_prev_pr.append((prev_pr,node))
	out.append(line)


klargest_cur = heapq.nlargest(k,all_curr_pr)
klargest_prev = heapq.nlargest(k,all_prev_pr)

prev_top_node = [node for rank,node in klargest_prev]
cur_top_node = [node for rank,node in klargest_cur]

prev_top_node_set = set(prev_top_node)
cur_top_node_set = set(cur_top_node)

if  itr == 50 or prev_top_node_set == cur_top_node_set:
	for rank,node in klargest_cur:
		#sys.stdout.write('FinalRank:'+str(rank)+'\t'+str(node)+'\n')
		sys.stdout.write('FinalRank:'+str(rank)+'\t'+str(node)+", iter=" + str(itr) +'\n')
else:
	for line in out:
		sys.stdout.write(line)









