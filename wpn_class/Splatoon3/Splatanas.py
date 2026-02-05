import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Splatanas_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Splatanas name to be?")
            wpn_range = input("What do you want your Splatanas range to be?")
            wpn_dmg = input("What you want your Splatanas damage to be?")
            wpn_hdl = input("What do you want your Splatanas handling to be?")
        case "2":
            print("***What type?***")
            print("(1)Stamper\n(2)Wiper\n(3)Decavitator")
            type = input()
            match type:
                case "1":
                    wpn_tpe = "Splatana Stamper"
                    wpn_range = 75
                    wpn_dmg = 43
                    wpn_hdl = 60
                case "2":
                    wpn_tpe = "Splatana Wiper"
                    wpn_range = 58
                    wpn_dmg = 29
                    wpn_hdl = 75
                case "3":
                    wpn_tpe = "Decavitator"
                    wpn_range = 63
                    wpn_dmg = 57
                    wpn_hdl = 45
                case _:
                    print("Theres no Type here")
                    Splatanas_3()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Splatanas_3()
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
            file = open(f"Splatanas/{wpn_name}.txt", "w")
            file.close()
            with open(f"Splatanas/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Damage:", str(wpn_dmg), "\n", "Handling:", str(wpn_hdl), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Splatanas/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)