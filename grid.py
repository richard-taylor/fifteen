#!/usr/bin/python

import optparse
import sys

parser = optparse.OptionParser(usage = """%prog [options]

Read a list of 15-letter words from stdin and try to find a set that fits
into a 15x15 crossword grid with minimal blank space. This can either be
8+8 words crossing at the odd letters or 7+7 words crossing at the evens.""")

parser.add_option("--odd", action="store_true", default=False, help=
	"Cross the words on the odd letters. This gives a grid of 8 words across "
	"and 8 words down. By default the even letters are crossed, which gives "
	"7 words across and 7 words down.")

(options, leftover) = parser.parse_args()

if options.odd:
	cross_from = 0
	length = 8
else:
	cross_from = 1
	length = 7

# keep all the possible sets of crossing letters (length 1, 2, 3 etc.)
# crosses[0] is the set of possible opening letters, crosses[1] is the
# set of possible opening 2-letter pairs.
crosses = [set() for i in range(0, length)]

# read in the words

total = 0
mapback = {}		# map from the crossing letters to the original word(s)

for line in sys.stdin.readlines():
	word = line.strip()
	if len(word) != 15:
		sys.stderr.write("ignoring '" + word + "'\n")
		continue
		
	crossletters = word[cross_from::2]
	
	for i in range(0, length):
		crosses[i].add(crossletters[0:i+1])
	
	if not crossletters in mapback:
		mapback[crossletters] = set()
	mapback[crossletters].add(word)
	
	total += 1
	
print "words =", total, ", unique crosses =", len(crosses[-1])

# print out a full grid

def print_grid(rows, cols):
	for r in rows:
		print r
	print
	
	for r in rows:
		print r, ":", " ".join(mapback[r])
	print
	
	for c in cols:
		print c, ":", " ".join(mapback[c])
	print
		
# test whether a new word can appear below a given list of rows

def possible(cols, word):

	intro = len(cols[0])
	for i,col in enumerate(cols):
		if not col + word[i] in crosses[intro]:
			return False
			
	return True
	
# try to add another row to a partially filled grid

def add_row(rows, cols):
	if len(rows) == length:    # the grid is full
		print_grid(rows, cols)
		return
		
	# try each word on the next row
	for word in crosses[-1]:
		if possible(cols, word):
			add_row(rows + [word], [cols[i] + word[i] for i in range(0, length)])
			
# try each word in the top row

for n,word in enumerate(crosses[-1]):
	print (n+1), "out of", len(crosses[-1])
	add_row([word], word)

