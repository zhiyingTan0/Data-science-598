#!/bin/sh
filename="$1" #input file name
cat $1 | wc -l | xargs
head -n 1 $1
tail -n 10000 $1 | grep -i "potus" | wc -l | xargs
sed -n '101,201p' $1 | grep "fake"| wc -l | xargs

