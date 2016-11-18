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
print(contant)





# all the following part is about how to find the exact best runner and worst runner.
#transfer the list into dictionary which might be easier to deal with
contant2 = dict(contant)


print(contant2)
#then we just find the data part of all the files
#contant = float(contant.rstrip('\n').split(',')[1])
#and then we need to deal with how much the total distance all the runners run.
#totaldistance = sum(contant)     # no idea if the sum command is right


# then we began to deal with the spcific person with max distance and min distance

