#       Carleton-Code-Gym
#       Distance over Time Calculator
#       Determines the Time it takes to reach your destination
#       Created by: Ahmad Osman (Co-Founder CCG)
#       Date: 6/2/2016
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
DistanceTraveled=int(input("please enter the distance you are traveling in km: "))       #Determines the distance the car is traveling
Speed=int(input("please enter the speed you will be traveling at in km/h: "))            #Determines the speed the car is traveling at

Time=DistanceTraveled/Speed                                                              #Determines the time it takes the car to reach it's destination

print("It will take you", "%.1f" % Time,"hours to get there")                            #Rounds the time to the nearest tenth of a decimal.