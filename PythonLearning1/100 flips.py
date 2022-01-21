#       Carleton-Code-Gym
#       The 100 coin flipper
#       flips a coin 100 times and records the results
#       Created by: Ahmad Osman (Co-Founder CCG)
#       Date: 29/3/2016
#------------------------------------------------------------------------------------------------------------------------
"""
The following program randomly flips a coin 100 times and using probability, determines the 
outcome being heads or tails. This program is not advanced nor complicated, meaning it does not
use True or False boolean; it uses the values 1 and 2 to determine if the state is true or not.
"""
#------------------------------------------------------------------------------------------------------------------------
import random


fivetails=0
fourtails=0
threetails=0
twotails=0
onetails=0
notails=0

for j in range(100):                        #Sets the range for the amount of group flips.
    numTails = 0
    for i in range(5):                      #Sets the range for how many flips per group
        tails=random.randint(1,2)           #Sets a random range
            
        if tails == 1:                      #command that is followed when one of the random integers is selected
            print("heads ", end="")
    
        if tails == 2:
            print("tails ", end="")         #command that is followed when one of the random integers is selected
            numTails = numTails + 1         #Counter for how many times it flips per group
        

    print()
    print("You got", numTails, "tails")
    
    if numTails == 5:                                       
        fivetails=numTails+1
    elif numTails == 4:
        fourtails=numTails+1
    elif numTails == 3:
        threetails=numTails+1               #for all of the following statments: counter for the following command, counts how many times the group prints a certain ammount of tails
    elif numTails == 2:
        twotails=numTails+1
    elif numTails == 1:  
        onetails=numTails+1
    else:
        notails=numTails+1
    
print()
print("you got fivetails", fivetails, "times")
print()
print("you got fourtails", fourtails, "times")
print()
print("you got threetails", threetails, "times")
print()
print("you got twotails", twotails, "times")
print()
print("you got onetails", onetails, "times")
print()
print("you got notails", notails, "times")
