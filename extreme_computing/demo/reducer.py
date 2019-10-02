#!/usr/bin/env python2
# Reducer in: [genre:str]  out: [genre:str]
import sys

last_val = None

for line in sys.stdin:
    # Read each line that contains exactly one genre
    genre = line.strip()

    # The input is sorted but contains duplicates
    if last_val is None: # Don't forget the first genre of the input
        last_val = genre
    elif last_val != genre:
        # Allow no duplicates in the output
        print(last_val)
        last_val = genre

# Don't forget the last genre of the input
print(last_val)
