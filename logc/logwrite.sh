#!/bin/sh

for i in {1..100000}
do
    echo $i
    echo "lines $i" >> log.txt
done