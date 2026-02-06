import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Brellas_2():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Brellas name to be?")
            wpn_range = input("What do you want your Brellas range to be?")
            wpn_dmg = input("What you want your Brellas to be?")
            wpn_dur = input("What do you want your Brellas handling to be?")
        case "2":
            print("***What type?***")
            print("(1)Splat\n(2)Tenta\n(3)Undercover")
            type = input()
            match type:
                case "1":
                    wpn_tpe = "Splat Brella"
                    wpn_range = 43
                    wpn_dmg = 65
                    wpn_dur = 60
                case "2":
                    wpn_tpe = "Tenta Brella"
                    wpn_range = 62
                    wpn_dmg = 85
                    wpn_dur = 85
                case "3":
                    wpn_tpe = "Undercover Brella"
                    wpn_range = 50
                    wpn_dmg = 30
                    wpn_dur = 25
                case _:
                    print("Theres no Type here")
                    Brellas_2()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Brellas_2()
    brand_class.brands.brands_2()
    subs_and_specials_class.subs.subs_2()
    subs_and_specials_class.specials.specials_2()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Damage:", wpn_dmg)
    print("Durabilty:", wpn_dur)
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
            file = open(f"Brellas/{wpn_name}.txt", "w")
            file.close()
            with open(f"Brellas/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Damage:", str(wpn_dmg), "\n", "Durability:", str(wpn_dur), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Brellas/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)

def Brellas_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Brellas name to be?")
            wpn_range = input("What do you want your Brellas range to be?")
            wpn_dmg = input("What you want your Brellas to be?")
            wpn_dur = input("What do you want your Brellas handling to be?")
        case "2":
            print("***What type?***")
            print("(1)Splat\n(2)Tenta\n(3)Undercover\n(4)Recycled")
            type = input()
            match type:
                case "1":
                    wpn_tpe = "Splat Brella"
                    wpn_range = 43
                    wpn_dmg = 65
                    wpn_dur = 60
                case "2":
                    wpn_tpe = "Tenta Brella"
                    wpn_range = 62
                    wpn_dmg = 85
                    wpn_dur = 85
                case "3":
                    wpn_tpe = "Undercover Brella"
                    wpn_range = 50
                    wpn_dmg = 30
                    wpn_dur = 25
                case "4":
                    wpn_tpe = "Recycled Brella"#
                    wpn_range = 56
                    wpn_dmg = 75
                    wpn_dur = 19
                case _:
                    print("Theres no Type here")
                    Brellas_3()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Brellas_3()
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Damage:", wpn_dmg)
    print("Durabilty:", wpn_dur)
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
            file = open(f"Brellas/{wpn_name}.txt", "w")
            file.close()
            with open(f"Brellas/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Damage:", str(wpn_dmg), "\n", "Durability:", str(wpn_dur), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Brellas/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)