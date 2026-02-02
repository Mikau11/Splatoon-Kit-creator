import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

from_game = "splat1"

def Sloshers_1():
    print("Slosher")

def Sloshers_2():
    pass

def Sloshers_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Sloshers name to be?")
            wpn_range = input("What do you want your Sloshers range to be?")
            wpn_dmg = input("What you want your Sloshers damage to be?")
            wpn_hdl = input("What do you want your Sloshers handling to be?")
        case "2":
            print("***What type?***")
            print("(1)Slosher\n(2)Tri\n(3)Machine\n(4)Bloblobber\n(5)Explsosher\n(6)Dread Wringer")
            type = input()
            match type:
                case "1":
                    wpn_name = input("What do you want your Slosher to be called?")
                    wpn_range = 58
                    wpn_dmg = 85
                    wpn_hdl = 50
                case "2":
                    wpn_name = input("What do you want your Tri-Slosher to be called?")
                    wpn_range = 31
                    wpn_dmg = 75
                    wpn_hdl = 70
                case "3":
                    wpn_name = input("What do you want your Sloshing machine to be called?")
                    wpn_range = 60
                    wpn_dmg = 90
                    wpn_hdl = 40
                case "4":
                    wpn_name = input("What do you want your Bloblobber to be called?")
                    wpn_range = 86
                    wpn_dmg = 29
                    wpn_hdl = 50
                case "5":
                    wpn_name = input("What do you want your Explosher to be called?")
                    wpn_range = 77
                    wpn_dmg = 65
                    wpn_hdl = 20
                case "6":
                    wpn_name = input("What do you want your Dread Wringer to be called?")
                    wpn_range = 60
                    wpn_dmg = 55
                    wpn_hdl = 35
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Damage:", wpn_dmg)
    print("Handling:", wpn_hdl)
    print("Brand:", brand_class.brands.wpn_brand)
    print("Sub:", subs_and_specials_class.subs.wpn_sub)
    print("Special:", subs_and_specials_class.specials.wpn_special)