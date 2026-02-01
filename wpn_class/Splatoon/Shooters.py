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
    print("Fire rate:", wpn_fr)
    print("Brand:", wpn_brand)
    print("Sub:", wpn_sub)
    print("Special:", wpn_special)
