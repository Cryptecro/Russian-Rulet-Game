#Status:Kinda Playable
import sys
import time 
import random 
from sys import version_info

player1 = ("Vincent")#raw_input("Enter player 1 name: ")
player2 = ("Kyler")#raw_input("Enter player 2 name: ")
player3 = ("Zach")#raw_input("Enter player 3 name: ")
player4 = ("Me")#raw_input("Enter player 4 name: ")
doesshoot = 0 
vars = [player1,player2,player3,player4]
Deade = random.choice(vars)
shoot = random.randint(1,7)
  
if shoot < 5:
    print "%s Dies" % Deade
else:
    print "%s Lives" % Deade 

#total = 0
#i = 1

#while i <=4:
    #total += i
    #i += 1
