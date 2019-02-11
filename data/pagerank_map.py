#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

def read_in(line):
	info = line.split()
	node_id = info[0].split(':')[1]
	node_info = info[1].split(',')
	curr_pr = float(node_info[0])
	prev_pr = float(node_info[1])
	node_out_links = [int(node) for node in node_info[2:]]
	return node_id, [curr_pr, prev_pr, node_out_links]

def pr_mapper(node_id, list_of_values):
	alpha = 0.85
	curr_pr = list_of_values[0]
	prev_pr = list_of_values[1]
	node_out_links = list_of_values[2]
	out_deg = len(node_out_links)
	
	line = node_id + "," + str(curr_pr) + ","
	
	if out_deg == 0: # no out links
		curr_contri = curr_pr * (alpha * 1 + (1 - alpha)) 
		sys.stdout.write("%s-%s\t%f\n" % (node_id, node_id, curr_contri))

	for out_node in node_out_links: # contribution to each out link
		p_ij = 1 / out_deg
		curr_contri = curr_pr * (alpha * p_ij + (1 - alpha))
		sys.stdout.write("%s-%s\t%f\n" % (node_id, out_node, curr_contri))
		line = line + str(out_node)
	#sys.stdout.write("%s\t%f", (node_id, line))


for line in sys.stdin:
	node_id, list_of_values = read_in(line)
	pr_mapper(node_id, list_of_values)
    #sys.stdout.write(line)

