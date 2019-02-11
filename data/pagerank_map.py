#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#


def read_in(line):
    '''
    line format: iter@NodeId:i	curr_pr, prev_pr, out_node_1, out_node_2, ...
    '''
    raw_info = line.split('@')

    iter = raw_info[0] # iteration time
    if len(iter) == 1:
        iteration = int(iter) + 1
    else:
        iteration = 1

    ori_info = raw_info[-1] # NodeId:i	curr_pr, prev_pr, out_node_1, out_node_2, ...
    info = ori_info.split()
    node_id = info[0].split(':')[-1]
    node_info = info[-1].split(',')
    curr_pr = float(node_info[0])
    prev_pr = float(node_info[1])
    node_out_links = [int(node) for node in node_info[2:]]

    return node_id, [iteration, curr_pr, prev_pr, node_out_links]


def mapper(node_id, list_of_values):
    alpha = 0.85
    iteration = list_of_values[0]
    curr_pr = list_of_values[1]
    prev_pr = list_of_values[2]
    node_out_links = list_of_values[3]

    out_deg = len(node_out_links)
    #sys.stdout.write(str(out_deg) + "\n")

    graph_info = str(curr_pr) + "," + str(prev_pr) + ","

    if out_deg == 0: # no out links
        curr_contri = curr_pr * (alpha * 1)
        sys.stdout.write("%d@NodeId:%s\t+%f\n" % (iteration, node_id, curr_contri))

    for out_node in node_out_links: # contribution to each out link
        p_ij = 1.0 / out_deg
        #sys.stdout.write(str(p_ij) + "\n")
        curr_contri = curr_pr * (alpha * p_ij)
        sys.stdout.write("%d@NodeId:%s\t+%f\n" % (iteration, out_node, curr_contri))
        graph_info = graph_info + str(out_node) + ","

    graph_info = graph_info[:-1]
    sys.stdout.write("%d@NodeId:%s\t%s\n" % (iteration, node_id, graph_info))


for line in sys.stdin:
    node_id, list_of_values = read_in(line)
    mapper(node_id, list_of_values)
    #sys.stdout.write(line)

