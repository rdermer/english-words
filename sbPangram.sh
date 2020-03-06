#!/bin/bash
if [[ $# -ne 1 || ${#1} -ne 7 ]]; then
echo usage: $0 7letters
exit
fi
egrep "^[$1]+$" words_alpha.txt | grep ${1:0:1} | grep ${1:1:1} | grep ${1:2:1} | grep ${1:3:1} | grep ${1:4:1} | grep ${1:5:1} | grep ${1:6:1}
