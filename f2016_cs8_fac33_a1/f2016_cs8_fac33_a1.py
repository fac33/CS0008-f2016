perfer = int(input("please tell us what mesuring system you want to use, for km and liter, please type 1, else please type 0"))

if(perfer == 0):
        mile = float(input("please type in the miles you have used."))
        gallon = float(input("please type in the gallons you have used."))
        KM = 0.621371*mile
        liter = 0.264172*gallon
        consumption1 = mile/gallon
        consumption2 = (liter/KM)*100
elif(perfer == 1):
        KM = float(input("please type in the kms you have used."))
        liter = float(input("please type in the litters you have used"))
        mile = 1.60934*KM
        gallon = 3.78541*liter
        consumption1 = mile/gallon
        consumption2 = (liter/KM)*100
else:
        print("there must be something wrong with your typing. You are a mean person. SEE YOU")
# now we are going to deal with the Consumption Category
if(consumption2 >20):
    CC = "extremly poor"
elif(consumption2<=20 and consumption2>15):
    CC = "Poor"
elif(consumption2<=15 and consumption2>10):
    CC = "Average"
elif(consumption2<=10 and consumption2>8):
    CC = "Good"
elif(consumption2<=8):
    CC = "Excellent"
else:
    print("I don't know why but there must be something wrong")
m = ("%.3f" % mile)
k = ("%.3f" % KM)
g = ("%.3f" % gallon)
l = ("%.3f" % liter)
C1 = ("%.3f" % consumption1)
C2 = ("%.3f" % consumption2)


A = ["                    ","USC","               ","Metric"]
A1 = ["Distance-------:",m+"miles","  ",k+"Km"]
A2 = ["Gas------------:",g+"gallons","    ",l+"liters"]
A3 = ["Consumption----:",C1+"gpm","    ",C2+"1/100Km"]
print('A={0}'.format(A))
print('A1={0}'.format(A1))
print('A2={0}'.format(A2))
print('A3={0}'.format(A3))

print("Gas Consumption Rating : ",CC)
