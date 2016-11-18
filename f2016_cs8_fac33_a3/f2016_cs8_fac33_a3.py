# create a variable to put the data file name in it.
filename = "f2016_cs8_a3.data.txt"
# open the data file
K = open(filename,'r')
# read info in it line by line, without \n .

name = K.readline()
# now we can find the total files we have to deal with
totalfile = len(name)
#print(name)
# then we need to open all of the files writed in the data file.
for item in name:
    P = open(item,'r')
    contant = P.readline()
    contant[len(contant):len(contant)] = contant
# then we can find the total line we have read
totalline = len(contant)

#deep copy the list
contant1 = []
for n in contant:
    contant1 = contant1.append(n)


#print(contant)
#then we just find the data part of all the files
contant = float(contant.rstrip('\n').split(',')[1])
#and then we need to deal with how much the total distance all the runners run.
totaldistance = sum(contant)     # no idea if the sum command is right


# then we began to deal with the spcific person with max distance and min distance

