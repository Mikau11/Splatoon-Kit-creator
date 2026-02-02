import sys
sys.path.append('../wpn_class')

import wpn_class.brand_hdl as brand_class
import wpn_class.subs_specials_hdl as subs_and_specials_class

def Rollers_1():
    print("Roller")

def Rollers_2():
    pass

def Rollers_3():
    print("***First, do you wanna create a kit for a new weapon type, or a kit for a preexisting weapon type?***")
    print("(1)New Type\n(2)Preexisting type")
    type = input()
    match type:
        case "1":
            wpn_name = input("What do you want you Rollers name to be?")
            wpn_range = input("What do you want your Rollers range to be?")
            wpn_ikspd = input("What you want your Rollers Ink speed to be?")
            wpn_hdl = input("What do you want your Rollers handling to be?")
        case "2":
            print("***What type?***")
            print("(1)Carbon\n(2)Splat\n(3)Dynamo\n(4)Flingza\n(5)Big swing")
            type = input()
            match type:
                case "1":
                    wpn_name = input("What do you want your Carbon to be called?")
                    wpn_range = 20
                    wpn_ikspd = 63
                    wpn_hdl = 65
                case "2":
                    wpn_name = input("What do you want your Splat roller to be called?")
                    wpn_range = 48
                    wpn_ikspd = 45
                    wpn_hdl = 55
                case "3":
                    wpn_name = input("What do you want your Dynamo to be called?")
                    wpn_range = 76
                    wpn_ikspd = 25
                    wpn_hdl = 20
                case "4":
                    wpn_name = input("What do you want your Flingza to be called?")
                    wpn_range = 58
                    wpn_ikspd = 45
                    wpn_hdl = 45
                case "5":
                    wpn_name = input("What do you want your Big swing to be called?")
                    wpn_range = 56
                    wpn_ikspd = 54
                    wpn_hdl = 60
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Ink speed:", wpn_ikspd)
    print("Handling:", wpn_hdl)
    print("Brand:", brand_class.brands.wpn_brand)
    print("Sub:", subs_and_specials_class.subs.wpn_sub)
    print("Special:", subs_and_specials_class.specials.wpn_special)