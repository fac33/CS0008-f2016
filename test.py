#def loop(x):
 # x = int(x)
  #t = -1
  #for num in range(x+1):
   #   t += 1
    #  print (t)



#y= loop(23456)

global a
global b
global c
global d
global e


def aveage(a,b,c,d,e):
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    m = (a+b+c+d+e)/5
    print("the average grade is ", m)

file = input("first file")
TTD = 0
TTN = 0














while file and file != "quit" and file != "q":
    fh = open('file','r')
    PD,PTN = processfile(fh)
    printkv('string',PTN)
    printkv('string',PD)
    fh.close()
    TTD +=PD
    TTN += PTN







PTN = 0
PD = 0
FO = open()
for line in FO:

    line = line.rstrip("\n")
    temp = line.split(",")
    dist = float(temp[1])
    PD += dist
    PTN += 1
def printkv(partialnumber,PTN):
