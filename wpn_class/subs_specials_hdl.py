import time

class subs():
    wpn_sub = "null"
    def subs_1():
        print("What do you want the sub to be?")
        print("(1)Splat\n(2)Burst\n(3)Suction\n(4)Seeker\n(5)Inkmine\n(6)Disruptor\n(7)Point Sensor\n(8)Splashwall\n(9)Sprinkler\n(10)Beakon")
        type = input()
        match type:
            case "1":
                subs.wpn_sub = "Splat bomb"
            case "2":
                subs.wpn_sub = "Burst bomb"
            case "3":
                subs.wpn_sub = "Suction bomb"
            case "4":
                subs.wpn_sub = "Curlinb bomb"
            case "5":
                subs.wpn_sub = "Inkmine"
            case "6":
                subs.wpn_sub = "Disruptor"
            case "7":
                subs.wpn_sub = "Point sensor"
            case "8":
                subs.wpn_sub = "Splash wall"
            case "9":
                subs.wpn_sub = "Sprinkler"
            case "10":
                subs.wpn_sub = "Beakon"
            case _:
                print("No subs here")
                time.sleep(2)
                subs.subs_1()
    def subs_2():
        print("What do you want the sub to be?")
        print("(1)Splat\n(2)Burst\n(3)Suction\n(4)Curling\n(5)Auto\n(6)Inkmine\n(7)Toxic mist\n(8)Point Sensor\n(9)Splashwall\n(10)Sprinkler\n(11)Beakon")
        print("(12)Fizzy\n(13)Torpedo")
        type = input()
        match type:
            case "1":
                subs.wpn_sub = "Splat bomb"
            case "2":
                subs.wpn_sub = "Burst bomb"
            case "3":
                subs.wpn_sub = "Suction bomb"
            case "4":
                subs.wpn_sub = "Curling bomb"
            case "5":
                subs.wpn_sub = "Auto bomb"
            case "6":
                subs.wpn_sub = "Ink mine"
            case "7":
                subs.wpn_sub = "Toxic mist"
            case "8":
                subs.wpn_sub = "Point sensor"
            case "9":
                subs.wpn_sub = "Splash wall"
            case "10":
                subs.wpn_sub = "Sprinkler"
            case "11":
                subs.wpn_sub = "Squid Beakon"
            case "12":
                subs.wpn_sub = "Fizzy bomb"
            case "13":
                subs.wpn_sub = "Torpedo"
            case _:
                print("No subs here")
                time.sleep(2)
                subs.subs_2()
    def subs_3():
        print("What do you want the sub to be?")
        print("(1)Splat\n(2)Suction\n(3)Burst\n(4)Curling\n(5)Auto\n(6)Ink Mine\n(7)Toxic mist\n(8)Point sensor\n(9)Splash wall\n(10)Sprinkler")
        print("(11)Beakon\n(12)Fizzy\n(13)Torpedo\n(14)Angle shooter")
        type = input()
        match type:
            case "1":
                subs.wpn_sub = "Splat bomb"
            case "2":
                subs.wpn_sub = "Suction bomb"
            case "3":
                subs.wpn_sub = "Burst bomb"
            case "4":
                subs.wpn_sub = "Curling bomb"
            case "5":
                subs.wpn_sub = "Auto bomb"
            case "6":
                subs.wpn_sub = "Ink mine"
            case "7":
                subs.wpn_sub = "Toxic mist"
            case "8":
                subs.wpn_sub = "Point sensor"
            case "9":
                subs.wpn_sub = "Splash wall"
            case "10":
                subs.wpn_sub = "Sprinkler"
            case "11":
                subs.wpn_sub = "Squid Beakon"
            case "12":
                subs.wpn_sub = "Fizzy bomb"
            case "13":
                subs.wpn_sub = "Torpedo"
            case "14":
                subs.wpn_sub = "Angle shooter"
            case _:
                print("No subs here")
                time.sleep(2)
                subs.subs_3()

class specials():
    wpn_special = "null"
    def specials_1():
        print("What do you want the special to be?")
        print("(1)Bomb Rush\n(2)Bubbler\n(3)Echolocator\n(4)Inkstrike\n(5)Inkzooka\n(6)Killer Wail\n(7)Kraken")
        type = input()
        match type:
                case "1":
                    specials.wpn_special = "Bomb Rush"
                case "2":
                    specials.wpn_special = "Bubbler"
                case "3":
                    specials.wpn_special = "Echolocator"
                case "4":
                    specials.wpn_special = "Inkstrike"
                case "5":
                    specials.wpn_special = "Inkzooka"
                case "6":
                    specials.wpn_special = "Killer Wail"
                case "7":
                    specials.wpn_special = "Kraken"
                case _:
                    print("No specials here")
                    time.sleep(2)
                    specials.specials_1()
    def specials_2():
        print("What do you want the special to be?")
        print("(1)Baller\n(2)Bomb Launcher\n(3)Booyah Bomb\n(4)Bubble Blower\n(5)Ink Armour\n(6)Ink storm\n(7)Inkjet\n(8)Splashdown\n(9)Sting Ray(please don't)")
        print("(10)Tenta Missiles\n(11)Ultra stamp")
        type = input()
        match type:
                case "1":
                    specials.wpn_special = "Baller"
                case "2":
                    specials.wpn_special = "Bomb Launcher"
                case "3":
                    specials.wpn_special = "Booyah bomb"
                case "4":
                    specials.wpn_special = "Bubble Blower"
                case "5":
                    specials.wpn_special = "Ink Armour"
                case "6":
                    specials.wpn_special = "Ink storm"
                case "7":
                    specials.wpn_special = "Inkjet"
                case "8":
                    specials.wpn_special = "Splashdown"
                case "9":
                    specials.wpn_special = "Sting Ray(Whats wrong whith you? Do you have ANY concept of fun?)"
                case "10":
                    specials.wpn_special = "Tenta Missiles"
                case "11":
                    specials.wpn_special = "Ultra stamp"
                case _:
                    print("No specials here")
                    time.sleep(2)
                    specials.specials_2()
    def specials_3():
        print("What do you want the special to be?")
        print("(1)Big Bubbler\n(2)Booyah bomb\n(3)Crab tank\n(4)Ink storm\n(5)Ink vac\n(6)Inkjet\n(7)Killer wail 5.1\n(8)Kraken royale\n(9)Reefslider")
        print("(10)Splatcolour screen\n(11)Super chump\n(12)Tacticooler\n(13)Tenta missiles\n(14)Triple Inkstike\n(15)Trizooka\n(16)Ultra stamp")
        print("(17)Wave breaker\n(18)Zipcaster\n(19)Triple splashdown")
        type = input()
        match type:
                case "1":
                    specials.wpn_special = "Big bubbler"
                case "2":
                    specials.wpn_special = "Booyah bomb"
                case "3":
                    specials.wpn_special = "Crab tank"
                case "4":
                    specials.wpn_special = "Ink storm"
                case "5":
                    specials.wpn_special = "Ink vac"
                case "6":
                    specials.wpn_special = "Inkjet"
                case "7":
                    specials.wpn_special = "Killer wail 5.1"
                case "8":
                    specials.wpn_special = "Kraken royale"
                case "9":
                    specials.wpn_special = "Reefslider"
                case "10":
                    specials.wpn_special = "Splatcolour sreen"
                case "11":
                    specials.wpn_special = "Super chump"
                case "12":
                    specials.wpn_special = "Tacticooler"
                case "13":
                    specials.wpn_special = "Tenta missiles"
                case "14":
                    specials.wpn_special = "Triple Inkstrike"
                case "15":
                    specials.wpn_special = "Trizooka"
                case "16":
                    specials.wpn_special = "Ultra stamp"
                case "17":
                    specials.wpn_special = "Wave breaker"
                case "18":
                    specials.wpn_special = "Zipcaster"
                case "19":
                    specials.wpn_special = "Triple splashdown"
                case _:
                    print("No specials here")
                    time.sleep(2)
                    specials.specials_3()