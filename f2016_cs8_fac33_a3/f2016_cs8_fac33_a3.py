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
# then we can find the total line we have read
totalline = len(contant)
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

# then it's time for us to count for the total distance people run
totaldistance = 0
for dist in contant:
    totaldistance += float(dist[1])
#print(totaldistance)
#print(contant)





# all the following part is about how to find the exact best runner and worst runner.
#transfer the list into dictionary which might be easier to deal with
contant2 = dict(contant)
temp = len(contant)

#print(contant2)
#test
#print(temp)
#print(totalline)
# then we begin to add all the same person's distance
a = 0
b = 0
finaldist = {}
for a in contant2.keys():
    for b in contant2.keys():
        if a == b:
            finaldist[a] = float(contant2[a]) + float(contant2[b])
# and then we need to cancel the mistake made by this two for loop.
c = 0
d = 0
finaldist_error = copy.deepcopy(finaldist)
for c in contant2.keys():
    for d in finaldist_error.keys():
        if c == d:
            finaldist_error[d] = float(finaldist_error[d]) - float(contant2[c])
#then we got the mistake data

#then we can use for loop to correct this mistake
e = 0
f = 0
for e in finaldist:
    for f in finaldist_error:
        if e==f:
            finaldist[e] = finaldist[e] - finaldist_error[f]
#test
#print(len(finaldist))
#print(len(finaldist_error))
#then we began to find the bet runner and the worst runner
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
multi = totalline - 3 - parti



#finally, we print datas all.
def printKV(key,value,klen=0 ):
    KL = max(len(key),klen)
    print(format(key,str(KL)+'s'),':',
   value )

printKV("Number of imput files read",totalfile)
printKV("total number of lines read",totalline)
printKV("total distance run",totaldistance)
printKV("max distance run",max_value)
printKV("by participant",max_runner)
printKV("min distance run",min_value)
printKV("by participant",min_runner)
printKV("total number of articipant",parti)
printKV("number of participants with multiple records",multi)

