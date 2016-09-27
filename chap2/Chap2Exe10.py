# Template for code submission
# name: Fanyang Cheng
# email: fac33@pitt.edu
# date: 09/06/2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
#
# Description
# description of this file goes here
# Starting with Python, Chapter 1, Exercise 10
# notes
# template

cookies = float(input("please tell me how many cookies you want to make.\
 Please type in an integer."))
# ask for the amount of cookies
if (cookies%1 != 0):
    print("what you just type is wrong, please try again later.")
else :
    sugar = cookies * 300/48
    butters = cookies * 240/48
    flours = cookies * 330/48

    #calculate the each components' amount

    print("you need ", sugar, "g of sugar.")
    print("you need", butters, "g of butter.")
    print("you need", flours, "g of flour.")

# output