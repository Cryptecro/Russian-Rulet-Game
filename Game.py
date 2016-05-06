#Status:Playable
import sys
import time 
import random 
from sys import version_info

player1 = raw_input("Enter player 1 name: ")
player2 = raw_input("Enter player 2 name: ")
player3 = raw_input("Enter player 3 name: ")
player4 = raw_input("Enter player 4 name: ")
vars = [player1,player2,player3,player4]

print random.sample(vars, 1)
print "Dies"
