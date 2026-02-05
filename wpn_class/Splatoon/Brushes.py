import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Brushes_1():
    print("Brushe")

def Brushes_2():
    pass

def Brushes_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Brushes name to be?")
            wpn_range = input("What do you want your Brushes range to be?")
            wpn_ikspd = input("What you want your Bruhses Ink speed to be?")
            wpn_hdl = input("What do you want your Brushes handling to be?")
        case "2":
            print("***What type?***")
            print("(1)Ink\n(2)Octo\n(3)Paint")
            type = input()
            match type:
                case "1":
                    wpn_tpe = "Inkbrush"
                    wpn_range = 5
                    wpn_ikspd = 100
                    wpn_hdl = 100
                case "2":
                    wpn_tpe = "Octobrush"
                    wpn_range = 23
                    wpn_ikspd = 80
                    wpn_hdl = 85
                case "3":
                    wpn_tpe = "Paintrush"
                    wpn_range = 33
                    wpn_ikspd = 85
                    wpn_hdl = 60
                case _:
                    print("Theres no Type here")
                    Brushes_3()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Brushes_3()
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Ink speed:", wpn_ikspd)
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
            file = open(f"Brushes/{wpn_name}.txt", "w")
            file.close()
            with open(f"Brushes/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Ink speed:", str(wpn_ikspd), "\n", "Handling:", str(wpn_hdl), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Brushes/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)
    