#
# MN: you are missing the header with the info on user, instructor and course
#
# Notes:
# MN: You need to insert more comments and explain what each single blocks of code
file = 0


file = input("please give me the name of the file you want me to deal with.")

# MN: what does this function do?
def processFile(fh):
    PTN = 0
    PD = 0
    FO = open(file,'r')
    for line in FO:
        line = line.rstrip("\n")
        temp = line.split(",")
        dist = float(temp[1])
        PD += dist
        PTN += 1
    return (PD,PTN)

# MN: what does this function do?
def printKV(key,value,klen=0 ):
    KL = max(len(key),klen)
    if isinstance(value,str):
        FS = '20s'
    elif isinstance(value,float):
        FS = '10.3f'
    elif isinstance(value,int):
        FS = '10'
    else:
        print("there must be something wrong with your data.")
    print(format(key,str(KL)+'s'),
   format(value,FS) )

TTD = 0
TTN = 0

while file and file != "quit" and file != "q":
    fh = open(file,'r')
    PD,PTN = processFile(fh)
    printKV('total lines in this file',PTN)
    printKV('total distance in this file',PD)
    fh.close()
    TTD +=PD
    TTN += PTN
    file = input('next file')

printKV('total distance in all files',TTD)
printKV('total lines in all files',TTN)
