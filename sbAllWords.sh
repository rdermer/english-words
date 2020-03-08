#!/bin/bash

# spelling bee find all words 

if [[ $# -ne 2 || ${#1} -ne 7 || ${#2} -ne 1 ]]; then
echo usage: $0 7letters 1required
exit
fi

x=`echo $1 | tr "[:upper:]" "[:lower:]"`
y=`echo $2 | tr "[:upper:]" "[:lower:]"`
egrep "^[$x]+$" words_alpha.txt | grep $y | grep -v '^.$' | grep -v '^..$' | grep -v '^...$'
