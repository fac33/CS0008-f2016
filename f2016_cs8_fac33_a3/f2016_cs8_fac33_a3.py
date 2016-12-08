import copy
# create a variable to put the data file name in it.
filename = "f2016_cs8_a3.data.txt"
# open the data file
K = open(filename,'r')
# read info in it line by line, without \n .

name = K.readlines()# read the file names in a list

# remove '\n'
n = 0
for line in name:
    line = line.rstrip('\n')
    name[n] = line
    n = n+1


# now we can find the total files we have to deal with
totalfile = len(name)
#print(name)
# then we need to open all of the files writed in the data file.
contant = []
for item in name:
    P = open(item,'r')
    contant1 = P.readlines()
    contant.extend(contant1)

#then we remove '\n'
# and split the line in to different datas
k = 0
for data in contant:
    data = data.rstrip('\n')
    data = data.split(',')
    contant[k] = data
    k = k+1
#then we need to remove the "name distance" part
w = 0
for rmv in contant:
    if "distance" in rmv:
        del contant[w]
    w = w+1
# then we can find the total line we have read
totalline = len(contant)

# then it's time for us to count for the total distance people run
totaldistance = 0
for dist in contant:
    totaldistance += float(dist[1])
#print(totaldistance)
#print(contant)





# all the following part is about how to find the exact best runner and worst runner.
#transfer the list into dictionary which might be easier to deal with
contant2 = dict(contant)
contant3 = copy.deepcopy(contant)
contant4 = copy.deepcopy(contant)
contant_multi = []
everyrepeater = []
temp = len(contant)

print(contant2)
#test
#print(temp)
#print(totalline)
# then we begin to add all the same person's distance
a = 0
b = 0

finaldist = {}
for a in contant2.keys():
    m = 0
    r = 0
    for b in contant3:
        if a == b[0]:
            m = m + float(b[1])
            r +=1
            everyrepeater.append(r)
            print(m)
            finaldist[a] = m

# in here, we need to prepare for a list to print in the final document.
repr = 0
for runners in contant4:

        runners.append(everyrepeater[repr])
        repr+=1

z = list(finaldist.values())
y = list(finaldist.keys())
max_value = y[z.index(max(z))]
max_runner = finaldist.get(max_value)
#test
#print(max_runner)
#print(max_value)
#then the worst runner
z = list(finaldist.values())
y = list(finaldist.keys())
min_value = y[z.index(min(z))]
min_runner = finaldist.get(min_value)
#test
#print(min_runner)
#print(min_value)
#final step, find how many people run and how many have multiple records
parti = len(finaldist)
multi = totalline - parti



#finally, we print datas all.
def printKV(key,value,klen=0 ):
    KL = max(len(key),klen)
    print(format(key,str(KL)+'s'),':',
   value )
print(finaldist)
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
f = open("f2016_cs8_fac33_a3.data.output.csv",'w')
for each in contant4:
    ff = str(each)+'/n'
    f.write(ff)
f.close()
K.close()


