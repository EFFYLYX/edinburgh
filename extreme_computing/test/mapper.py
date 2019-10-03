#!/usr/bin/env python2
# Mapper in: title.basics.tsv out: [genre:str]
import sys
from collections import defaultdict

#\tconst\ttitleType\tprimaryTitle\toriginalTitle\tisAdult\tstartYear\tendYear\truntimeMinutes\tgenres
word_dict = defaultdict(int)
MAX_SIZE = 100
def map_function(title):
    fields = title.strip().split('\t') # split title to fields
    primaryTitle = fields[2]
    for word in primaryTitle.strip().split():
        yield word, 1 # use a word as a key


for line in sys.stdin:
    # Call map_function for each line in the input
    for key, value in map_function(line):
        # Emit key-value pairs using '|' as a delimeter
        print(key + "|" + str(value))
