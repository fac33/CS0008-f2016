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
# The program should provide output on the screen similar to the following:
#Number of Input files read : xx
#Total number of lines read : xx
#total distance run : xxxx.xxxxx
#max distance run : xxxx.xxxxx
# by participant : participant name
#min distance run : xxxx.xxxxx
# by participant : participant name
#Total number of participants : xx
#Number of participants
# with multiple records : xx
#The program should also create an output file reporting name of the participant, how many times their
#name appears in the input files and the total distance run. Each row should be as follows:
#Max,3,124.23
#Barbara,2,65.00
#Luka,1,12.87





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
append = []
contant0 = []  # this one will be the vary basic list contain the basic data.
for item in name:
    P = open(item,'r')  # open the file
    append = P.readlines()
    contant.extend(append)
P.close()
totaldistance = 0
for data in contant:
    data = data.rstrip('\n')
    data = data.split(',')
    if not "distance" in data:
        contant0.append({'name': data[0].strip(' '), 'distance':float(data[1])})
        totaldistance += float(data[1])


#now it is time for us to define the class of participation.
class participant:
    """ participant class"""

    # properties
    # name of the participant
    name = "unknown"
    # total distance run by the participant
    distance = 0
    # total number of runs by the participant
    runs = 0

    # methods
    # initializer methods
    def __init__(self, name, distance=0):
        # set name
        self.name = name
        # set distance if non zero
        if distance > 0:
            # set distance
            self.distance = distance
            # set number of runs accordingly
            self.runs = 1
            # end if

    # end def __init__

    # addDistance method
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1
            # end if

    # end def addDistance

    # addDistances method
    def addDistances(self, distances):
        # loops over list
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
                # end if
                # end for

    # end def addDistance

    # return the name of the participant
    def getName(self):
        return self.name

    # end def getName

    # return the total distance run computed
    def getDistance(self):
        return self.distance

    # end def getDistance

    # return the number of runs
    def getRuns(self):
        return self.runs

    # end def getRuns

    # stringify the object
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')
        # end def __init__

    # convert to csv
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])
    # end def tocsv

# ok, now we have finished all the def class work and we need to move on to how to assign the datas in files to class.
# then we get how many files we need to deal with.
NumberofFile = len(name)
# and Totaline is the total line of all three files of datas.
Totalline = len(contant0)
print(Totalline)


#then I decided to find all the participants using a dictionary.
participants = {}


for item in contant0:
    if not item['name'] in participants.keys():
        participants[item['name']] = participant(item['name'])
        # insert distance in the list for this participant
    participants[item['name']].addDistance(item['distance'])



minDistance = { 'name' : None, 'distance': None }
# maximum distance run with name
maxDistance = { 'name' : None, 'distance': None }
# appearences dictionary
apparences = {}



for name, object in participants.items():
    # get the total distance run by this participant
    distance = object.getDistance()
    # check if we need to update min
    # if this is the first iteration or if the current participant distance is lower than the current min
    if minDistance['name'] is None or minDistance['distance'] > distance:
        minDistance['name'] = name
        minDistance['distance'] = distance
    # end if
    # check if we need to update max
    # if this is the first iteration or if the current participant distance is lower than the current min
    if maxDistance['name'] is None or maxDistance['distance'] < distance:
        maxDistance['name'] = name
        maxDistance['distance'] = distance
    # end if
    #
    # get number of runs, aka apparences from participant object
    participantAppearences = object.getRuns()
    #
    # check if we need to initialize this entry
    if not participantAppearences in apparences.keys():
        apparences[participantAppearences] = []
    apparences[participantAppearences].append(name)
# end for

#
# compute total number of participant
# this is equivalent to the length of the participantDistances
totalparticipant = len(participants);

#
# compute total number of participants with more than one record
# extract all the participants that have 2 or more runs
# and count th enumber of elements in the list with len()
totalNumberOfParticipantWithMultipleRecords = len([1 for item in participants.values() if item.getRuns() > 1])


# set format strings
INTEGER = '10d'
FLOAT = '12.5f'
STRING = '20s'

# provide requested output

print(" Number of Input files read   : " + format(NumberofFile,INTEGER))
print(" Total number of lines read   : " + format(Totalline,INTEGER))

print(" Total distance run           : " + format(totaldistance,FLOAT))

print(" Max distance run             : " + format(maxDistance['distance'],FLOAT))
print("   by participant             : " + format(maxDistance['name'],STRING))

print(" Min distance run             : " + format(minDistance['distance'],FLOAT))
print("   by participant             : " + format(minDistance['name'],STRING))

print(" Total number of participants : " + format(totalparticipant,INTEGER))
print(" Number of participants")
print("  with multiple records       : " + format(totalNumberOfParticipantWithMultipleRecords,FLOAT))


#
# create output file
outputFile = "f2016_cs8_fac33_a3.output.csv"
# open file for writing
fh = open(outputFile,'w')
# write header in file
fh.write('name,records,distance\n')
# loop on all the participants
for name, object in participants.items():
    # write line in file
    fh.write(object.tocsv() + '\n')
#end for
# close files
fh.close()
