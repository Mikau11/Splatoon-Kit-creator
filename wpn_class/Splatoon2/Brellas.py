from_game = "splat2"

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
            wpn_dmg = input("What you want your Rollers Brellas to be?")
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
    print("Damage:", wpn_dmg)
    print("Durabilty:", wpn_dur)
    print("Brand:", wpn_brand)
    print("Sub:", wpn_sub)
    print("Special:", wpn_special)