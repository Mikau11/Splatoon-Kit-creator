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
                    wpn_tpe = "Slosher"
                    wpn_range = 58
                    wpn_dmg = 85
                    wpn_hdl = 50
                case "2":
                    wpn_tpe = "Tri-Slosher"
                    wpn_range = 31
                    wpn_dmg = 75
                    wpn_hdl = 70
                case "3":
                    wpn_tpe = "Sloshing machine"
                    wpn_range = 60
                    wpn_dmg = 90
                    wpn_hdl = 40
                case "4":
                    wpn_tpe = "Bloblobber"
                    wpn_range = 86
                    wpn_dmg = 29
                    wpn_hdl = 50
                case "5":
                    wpn_tpe = "Explosher"
                    wpn_range = 77
                    wpn_dmg = 65
                    wpn_hdl = 20
                case "6":
                    wpn_tpe = "Dread Wringer"
                    wpn_range = 60
                    wpn_dmg = 55
                    wpn_hdl = 35
                case _:
                    print("Theres no Type here")
                    Sloshers_3()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Sloshers_3()
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Damage:", wpn_dmg)
    print("Handling:", wpn_hdl)
    print("Type:", wpn_tpe)
    print("Brand:", brand_class.brands.wpn_brand)
    print("Sub:", subs_and_specials_class.subs.wpn_sub)
    print("Special:", subs_and_specials_class.specials.wpn_special)
    print("Would ypu like to save the file?(Y/N)")
    print("Warning: this will override ANY contents in a file if that file already exists, so keep names unqiue")
    type = input()
    filenum = 1
    match type:
        case "Y":
            file = open(f"Sloshers/{wpn_name}.txt", "w")
            file.close()
            with open(f"Sloshers/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Damage:", str(wpn_dmg), "\n", "Handling:", str(wpn_hdl), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Sloshers/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)