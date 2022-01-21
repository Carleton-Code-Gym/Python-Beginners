#       Carleton-Code-Gym
#       Even/Odd Calculator
#       Determines if a number is even or odd and negative or positive
#       Created by: Ahmad Osman (Co-Founder CCG)
#       Date: 10/2/2016

#-------------------------------------------------------------------------------------------------
"""
The program below assists users in determining if the input value, a random number, is even or odd.
The program will also check if that value is zero, positive, or negative. This type of program can
be further expanded into real time situation development such as, Machine Learning.
"""
#-------------------------------------------------------------------------------------------------
number = int(input("Enter number here: "))
print("The number is ",end="")
if number == 0:                                 #Determines if the number is zero
    print("zero", end="")
elif number > 0:                                  #Determines if the number is positive
    print("positive", end="")           
elif number < 0:                                  #Determines if the number is negative
    print("negative", end="")            
elif number % 2 == 0 :                            #Determines if the number is even
    print(" and even.")
else:                                           #Determines if the number is odd
    print(" and odd.")
    