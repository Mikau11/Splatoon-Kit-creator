import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Chargers_1():
    print("Charger")

def Chargers_2():
    pass

def Chargers_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Chargers name to be?")
            wpn_range = input("What do you want your Chargers range to be?")
            wpn_crgspd = input("What you want your Chargers charge speed to be?")
            wpn_mob = input("What do you want your Chargers mobilty to be?")
        case "2":
            print("***What type?***")
            print("(1)Squiffer\n(2)Splat\n(3)SplatScope\n(4)E-Liter(4K)\n(5)E-literScope(4K)\n(6)Bamboozler\n(7)GooTuber\n(8)Snipewriter")
            type = input()
            match type:
                case "1":
                    wpn_name = input("What do you want your Squiffer to be called?")
                    wpn_range = 75
                    wpn_crgspd = 70
                    wpn_mob = 60
                case "2":
                    wpn_name = input("What do you want your Splat Charger to be called?")
                    wpn_range = 88
                    wpn_crgspd = 50
                    wpn_mob = 40
                case "3":
                    wpn_name = input("What do you want your Splatscope to be called?")
                    wpn_range = 91
                    wpn_crgspd = 50
                    wpn_mob = 30
                case "4":
                    wpn_name = input("What do you want your E-liter to be called?")
                    wpn_range = 96
                    wpn_crgspd = 20
                    wpn_mob = 15
                case "5":
                    wpn_name = input("What do you want your E-literscope to be called?")
                    wpn_range = 100
                    wpn_crgspd = 20
                    wpn_mob = 5
                case "6":
                    wpn_name = input("What do you want your Bamboozler to be called?")
                    wpn_range = 78
                    wpn_crgspd = 90
                    wpn_mob = 80
                case "7":
                    wpn_name = input("What do you want your GooTuber to be called?")
                    wpn_range = 78
                    wpn_crgspd = 38
                    wpn_mob = 70
                case "8":
                    wpn_name = input("What do you want your Snipewriter to be called?")
                    wpn_range = 91
                    wpn_crgspd = 43
                    wpn_mob = 80
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
    