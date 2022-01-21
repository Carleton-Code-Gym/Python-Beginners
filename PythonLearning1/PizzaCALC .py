#	Carleton-Code-Gym
#   Pizza Program
#	Determines the number of pizzas that need to be ordered
#	Created by:  Ahmad Osman (Co-Founder CCG)
#	Date: 9 Feb 2016
#-------------------------------------------------------------------------------------------------------------------------------------------------
"""
This is a simple yet great calculator. Do you want to order pizza for a party but do not know
how many pizzas to order. This program fixes that issue, by implementing the number of atendees
and how many slices each person will have, the Pizza Calculator will aid in telling you how many
pizzas are needed at eight slices each as well as informing you there if there will be left overs
or not. Enjoy!!!
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------
numPeople = int(input("How many people will be attending the party: "))   #Asks for the number of people attending
numSlicesPerPerson = int(input("How many slices will each person eat: ")) #Asks for the number of slices each person will eat

totalSlicesNeeded = numPeople * numSlicesPerPerson                        #Determines the total number of slices needed

if totalSlicesNeeded % 8 == 0:                                            #Function to determine if there is a remainder of slices
    numPizzas = totalSlicesNeeded // 8                                    #Determines number of pizzas needed if there is no remainder
else:
    numPizzas= totalSlicesNeeded // 8 + 1                                 #Determines number of pizzas needed if there is a remainder

totalSlices = numPizzas * 8                                               #Determines the total number of slices there is

numSlicesRemaining= totalSlices - totalSlicesNeeded                       #Determines the number of slices remaining
print("The amount of pizzas that will need to be ordered is",numPizzas,". The amount of leftover slices will be",numSlicesRemaining,"." )