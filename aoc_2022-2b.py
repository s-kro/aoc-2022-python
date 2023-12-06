#! /usr/bin/python3


# Advent of Code Day 2 Part 2

f = open("aoc_2022-2.dat")

re = ('X', 'Y', 'Z') # results - lose, draw, win
op = ('A', 'B', 'C') # opponent's choice - r, p, s
sc = 0               # score
for line in f:
    (o, r) = line.strip().split(' ')
    sc += (op.index(o) + re.index(r) - 1) % 3 + 1 + re.index(r) * 3
f.close()

print("My rock paper scissors score:", sc)
