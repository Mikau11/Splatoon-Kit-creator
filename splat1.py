import time

from wpn_class.Splatoon.Blasters import *;from wpn_class.Splatoon.Brushes import *;from wpn_class.Splatoon.Chargers import * #Splatoon
from wpn_class.Splatoon.Rollers import *;from wpn_class.Splatoon.Shooters import *;from wpn_class.Splatoon.Sloshers import * #One
from wpn_class.Splatoon.Splatlings import * #Classes

def splat1():
    print("*****Splatoon 1*****")
    print("  ***Chose a Class***  ")
    print("(1)Shooters\n(2)Rollers\n(3)Chargers\n(4)Sloshers\n(5)Splatlings\n(6)Blasters\n(7)Brushes") #Splatoon 1 Classes
    wpnclass = input()
    match wpnclass:
        case "1":
            Shooters_1()
        case "2":
            Rollers_1()
        case "3":
            Chargers_1()
        case "4":
            Sloshers_1()
        case "5":
            Splatlings_1()
        case "6":
            Blasters_1()
        case "7":
            Brushes_1()
        case _:
            print("There is no weapon class here")
            time.sleep(2)
            splat1()