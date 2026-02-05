import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Splatlings_1():
    print("Splatling")

def Splatlings_2():
    print("Splatling")

def Splatlings_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Chargers name to be?")
            wpn_range = input("What do you want your Chargers range to be?")
            wpn_crgspd = input("What you want your Chargers charge speed to be?")
            wpn_mob = input("What do you want your Chargers mobilty to be?")
        case "2":
            print("***What type?***")
            print("(1)Mini\n(2)Heavy\n(3)Hydra\n(4)Ballpoint\n(5)Nautilus\n(6)Heavy Edit")
            type = input()
            match type:
                case "1":
                    wpn_tpe = "Mini Splatling"
                    wpn_range = 62
                    wpn_crgspd = 80
                    wpn_mob = 90
                case "2":
                    wpn_tpe = "Heavy splatling"
                    wpn_range = 78
                    wpn_crgspd = 38
                    wpn_mob = 55
                case "3":
                    wpn_tpe = "Hydra splatling"
                    wpn_range = 85
                    wpn_crgspd = 10
                    wpn_mob = 20
                case "4":
                    wpn_tpe = "Ballpoint splatling"
                    wpn_range = 84
                    wpn_crgspd = 18
                    wpn_mob = 60
                case "5":
                    wpn_tpe = "Nautilus"
                    wpn_range = 74
                    wpn_crgspd = 37
                    wpn_mob = 70
                case "6":
                    wpn_tpe = "Heavy Edit splatling"
                    wpn_range = 70
                    wpn_crgspd = 14
                    wpn_mob = 90
                case _:
                    print("Theres no Type here")
                    Splatlings_3()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Splatlings_3()
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Charge Speed:", wpn_crgspd)
    print("Mobilty:", wpn_mob)
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
            file = open(f"Splatlings/{wpn_name}.txt", "w")
            file.close()
            with open(f"Splatlings/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Charge speed:", str(wpn_crgspd), "\n", "Mobility:", str(wpn_mob), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Splatlings/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)
    