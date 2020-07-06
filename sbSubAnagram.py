#!/usr/local/bin/python3

import argparse
import os
import sys
import re
import collections

class SBSubAnagram:
    def __init__(self, wordfile, letters, minlength):
        self.wordfile = wordfile if wordfile else os.path.join(os.path.dirname(os.path.realpath(__file__)), "words_alpha.txt")
        self.letters = letters.lower()
        self.minlength = minlength
        self.matchword = collections.Counter(self.letters)

    def __iter__(self):
        self.words = open(self.wordfile, newline='\n')
        return self

    def __next__(self):
        for word in self.words:
            word=word.strip()
            if (len(word) < self.minlength):
                continue
            wordLowerCounter = collections.Counter(word.lower())
            if all(wordLowerCounter[char] <= self.matchword[char] for char in wordLowerCounter):
                return word
        self.words.close()
        raise StopIteration

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w',  "--words", action="store_true", dest="words", default=None,  help="word list")
    parser.add_argument('letters', help='search string for sub anagrams')
    args=parser.parse_args()

    allwords = SBSubAnagram(args.words, args.letters, 2)
    for word in allwords:
        print(word)

if __name__ == "__main__":
    sys.exit(main())
