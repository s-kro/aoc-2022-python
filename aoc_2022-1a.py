#! /usr/bin/python3


# Advent of Code Day 1 Part 1

f = open("aoc_2022-1.dat")

tc = 0 # total calories
mc = 0 # most calories
for line in f:
    if line != "\n":
        tc += int(line)

    else:
        mc = max(mc, tc)
        tc = 0

f.close()

print ("Most calories: ", mc)
