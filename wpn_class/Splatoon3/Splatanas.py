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
                    wpn_name = input("What do you want your Splatana Stamper to be called?")
                    wpn_range = 75
                    wpn_dmg = 43
                    wpn_hdl = 60
                case "2":
                    wpn_name = input("What do you want your Splatana Wiper to be called?")
                    wpn_range = 58
                    wpn_dmg = 29
                    wpn_hdl = 75
                case "3":
                    wpn_name = input("What do you want your Decavitator to be called?")
                    wpn_range = 63
                    wpn_dmg = 57
                    wpn_hdl = 45
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Damage:", wpn_dmg)
    print("Handling:", wpn_hdl)
    print("Brand:", brand_class.brands.wpn_brand)
    print("Sub:", subs_and_specials_class.subs.wpn_sub)
    print("Special:", subs_and_specials_class.specials.wpn_special)
