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
filename = input("pls input the file with all the files' name you want me to deal with.")
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
    print(contant)
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
# here is the end of __init__ and we need to move on to different functions

# first, the addDistance method which could add the distance of one class.  here I still coout if the distance is zero.
def addDistance(self,distance):
    self.distance += distance
    self.runs +=1  #here we add one to the number of each participants

# end of addDistance

# next one on the list is addDistances which could add a list of distances into one class.
def addDistances(self,distances):
    #here, the variable is a list and we need to add each element in the list. and I also count the zero distance
    #loop distances::
    for items in distances:
            self.distance += items
            self.runs += 1 # here we add one to the number of runs of each participants
#the end of the inner function addDistance.

#then we need to find a way to give the variables in classes out to different global variables.
#so we def get functions that would be the next several things on the list.
# def getDistance:
def getDistance(self):
    return self.distance
#end of getDistance
#def getName:
def getName(self):
    return self.name
#end of getName
#there is one thing missed on the list which is that we need to get the runs variable. So, def getRuns:
def getRuns(self):
    return self.runs
#end of getRuns.

#finally we need to find a formed way to output our answers which is the method __ str__().
#def __str__()

def __str__(self):
    return\
        "Name : " + format(self.name, '>20s') +\
        '\n' +\
        " Distance run : " + format(self.distance, '9.4f') +\
        '\n' +\
        " Runs : " + format(self.runs, '4d')
# end def __str__

#and finally, there will  be a step that we need to print all those information into a csv file.
#so we define toCsv:
def toCsv(self):
    return ','.join([self.name,str(self.runs),str(self.distance)])
#end toCsv

# ok, now we have finished all the def class work and we need to move on to how to assign the datas in files to class.
# then we get how many files we need to deal with.
NumberofFile = len(name)
print(NumberofFile)

