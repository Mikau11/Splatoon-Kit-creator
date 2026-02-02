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
                    wpn_name = input("What do you want your Sploosh to be called?")
                    wpn_range = 5
                    wpn_dmg = 52
                    wpn_fr = 75
                case "2":
                    wpn_name = input("What do you want your Splattershot jr to be called?")
                    wpn_range = 36
                    wpn_dmg = 22
                    wpn_fr = 75
                case "3":
                    wpn_name = input("What do you want your Splash to be called?")
                    wpn_range = 43
                    wpn_dmg = 22
                    wpn_fr = 75
                case "4":
                    wpn_name = input("What do you want your Aerospray to be called?")
                    wpn_range = 36
                    wpn_dmg = 10
                    wpn_fr = 90
                case "5":
                    wpn_name = input("What do you want your Splattershot to be called?")
                    wpn_range = 52
                    wpn_dmg = 47
                    wpn_fr = 60
                case "6":
                    wpn_name = input("What do you want your .52 to be called?")
                    wpn_range = 55
                    wpn_dmg = 75
                    wpn_fr = 25
                case "7":
                    wpn_name = input("What do you want your .96 to be called?")
                    wpn_range = 74
                    wpn_dmg = 80
                    wpn_fr = 10
                case "8":
                    wpn_name = input("What do you want your Splattershot pro to be called?")
                    wpn_range = 70
                    wpn_dmg = 64
                    wpn_fr = 30
                case "9":
                    wpn_name = input("What do you want your Splattershot nova to be called?")
                    wpn_range = 68
                    wpn_dmg = 10
                    wpn_fr = 60
                case "10":
                    wpn_name = input("What do you want your N-zap to be called?")
                    wpn_range = 50
                    wpn_dmg = 29
                    wpn_fr = 75
                case "11":
                    wpn_name = input("What do you want your Squelcher to be called?")
                    wpn_range = 82
                    wpn_dmg = 36
                    wpn_fr = 30
                case "12":
                    wpn_name = input("What do you want your L3 to be called?")
                    wpn_range = 62
                    wpn_dmg = 30
                    wpn_fr = 65
                case "13":
                    wpn_name = input("What do you want your H3 to be called?")
                    wpn_range = 70
                    wpn_dmg = 64
                    wpn_fr = 30
                case "14":
                    wpn_name = input("What do you want your Squeezer to be called?")
                    wpn_range = 77
                    wpn_dmg = 52
                    wpn_fr = 30
    brand_class.brands.brands_3()
    subs_and_specials_class.subs.subs_3()
    subs_and_specials_class.specials.specials_3()
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Damage:", wpn_dmg)
    print("Fire rate:", wpn_fr)
    print("Brand:", brand_class.brands.wpn_brand)
    print("Sub:", subs_and_specials_class.subs.wpn_sub)
    print("Special:", subs_and_specials_class.specials.wpn_special)
