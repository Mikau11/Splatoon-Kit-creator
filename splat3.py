import time

from wpn_class.Splatoon.Blasters import *;from wpn_class.Splatoon.Brushes import *;from wpn_class.Splatoon.Chargers import * #Splatoon
from wpn_class.Splatoon.Rollers import *;from wpn_class.Splatoon.Shooters import *;from wpn_class.Splatoon.Sloshers import * #One
from wpn_class.Splatoon.Splatlings import * #Classes

from wpn_class.Splatoon2.Brellas import *;from wpn_class.Splatoon2.Dualies import * #Splatoon 2 Classes

from wpn_class.Splatoon3.Splatanas import *;from wpn_class.Splatoon3.Stringers import * #Splatoon 3 Classes


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
            Rollers_3()
        case "3":
            Chargers_3()
        case "4":
            Sloshers_3()
        case "5":
            Splatlings_3()
        case "6":
            Blasters_3()
        case "7":
            Brushes_3()
        case "8":
            Dualies_3()
        case "9":
            Brellas_3()
        case "10":
            Stringers_3()
        case "11":
            Splatanas_3()
        case _:
            print("There is no weapon class here")
            time.sleep(2)
            splat3()