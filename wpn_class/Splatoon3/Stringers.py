import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Stringers_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Stringers name to be?")
            wpn_range = input("What do you want your Stringers range to be?")
            wpn_crgspd = input("What you want your Stringers charge speed to be?")
            wpn_mob = input("What do you want your Stringers mobilty to be?")
        case "2":
            print("***What type?***")
            print("(1)Tri\n(2)REEF-LUX\n(3)Wellstring")
            type = input()
            match type:
                case "1":
                    wpn_tpe = "Tri-Stringer"
                    wpn_range = 88
                    wpn_crgspd = 40
                    wpn_mob = 40
                case "2":
                    wpn_tpe = "REEF-LUX"
                    wpn_range = 60
                    wpn_crgspd = 75
                    wpn_mob = 60
                case "3":
                    wpn_tpe = "Wellstring"
                    wpn_range = 83
                    wpn_crgspd = 33
                    wpn_mob = 30
                case _:
                    print("Theres no Type here")
                    Stringers_3()
            print("What do you want your", wpn_tpe, "to be called?")
            wpn_name = input()
        case _:
            print("Nuttin' 'ere")
            Stringers_3()
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
            file = open(f"Stringers/{wpn_name}.txt", "w")
            file.close()
            with open(f"Stringers/{wpn_name}.txt", "r") as weapon_file:
                stats = weapon_file.readlines()
            stats = "Name:", wpn_name, "\n", "Range:", str(wpn_range), "\n", "Charge speed:", str(wpn_crgspd), "\n", "Mobility:", str(wpn_mob), "\n", "Type:", wpn_tpe, "\n","Brand:", brand_class.brands.wpn_brand, "\n", "Sub:", subs_and_specials_class.subs.wpn_sub, "\n", "Special:", subs_and_specials_class.specials.wpn_special, "\n"
            with open(f"Stringers/{wpn_name}.txt", "w") as weapon_file:
                weapon_file.writelines(stats)
    