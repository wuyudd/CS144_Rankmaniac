#!/usr/bin/env python

import sys
import collections

#
# This program simply represents the identity function.
#

def reducer(key,vals):
	alpha = 0.85
	sum = 1-alpha
	fir = key
	sec = ""
	for v in vals:
		if v[0] == '+':
			sum += float(v[1:])
		else:
			sec = v
	sec = sec.split(',')
	sec[1] = sec[0]
	sec[0] = str(sum)

	if len(sec) == 2:
		s = fir+'\t'+','.join(sec) + '\n'
	else:
		s = fir+'\t'+','.join(sec)
	sys.stdout.write(s)

data = collections.defaultdict(list)
for line in sys.stdin:
    info = line.split('\t')
    key,val = info[0],info[1]
    data[key].append(val)

for key,val in data.items():
	reducer(key,val)


