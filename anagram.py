# Here it is:
# An anagram is a word formed by rearranging the letters of another,
# like "topside" and "deposit". In some cases, there might be as many
# (or more) anagrams than there are characters, like "post", "spot",
# "stop" and "tops".

# Write a program to find all of the anagrams in a dictionary in which
# there are at least 4 letters in the word and at least as many anagrams
# as there are letters.

# The dictionary will be a file on disk with one line per word.
# Your operating system likely already has such a file in
# /usr/dict/words or /usr/share/dict/words.

# The output produced by your code should be in this format:

# emit, item, mite, time
# merit, miter, mitre, remit, timer
# reins, resin, rinse, risen, serin, siren
# inert, inter, niter, retin, trine
# inset, neist, snite, stein, stine, tsine

from string import ascii_lowercase
import sys
import os.path


filepath = "/usr/dict/words"
if len(sys.argv) >= 2:
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("file path provided doesn't exist")
        sys.exit(1)

if not os.path.isfile(filepath):
    filepath = "/usr/share/dict/words"
    if not os.path.isfile(filepath):
        print("file paths /usr/dict/words and /usr/share/dict/words don't exist.")
        print("Provide path as input argument 'python anagram.py /path/to/dictionary'")
        sys.exit(1)

# hashing characters with prime numbers
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
primeMap = {}
for i in range(0, 26):
    primeMap[ascii_lowercase[i]] = primes[i]
# This means that if one word has a hyphen it's anagram must also have a hyphen
primeMap['-'] = 103

anagramMap = {}
with open(filepath) as f:
    for line in f:
        # grabs lowercase word
        word = line.strip().lower()
        count = len(word)
        if count < 4:
            continue

        primeKey = 1
        for c in word:
            primeKey *= primeMap[c]

        # stores the word with capitals, line.strip(), instead
        # of word. 'Babel' and 'babel' are therefore considered anagrams
        if primeKey not in anagramMap:
            anagramMap[primeKey] = [line.strip()]
        else:
            anagramMap[primeKey].append(line.strip())

    for primeKey in sorted(anagramMap):
        if len(anagramMap[primeKey]) > len(anagramMap[primeKey][0]):
            print ', '.join(sorted(anagramMap[primeKey]))
