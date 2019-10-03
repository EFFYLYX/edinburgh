#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Here are some libraries you're likely to use. You might want/need others as well.
import re
import sys
from random import random
from math import log
from collections import defaultdict
import numpy as np
from numpy.random import random_sample
tri_counts=defaultdict(int) #counts of all trigrams in input


#this function currently does nothing.
def preprocess_line(line):
    #() capture or group
    #[] a set of characters; ^arn  any character EXCEPT a r n; \s space;
    # \w contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
    # | either or; + one or more occurences; + any + character in the string
    # line = re.sub(r'([^\sA-Za-z0-9.]|_)+', '', line)
    line = re.sub(r'([^\sA-Za-z0-9.])', '', line)
    # print(line)
    return line
def generate_from_LM(distribution, N):
    outcomes = np.array(list(distribution.keys()))
    probs = np.array(list(distribution.values()))
    #make an array with the cumulative sum of probabilities at each
    #index (ie prob. mass func)
    bins = np.cumsum(probs)
    #create N random #s from 0-1
    #digitize tells us which bin they fall into.
    #return the sequence of outcomes associated with that sequence of bins
    #(we convert it from array back to list first)
    return list(outcomes[np.digitize(random_sample(N), bins)])


def read_LM_to_dict(path):
    d = {}
    with open(path, 'r') as f:

        for line in f:
            values = line.split('\t')
            # print(values)
            d[values[0]] = float(values[1]) # TODO: float, double or numpy?
    return d
#here we make sure the user provides a training filename when
#calling this program, otherwise exit with a usage error.
if len(sys.argv) != 2:# if not (isclose(sum(list(distribution.values())), 1.0)):
#     print('ERROR: Probability distribution does not sum to 1')
#     sys.exit(1)
    print("Usage: ", sys.argv[0], "<training_file>")
    sys.exit(1)

infile = sys.argv[1] #get input argument: the training file

#This bit of code gives an example of how you might extract trigram counts
#from a file, line by line. If you plan to use or modify this code,
#please ensure you understand what it is actually doing, especially at the
#beginning and end of each line. Depending on how you write the rest of
#your program, you may need to modify this code.
with open(infile) as f:
    for line in f:
        line = preprocess_line(line) #doesn't do anything yet.
        for j in range(len(line)-(3)):
            trigram = line[j:j+3]
            tri_counts[trigram] += 1

#Some example code that prints out the counts. For small input files
#the counts are easy to look at but for larger files you can redirect
#to an output file (see Lab 1).
# print("Trigram counts in ", infile, ", sorted alphabetically:")
# for trigram in sorted(tri_counts.keys()):
#     print(trigram, ": ", tri_counts[trigram])
# print("Trigram counts in ", infile, ", sorted numerically:")
# for tri_count in sorted(tri_counts.items(), key=lambda x:x[1], reverse = True):
#     print(tri_count[0], ": ", str(tri_count[1]))

path = 'model-br.en'
# f = open(path,'r')
# content = f.read()
# f.close()
# content = content.strip('\n')

# content = re.sub('\n\s*\n', '',content)
# print(content)
# arr = np.loadtxt(content)
# print(arr.shape)

# print(read_LM_to_dict(path))
distribution = read_LM_to_dict(path)
str_list = generate_from_LM(distribution, 300)
print(str_list)
# if not (isclose(sum(list(distribution.values())), 1.0)):
#     print('ERROR: Probability distribution does not sum to 1')
#     sys.exit(1)
