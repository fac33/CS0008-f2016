# Template for code submission
# name: Fanyang Cheng
# email: fac33@pitt.edu
# date: 12/10/2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
#
# Description
# description of this file goes here
# Starting with Python, final projet
# notes
# template




#first we need to read in all the names of the file we need to read
filename = "f2016_cs8_fp.data.txt"
# open the data file
K = open(filename,'r')
# read info in it line by line, without \n .

name = K.readlines()# read the file names in a list

# MN: you need to close the file
K.close()

# remove '\n'

for line in name:
    line = line.rstrip('\n')
