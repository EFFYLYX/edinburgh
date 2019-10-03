#!/usr/bin/env python2
# Mapper in: title.basics.tsv out: [genre:str]
import sys


def reduce_function(word, values):
    return word, sum(values)

prev_key = None
values = []

for line in sys.stdin:
    key, value = line.strip().split('|')
 # If key has changed then one can finish processing the previous key
    if key != prev_key and prev_key is not None:
        result_key, result_value= reduce_function(prev_key, values)
        print(result_key + '|' + str(result_value))
        values = []

    prev_key = key
    values.append(int(value))
# last value
if prev_key is not None:
    result_key, result_value = reduce_function(prev_key, values)
    print(result_key + '|' + str(result_value))
