import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Brellas_2():
    print("Brella")

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
                    wpn_name = input("What do you want your Splat Brella to be called?")
                    wpn_range = 43
                    wpn_dmg = 65
                    wpn_dur = 60
                case "2":
                    wpn_name = input("What do you want your Tenta Brella to be called?")
                    wpn_range = 62
                    wpn_dmg = 85
                    wpn_dur = 85
                case "3":
                    wpn_name = input("What do you want your Undercover Brella to be called?")
                    wpn_range = 50
                    wpn_dmg = 30
                    wpn_dur = 25
                case "4":
                    wpn_name = input("What do you want your Recycled Brella to be called?")
                    wpn_range = 56
                    wpn_dmg = 75
                    wpn_dur = 19
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Damage:", wpn_dmg)
    print("Durabilty:", wpn_dur)
    print("Brand:", brand_class.brands.wpn_brand)
    print("Sub:", subs_and_specials_class.subs.wpn_sub)
    print("Special:", subs_and_specials_class.specials.wpn_special)