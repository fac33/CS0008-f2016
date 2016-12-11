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
n = 0   #this n is a recorder which will help us to record the position where the file name is in the list "name".
for line in name:
    line = line.rstrip('\n')
    name[n] = line # here is where I use the n to reassign the file name without "/n" to the list "name".
    n+=1 # here add 1 to n

# then ,we read all of the contant in to a list of list, "contant"
contant = []
for item in name:
    P = open(item,'r') # open the file
    contant1 = P.readlines()
    contant.extend(contant1)
    # close the file
    P.close()
    # then we remove '\n'
    # and split the line in to different datas
    # MN: why do you define and update a counter (K) but you never use it
    k = 0
    for data in contant:
        data = data.rstrip('\n')
        data = data.split(',')
        contant[k] = data
        if "distance" in data:
            del contant[k]
        k = k + 1


#now it is time for us to define the class of participation.
class participation:

    # properties
    # name of the participant
    name = ""
    # total distance run by the participant
    distance = 0
    # total number of runs by the participant
    runs = 0

    # and we need to define the initializer which contain how to set name, set total distance and how to set how many times the participantions join.
    def __init__(self, name, distance = 0):
        # set name
        self.name = name
        # set distance if the distance is meaningful (not zero)
        if distance > 0:
            # set distance.
            self.distance = distance
            # set number of runs.
            self.runs = 1
