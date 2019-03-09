#!/bin/bash
for iter in {1..50}
do
	python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt

rm input.txt
cp output.txt input.txt
rm output.txt

if grep FinalRank input.txt
then 
	echo 'DADA!'
	break
fi

done

