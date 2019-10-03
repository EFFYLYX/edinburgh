#!/usr/bin/python2.7
# mapper_combiner.py
import sys

from collections import defaultdict

word_dict = defaultdict(int)
MAX_SIZE = 100

def map_function(title):
    fields = title.strip().split('\t')         # Split title to fields
    primaryTitle = fields[2]                   # Select the required field
    for word in primaryTitle.strip().split():  # Split primary title by words
        yield word, 1                          # Use a word as a key

for line in sys.stdin:
    # Call the map_function for each line in the input
    for key, value in map_function(line):
        # Agregate value for a word locally
        word_dict[key] += value

        # To keep O(1) space, we bound the size of our memory footprint
        if len(word_dict) > MAX_SIZE:
            for key, value in word_dict.items():
                print(key + "|" + str(value))

            word_dict.clear()

# Emit leftover key-value pairs and use '|' as the delimiter
for key, value in word_dict.items():
    print(key + "|" + str(value))
