#!/usr/local/bin/python3

import argparse
import os
import sys
import re

class SBAllWords:
    def __init__(self, wordfile, letters, required, minlength):
        self.wordfile = wordfile if wordfile else os.path.join(os.path.dirname(os.path.realpath(__file__)), "words_alpha.txt")
        self.letters = letters.lower()
        self.required = required.lower()
        self.minlength = minlength
        self.matchword = re.compile(f"^[{self.letters}]+$")

    def __iter__(self):
        self.words = open(self.wordfile, newline='\n')
        return self

    def __next__(self):
        for word in self.words:
            word=word.strip()
            wordLower = word.lower()
            if self.matchword.match(wordLower) and len(word) >= self.minlength and self.required in wordLower:
                return word
        self.words.close()
        raise StopIteration

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w',  "--words", action="store_true", dest="words", default=None,  help="word list")
    parser.add_argument('letters', nargs=2, help='search string for pangrams')
    args=parser.parse_args()

    allwords = SBAllWords(args.words, args.letters[0], args.letters[1], 4)
    for word in allwords:
        print(word)

if __name__ == "__main__":
    sys.exit(main())
