#! /usr/bin/python3


# Advent of Code Day 2 Part 1

f = open("aoc_2022-2.dat")

me = ('', 'X', 'Y', 'Z') # my choice - rock, paper, scissors
op = ('A', 'B', 'C') # opponent's choice - r, p, s
sc = 0               # score ## my choice is indexed from 1!
for line in f:
    (o, m) = line.rstrip().split(' ')
    sc += me.index(m) + ((me.index(m) - op.index(o)) % 3) * 3 
f.close()

print("My rock paper scissors score:", sc)
