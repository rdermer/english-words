#!/usr/bin/env python

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def checkit(a,b):
    return a==25-b or 25-a==b

if __name__ == '__main__':
    for word in load_words():
        if len(word) == 6:
            chars = [ord(char)-ord('a') for char in word.lower()] 
            if checkit(chars[0],chars[5]) and checkit(chars[1],chars[4]) and checkit(chars[2],chars[3]):
                print word,chars
