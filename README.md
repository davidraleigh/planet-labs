# PlanetLabs All Anagrams
This all anagrams python script takes a dictionary as input and returns all the lists of anagrams for words in the dictionary (words longer than 3 characters). The python script uses a dictionary that will be a file on disk with one line per word. Your operating system likely already has such a file in /usr/dict/words or /usr/share/dict/words.

### Running the Script
If your operating system has a dictionary file in one of the 2 directories mentioned above, run with:
```bash
$ python anagram.py
```

If you need to specify the path to a dictionary file, run with:
```bash
$ python anagram.py /path/to/dictionary/file
```

### The Output
In this version of anagram.py words that are capitalized are listed along with the same word without capitalization. 'Babel' and 'babel' are not anagrams of one another, but choosing to omit one means a more confusing system of listing out anagrams (should 'Babel' and 'babel' each have their own separate listing? Should one or the other be omitted completely?). Below is a sample of the output. The line order is sorted by the prime number key associated with an anagram and the words in each line are sorted alphabetical (with capitalized words being one alphabetically sorted set followed by the lowercase alphabetically sorted set)
```bash
Abba, baba
abac, caba
Caca, acca
Adad, Adda, Dada, adad, adda, dada
Baal, Bala, alba, baal
abed, bade, bead
Maba, amba
Bana, anba
bach, chab
Arab, arba, baar, bara
...
```
