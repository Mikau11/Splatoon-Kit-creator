import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Blasters_1():
    print("Blaster")

def Blasters_2():
    pass

def Blasters_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Blasters name to be?")
            wpn_range = input("What do you want your Blasters range to be?")
            wpn_imp = input("What you want your Blasters impact to be?")
            wpn_fr = input("What do you want your Blasters fire rate to be?")
        case "2":
            print("***What type?***")
            print("(1)Luna\n(2)Blaster\n(3)Range Blaster\n(4)Clash\n(5)Rapid\n(6)Rapid pro\n(7)S-BLAST")
            type = input()
            match type:
                case "1":
                    wpn_tpe = "Luna Blaster"
                    wpn_range = 18
                    wpn_imp = 70
                    wpn_fr = 30
                case "2":
                    wpn_tpe = "Blaster"
                    wpn_range = 27
                    wpn_imp = 70
                    wpn_fr = 20
                case "3":
                    wpn_tpe = "Range Blaster"
                    wpn_range = 56
                    wpn_imp = 70
                    wpn_fr = 10
                case "4":
                    wpn_tpe = "Clash Blaster"
                    wpn_range = 21
                    wpn_imp = 30
                    wpn_fr = 65
                case "5":
                    wpn_tpe = "Rapid Blaster"
                    wpn_range = 62
                    wpn_imp = 35
                    wpn_fr = 40
                case "6":
                    wpn_tpe = "Rapid Blaster Pro"
                    wpn_range = 72
                    wpn_imp = 35
                    wpn_fr = 30
                case "7":
                    wpn_tpe = "S-BLAST"
                    wpn_range = 45
                    wpn_imp = 70
                    wpn_fr = 15
                case _:
                    print("Theres no Type here")
                    Blasters_3()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Blasters_3()
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Impact:", wpn_imp)
    print("Fire rate:", wpn_fr)
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
            file = open(f"Blasters/{wpn_name}.txt", "w")
            file.close()
            with open(f"Blasters/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Impact:", str(wpn_imp), "\n", "Fire rate:", str(wpn_fr), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Blasters/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)
    