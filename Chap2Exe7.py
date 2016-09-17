# Template for code submission
# name: Fanyang Cheng
# email: fac33@pitt.edu
# date: 09/06/2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
#
# Description
# description of this file goes here
# Starting with Python, Chapter 1, Exercise 7
# notes
# template

miles = float(input("please type in the total miles you have driven"))
gallons = float(input("please type in the total gas you have used"))
km = miles/1.60931
litersall = gallons*3.541178
print("the KM you have driven is ", km, "KM")
print("the liters you have used is ", litersall, "L")
youhao = 100*litersall/km
print("L per 100 km is ", youhao, "L/100km")
