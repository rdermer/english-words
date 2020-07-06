#!/usr/local/bin/python3

import argparse
import os
import sys

class SBPangram:
    def __init__(self, wordfile, letters):
        self.wordfile = wordfile if wordfile else os.path.join(os.path.dirname(os.path.realpath(__file__)), "words_alpha.txt")
        self.letters = letters
        self.matchset=set(letters.lower())

    def __iter__(self):
        self.words = open(self.wordfile, newline='\n')
        return self

    def __next__(self):
        for word in self.words:
            word=word.strip()
            if self.matchset == set(word.lower()):
                return word
        self.words.close()
        raise StopIteration

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w',  "--words", action="store", dest="words", default=None,  help="word list")
    parser.add_argument('letters', help='search string for pangrams')
    args=parser.parse_args()

    sbpangram = SBPangram(args.words, args.letters)
    for word in sbpangram:
        print(word)

if __name__ == "__main__":
    sys.exit(main())