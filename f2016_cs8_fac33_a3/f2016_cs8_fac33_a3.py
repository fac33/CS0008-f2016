#
# MN: header with info on user, instructor and class missing
#
# Notes:
#

# Template for code submission
# name: Fanyang Cheng
# email: fac33@pitt.edu
# date: 12/10/2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
#
# Description
# description of this file goes here
# Starting with Python, assignment 3
# notes
# template







import copy
# create a variable to put the data file name in it.
# MN: why did you hard code the file name for the master list?
filename = input("please type in the file that contains the files' name I need to deal with.")
# open the data file, with the name provided by the user
try:
    K = open(filename,'r')
    # read info in it line by line, without \n .
except:
    print("there might be something wrong with your file, sorry.")

name = K.readlines()# read the file names in a list

# MN: you need to close the file
#close the file.
K.close()

# remove '\n'
# MN: why do you use a countr (variable n) that you never use
n = 0 # this n is a recorder of the position of the file name in the list "name".
for line in name:
    line = line.rstrip('\n')
    name[n] = line # here is where I use n to reassign the line without "/n" to the list "name" and the recorde of how many files we have read
    n = n+1


# now we can find the total files we have to deal with
totalfile = len(name)
#print(name)
# then we need to open all of the files writed in the data file.
contant = []
for item in name:
    P = open(item,'r')
    contant = P.readlines()

    # MN: you need to close the file
    #close the file
    P.close()

#then we remove '\n'
# and split the line in to different datas
# MN: why do you define and update a counter (K) but you never use it
k = 0  # just like n, this k is used as a recorder of the position of those datas.
totaldistance = 0  # this variable is used to cont for the totaldistance all of the participants run.
for data in contant:
    data = data.rstrip('\n')
    data = data.split(',')
    contant[k] = data  # here, we use the k to reassign those datas back to the list "contant"

    k = k+1  # after plus one, we can continuously find the next one of this list.

#then we need to remove the "name distance" part
# MN: why do you define and update a counter (w) but you never use it
w = 0
# MN: can we combine it with the previous for loop?
for rmv in contant:
    if "distance" in rmv:
        del contant[w]
    w = w+1
# then we can find the total line we have read
totalline = len(contant)

# then it's time for us to count for the total distance people run
# MN: can we combine with the previous loop?
totaldistance = 0
for dist in contant:
    totaldistance += float(dist[1])

# then we can find the total line we have read
totalline = len(contant)



# all the following part is about how to find the exact best runner and worst runner.
#transfer the list into dictionary which might be easier to deal with
# MN: why do you define 1 dictionary and 2 list (3 if we include the original) with the same info in it?
contant2 = dict(contant)  #this dictionary is prepared for the calculation of each participants' distance and number of runs.
contant3 = copy.deepcopy(contant)  #this list used as the same function of the contant2
contant4 = copy.deepcopy(contant)  # this list is prepared for the final print of the file output.
contant_multi = [] # this list is prepared to put all of those participants who have more than once records.
everyrepeater = []  # this list contain all of the number of runs for all the participants in order of the apperance order of participants in those three files.
temp = len(contant)

# MN: before you submit your script/project, make sure that you comment, or even better, remove all the debugging print that you ahve in the code

# then we begin to add all the same person's distance
a = 0
b = 0

finaldist = {} #this variable is used for the final answer.
# MN: why do you have a nested for loop looping on the same info?
#     maybe if you had commetned a little bit more, it would be more understandable
#     Not sure what you are doing here?
for a in contant2.keys(): #in here, we get each participant's name using the key method in dictionary.
    m = 0  # this varealbe is created for a record of each participant's total distance of run and will soon assign to another variable on outside of the loop
    r = 0  # this variable is created to record for how many repeater (those who have more than one record in those three files)
    for b in contant3: # here,we get through all item of the list "contant3"
        if a == b[0]:  # this is a recognition step to find wether the name in "contant3" is same as the name in the dictionary "contant2"
            m = m + float(b[1])  # if it is, we add the distant to variable m
            r +=1
            everyrepeater.append(r)  # now,we append the value in r (number of runs for each participants in order in to the list.)
            # MN: comment or remove debugging print
            finaldist[a] = m  #here, we assign the value in m to the finaldist with the key of a which contain a string variable of the name of participants.

# in here, we need to prepare for a list to print in the final document.
# MN: why do you define all this if we do not use it later on?
repr = 0
for runners in contant4:

        runners.insert(1,everyrepeater[repr])  #here we append the number of runs of participants into the list of contant4.
        repr+=1

z = list(finaldist.values())
y = list(finaldist.keys())
max_value = y[z.index(max(z))]
max_runner = finaldist.get(max_value)

# MN: you already defined this 2 variable above and here thy should still hold the same value
min_value = y[z.index(min(z))]
min_runner = finaldist.get(min_value)
#test
#print(min_runner)
#print(min_value)
#final step, find how many people run and how many have multiple records
parti = len(finaldist)
multi = totalline - parti



#finally, we print datas all.
# MN: is value properly formatted?
def printKV(key,value,klen=0 ):
    KL = max(len(key),klen)
    print(format(key,str(KL)+'s'),':',
   value )

# MN: please comments or remove the debuggin prints
#print(finaldist)

printKV("Number of imput files read",totalfile)
printKV("total number of lines read",totalline)
printKV("total distance run",totaldistance)
printKV("max distance run",max_runner)
printKV("by participant",max_value)
printKV("min distance run",min_runner)
printKV("by participant",min_value)
printKV("total number of participant",parti)
printKV("number of participants with multiple records",multi)
#print(contant4)
#print(contant)


#finally we will create a file to print all of the joiners' distance, name and their participation times.
# MN: is the format in the otput file, correct?
f = open("f2016_cs8_fac33_a3.data.output.csv",'w')
for each in contant4:
    ff = str(each)+'/n'
    fff = ff.rstrip('[').rstrip(']')
    f.write(fff)
f.close()
K.close()


