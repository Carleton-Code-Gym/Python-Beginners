#	Carleton-Code-Gym
#   Ottawa Weather channel
#	Determines the weather
#	Created by:  Ahmad Osman (Co-Founder CCG)
#	Date: March 29 2016

import random
sky = random.randint(1,2)
temperature = random.randint(1,2)
if sky == 1:
    print("Today will be sunny", end="")
elif sky == 2:
    print("Today will be cloudy", end="")
if temperature == 1:
    print(" and hot outside.")
elif temperature == 2:
    print(" and cold outside.")