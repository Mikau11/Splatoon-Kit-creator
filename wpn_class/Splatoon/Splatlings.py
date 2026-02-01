from_game = "splat1"

def Splatlings_1():
    print("Splatling")

def Splatlings_2():
    print("Splatling")

def Splatlings_3():
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
            print("(1)Mini\n(2)Heavy\n(3)Hydra\n(4)Ballpoint\n(5)Nautilus\n(6)Heavy Edit")
            type = input()
            match type:
                case "1":
                    wpn_name = input("What do you want your Mini Splatling to be called?")
                    wpn_range = 62
                    wpn_crgspd = 80
                    wpn_mob = 90
                case "2":
                    wpn_name = input("What do you want your Heavy splatling to be called?")
                    wpn_range = 78
                    wpn_crgspd = 38
                    wpn_mob = 55
                case "3":
                    wpn_name = input("What do you want your Hydra splatling to be called?")
                    wpn_range = 85
                    wpn_crgspd = 10
                    wpn_mob = 20
                case "4":
                    wpn_name = input("What do you want your Ballpoint splatling to be called?")
                    wpn_range = 84
                    wpn_crgspd = 18
                    wpn_mob = 60
                case "5":
                    wpn_name = input("What do you want your Nautilus to be called?")
                    wpn_range = 74
                    wpn_crgspd = 37
                    wpn_mob = 70
                case "6":
                    wpn_name = input("What do you want your Heavy Edit splatling to be called?")
                    wpn_range = 70
                    wpn_crgspd = 14
                    wpn_mob = 90
    wpn_brand = input("What do you want the brand to be?(type none if no brand)")
    print("What do you want the sub to be?")
    print("(1)Splat\n(2)Suction\n(3)Burst\n(4)Curling\n(5)Auto\n(6)Ink Mine\n(7)Toxic mist\n(8)Point sensor\n(9)Splash wall\n(10)Sprinkler")
    print("(11)Beakon\n(12)Fizzy\n(13)Torpedo\n(14)Angle shooter")
    type = input()
    match type:
        case "1":
            wpn_sub = "Splat bomb"
        case "2":
            wpn_sub = "Suction bomb"
        case "3":
            wpn_sub = "Burst bomb"
        case "4":
            wpn_sub = "Curlinb bomb"
        case "5":
            wpn_sub = "Auto bomb"
        case "6":
            wpn_sub = "Ink mine"
        case "7":
            wpn_sub = "Toxic mist"
        case "8":
            wpn_sub = "Point sensor"
        case "9":
            wpn_sub = "Splash wall"
        case "10":
            wpn_sub = "Sprinkler"
        case "11":
            wpn_sub = "Squid Beakon"
        case "12":
            wpn_sub = "Fizzy bomb"
        case "13":
            wpn_sub = "Torpedo"
        case "14":
            wpn_sub = "Angle shooter"
    print("What do you want the special to be?")
    print("(1)Big Bubbler\n(2)Booyah bomb\n(3)Crab tank\n(4)Ink storm\n(5)Ink vac\n(6)Inkjet\n(7)Killer wail 5.1\n(8)Kraken royale\n(9)Reefslider")
    print("(10)Splatcolour screen\n(11)Super chump\n(12)Tacticooler\n(13)Tenta missiles\n(14)Triple Inkstike\n(15)Trizooka\n(16)Ultra stamp")
    print("(17)Wave breaker\n(18)Zipcaster\n(19)Triple splashdown")
    type = input()
    match type:
            case "1":
                wpn_special = "Big bubbler"
            case "2":
                wpn_special = "Booyah bomb"
            case "3":
                wpn_special = "Crab tank"
            case "4":
                wpn_special = "Ink storm"
            case "5":
                wpn_special = "Ink vac"
            case "6":
                wpn_special = "Inkjet"
            case "7":
                wpn_special = "Killer wail 5.1"
            case "8":
                wpn_special = "Kraken royale"
            case "9":
                wpn_special = "Reefslider"
            case "10":
                    wpn_special = "Splatcolour sreen"
            case "11":
                wpn_special = "Super chump"
            case "12":
                wpn_special = "Tacticooler"
            case "13":
                wpn_special = "Tenta missiles"
            case "14":
                wpn_special = "Triple Inkstrike"
            case "15":
                wpn_special = "Trizooka"
            case "16":
                wpn_special = "Ultra stamp"
            case "17":
                wpn_special = "Wave breaker"
            case "18":
                wpn_special = "Zipcaster"
            case "19":
                wpn_special = "Triple splashdown"
    print("Name:", wpn_name)
    print("Range:", wpn_range)
    print("Charge Speed:", wpn_crgspd)
    print("Mobilty:", wpn_mob)
    print("Brand:", wpn_brand)
    print("Sub:", wpn_sub)
    print("Special:", wpn_special)
    