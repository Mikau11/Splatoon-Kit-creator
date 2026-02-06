import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Dualies_2():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Dualies name to be?")
            wpn_range = input("What do you want your Dualies range to be?")
            wpn_dmg = input("What you want your Dualies damage to be?")
            wpn_mob = input("What do you want your Dualies handling to be?")
        case "2":
            print("***What type?***")
            print("(1)Splat\n(2)Dapple\n(3)Glooga\n(4)Squelchers\n(5)Tetra")
            type = input()
            match type:
                case "1":
                    wpn_tpe = "Splat Dualies"
                    wpn_range = 50
                    wpn_dmg = 29
                    wpn_mob = 60
                case "2":
                    wpn_tpe = "Dapple Dualies"
                    wpn_range = 24
                    wpn_dmg = 47
                    wpn_mob = 80
                case "3":
                    wpn_tpe = "Glooga Dualies"
                    wpn_range = 66
                    wpn_dmg = 75
                    wpn_mob = 35
                case "4":
                    wpn_tpe = "Dualie Squelchers"
                    wpn_range = 70
                    wpn_dmg = 22
                    wpn_mob = 70
                case "5":
                    wpn_tpe = "Tetra Dualies"
                    wpn_range = 58
                    wpn_dmg = 22
                    wpn_mob = 90
                case _:
                    print("Theres no Type here")
                    Dualies_2()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Dualies_2()
    brand_class.brands.brands_2()
    subs_and_specials_class.subs.subs_2()
    subs_and_specials_class.specials.specials_2()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Damage:", wpn_dmg)
    print("Mobility:", wpn_mob)
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
            file = open(f"Dualies/{wpn_name}.txt", "w")
            file.close()
            with open(f"Dualies/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Damage:", str(wpn_dmg), "\n", "Mobility:", str(wpn_mob), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Dualies/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)

def Dualies_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Dualies name to be?")
            wpn_range = input("What do you want your Dualies range to be?")
            wpn_dmg = input("What you want your Dualies damage to be?")
            wpn_mob = input("What do you want your Dualies handling to be?")
        case "2":
            print("***What type?***")
            print("(1)Splat\n(2)Dapple\n(3)Glooga\n(4)Squelchers\n(5)Tetra\n(6)Douser")
            type = input()
            match type:
                case "1":
                    wpn_tpe = "Splat Dualies"
                    wpn_range = 50
                    wpn_dmg = 29
                    wpn_mob = 60
                case "2":
                    wpn_tpe = "Dapple Dualies"
                    wpn_range = 24
                    wpn_dmg = 47
                    wpn_mob = 80
                case "3":
                    wpn_tpe = "Glooga Dualies"
                    wpn_range = 66
                    wpn_dmg = 75
                    wpn_mob = 35
                case "4":
                    wpn_tpe = "Dualie Squelchers"
                    wpn_range = 70
                    wpn_dmg = 22
                    wpn_mob = 70
                case "5":
                    wpn_tpe = "Tetra Dualies"
                    wpn_range = 58
                    wpn_dmg = 22
                    wpn_mob = 90
                case "6":
                    wpn_tpe = "Douser Dualies"
                    wpn_range = 78
                    wpn_dmg = 20
                    wpn_mob = 25
                case _:
                    print("Theres no Type here")
                    Dualies_3()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Dualies_3()
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Damage:", wpn_dmg)
    print("Mobility:", wpn_mob)
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
            file = open(f"Dualies/{wpn_name}.txt", "w")
            file.close()
            with open(f"Dualies/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Damage:", str(wpn_dmg), "\n", "Mobility:", str(wpn_mob), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Dualies/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)