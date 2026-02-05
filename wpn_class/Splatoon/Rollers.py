import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Rollers_1():
    print("Roller")

def Rollers_2():
    pass

def Rollers_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Rollers name to be?")
            wpn_range = input("What do you want your Rollers range to be?")
            wpn_ikspd = input("What you want your Rollers Ink speed to be?")
            wpn_hdl = input("What do you want your Rollers handling to be?")
        case "2":
            print("***What type?***")
            print("(1)Carbon\n(2)Splat\n(3)Dynamo\n(4)Flingza\n(5)Big swing")
            type = input()
            match type:
                case "1":
                    wpn_tpe = "Carbon"
                    wpn_range = 20
                    wpn_ikspd = 63
                    wpn_hdl = 65
                case "2":
                    wpn_tpe = "Splat roller"
                    wpn_range = 48
                    wpn_ikspd = 45
                    wpn_hdl = 55
                case "3":
                    wpn_tpe = "Dynamo"
                    wpn_range = 76
                    wpn_ikspd = 25
                    wpn_hdl = 20
                case "4":
                    wpn_tpe = "Flingza"
                    wpn_range = 58
                    wpn_ikspd = 45
                    wpn_hdl = 45
                case "5":
                    wpn_tpe = "Big swing"
                    wpn_range = 56
                    wpn_ikspd = 54
                    wpn_hdl = 60
                case _:
                    print("Theres no Type here")
                    Rollers_3()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Rollers_3()
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Ink speed:", wpn_ikspd)
    print("Handling:", wpn_hdl)
    print("Brand:", brand_class.brands.wpn_brand)
    print("Sub:", subs_and_specials_class.subs.wpn_sub)
    print("Special:", subs_and_specials_class.specials.wpn_special)
    print("Would ypu like to save the file?(Y/N)")
    print("Warning: this will override ANY contents in a file if that file already exists, so keep names unqiue")
    type = input()
    filenum = 1
    match type:
        case "Y":
            file = open(f"Rollers/{wpn_name}.txt", "w")
            file.close()
            with open(f"Rollers/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Ink speed:", str(wpn_ikspd), "\n", "Handling:", str(wpn_hdl), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Rollers/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)