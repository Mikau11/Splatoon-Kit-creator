import time

from wpn_class.Splatoon.Blasters import Blasters;from wpn_class.Splatoon.Brushes import Brushes;from wpn_class.Splatoon.Chargers import Chargers #Splatoon
from wpn_class.Splatoon.Rollers import Rollers;from wpn_class.Splatoon.Shooters import *;from wpn_class.Splatoon.Sloshers import Sloshers #One
from wpn_class.Splatoon.Splatlings import Splatlings #Classes

from wpn_class.Splatoon2.Brellas import Brellas;from wpn_class.Splatoon2.Dualies import Dualies #Splatoon 2 Classes

from wpn_class.Splatoon3.Splatanas import Splatanas;from wpn_class.Splatoon3.Stringers import Stringers #Splatoon 3 Classes


def splat3():
    print("*****Splatoon 3*****")
    print("  ***Chose a Class***  ")
    print("(1)Shooters\n(2)Rollers\n(3)Chargers\n(4)Sloshers\n(5)Splatlings\n(6)Blasters\n(7)Brushes") #Splatoon 1 Classes
    print("(8)Dualies\n(9)Brellas") #Splatoon 2 Classes
    print("(10)Stringers\n(11)Splatanas") #Splatoon 3 Classes
    wpnclass = input()
    match wpnclass:
        case "1":
            Shooters_3()
        case "2":
            Rollers()
        case "3":
            Chargers()
        case "4":
            Sloshers()
        case "5":
            Splatlings()
        case "6":
            Blasters()
        case "7":
            Brushes()
        case "8":
            Dualies()
        case "9":
            Brellas()
        case "10":
            Stringers()
        case "11":
            Splatanas()
        case _:
            print("There is no weapon class here")
            time.sleep(2)
            splat3()