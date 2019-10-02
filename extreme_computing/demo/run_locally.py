#!/usr/bin/env python2
# Mapper in: title.basics.tsv out: [genre:str]
import sys

SKIPVAL = '\\N'
DELIM = '\t'

all_genres = set()

for line in sys.stdin:
    parts = line.strip().split(DELIM)

    if parts[-1] == SKIPVAL:
        continue

    for genre in parts[-1].split(','):
        all_genres.add(genre)

for genre in sorted(all_genres):
    print(genre)
