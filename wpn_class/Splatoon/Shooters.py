import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Shooters_1():
    print("Stay Fresh!")

def Shooters_2():
    print("Off the Hook!")

def Shooters_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Shooters name to be?")
            wpn_range = input("What do you want your Shooters range to be?")
            wpn_dmg = input("What you want your Shooters damage to be?")
            wpn_fr = input("What do you want your Shooters fire rate to be?")
        case "2":
            print("***What type?***")
            print("(1)Sploosh\n(2)Jr\n(3)Splash\n(4)Aerospray\n(5)Splattershot\n(6).52 Gal\n(7).96 Gal\n(8)Shot pro\n(9)Shot nova\n(10)N-zap")
            print("(11)Squelcher\n(12)L3\n(13)H3\n(14)Squeezer")
            type = input()
            match type:
                case "1":
                    wpn_tpe = "Sploosh"
                    wpn_range = 5
                    wpn_dmg = 52
                    wpn_fr = 75
                case "2":
                    wpn_tpe = "Splattershot jr"
                    wpn_range = 36
                    wpn_dmg = 22
                    wpn_fr = 75
                case "3":
                    wpn_tpe = "Splash"
                    wpn_range = 43
                    wpn_dmg = 22
                    wpn_fr = 75
                case "4":
                    wpn_tpe = "Aerospray"
                    wpn_range = 36
                    wpn_dmg = 10
                    wpn_fr = 90
                case "5":
                    wpn_tpe = "Splattershot"
                    wpn_range = 52
                    wpn_dmg = 47
                    wpn_fr = 60
                case "6":
                    wpn_tpe = ".52"
                    wpn_range = 55
                    wpn_dmg = 75
                    wpn_fr = 25
                case "7":
                    wpn_tpe = ".96"
                    wpn_range = 74
                    wpn_dmg = 80
                    wpn_fr = 10
                case "8":
                    wpn_tpe = "Splattershot pro"
                    wpn_range = 70
                    wpn_dmg = 64
                    wpn_fr = 30
                case "9":
                    wpn_tpe = "Splattershot nova"
                    wpn_range = 68
                    wpn_dmg = 10
                    wpn_fr = 60
                case "10":
                    wpn_tpe = "N-zap"
                    wpn_range = 50
                    wpn_dmg = 29
                    wpn_fr = 75
                case "11":
                    wpn_tpe = "Squelcher"
                    wpn_range = 82
                    wpn_dmg = 36
                    wpn_fr = 30
                case "12":
                    wpn_tpe = "L3"
                    wpn_range = 62
                    wpn_dmg = 30
                    wpn_fr = 65
                case "13":
                    wpn_tpe = "H3"
                    wpn_range = 70
                    wpn_dmg = 64
                    wpn_fr = 30
                case "14":
                    wpn_tpe = "Squeezer"
                    wpn_range = 77
                    wpn_dmg = 52
                    wpn_fr = 30
                case _:
                    print("Theres no Type here")
                    Shooters_3()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Shooters_3()
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Damage:", wpn_dmg)
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
            file = open(f"Shooters/{wpn_name}.txt", "w")
            file.close()
            with open(f"Shooters/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Damage:", str(wpn_dmg), "\n", "Fire rate:", str(wpn_fr), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Shooters/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)
