#!/bin/bash
# usage: $0 letters required
#egrep '^[varmint]+$' words_alpha.txt | grep r | grep -v '^.$' | grep -v '^..$' | grep -v '^...$'
egrep "^[$1]+$" words_alpha.txt | grep $2 | grep -v '^.$' | grep -v '^..$' | grep -v '^...$'
