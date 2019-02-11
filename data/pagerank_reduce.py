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
	sec = ''
	for v in vals:
		if v[0] == '+':
			sum += flaot(v[1:])
		else:
			sec = v
	sec = sec.split(',')
	sec[1] = sec[0]
	sec[0] = str(sum)
	s = fir+'\t'+sec.join(',')
	sys.stdout.write(s)

data = collections.defaultdict(list)
for line in sys.stdin:
    data = line.split('\t')
    key,val = data[0],data[1]
    data[key].append(val)

for key,val in data.items():
	reducer(key,val)


