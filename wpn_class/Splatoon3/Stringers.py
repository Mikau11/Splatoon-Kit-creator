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
                    wpn_name = input("What do you want your Tri-Stringer to be called?")
                    wpn_range = 88
                    wpn_crgspd = 40
                    wpn_mob = 40
                case "2":
                    wpn_name = input("What do you want your REEF-LUX to be called?")
                    wpn_range = 60
                    wpn_crgspd = 75
                    wpn_mob = 60
                case "3":
                    wpn_name = input("What do you want your Wellstring to be called?")
                    wpn_range = 83
                    wpn_crgspd = 33
                    wpn_mob = 30
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Charge Speed:", wpn_crgspd)
    print("Mobilty:", wpn_mob)
    print("Brand:", brand_class.brands.wpn_brand)
    print("Sub:", subs_and_specials_class.subs.wpn_sub)
    print("Special:", subs_and_specials_class.specials.wpn_special)
    
    