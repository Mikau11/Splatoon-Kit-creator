import time

class brands():
    wpn_brand = "null"
    def brands_1():
        print("What do you want the brand to be?(to be on this list they have to have at least one weapon in splatoon 1)")
        print("(1)Cuttlegear\n(2)Forge\n(3)Krak-On\n(4)Zink\n(5)Custom\n(6)None")
        type = input()
        match type:
            case "1":
                brands.wpn_brand = "Cuttle gear"
            case "2":
                brands.wpn_brand = "Forge"
            case "3":
                brands.wpn_brand = "Krak-On"
            case "4":
                brands.wpn_brand = "Zink"
            case "5":
                brands.wpn_brand = input("Whats your custom brand name?")
            case "6":
                brands.wpn_brand = "None"
            case _:
                print("No brand here, if you want a custom brand type '5'")
                time.sleep(2)
                brands.brands_1()
    def brands_2():
        print("What do you want the brand to be?(to be on this list they have to have at least one weapon in splatoon 2)")
        print("(1)Cuttle Gear\n(2)Enperry\n(3)Firefin\n(4)Forge\n(5)Inkline\n(6)Krak-On\n(7)SquidForce\n(8)Tentatek\n(9)Kensa\n(10)Zink\n(11)Custom\n(12)None")
        type = input()
        match type:
            case "1":
                brands.wpn_brand = "Cuttle gear"
            case "2":
                brands.wpn_brand = "Enprry"
            case "3":
                brands.wpn_brand = "Firefin"
            case "4":
                brands.wpn_brand = "Forge"
            case "5":
                brands.wpn_brand = "Inkline"
            case "6":
                brands.wpn_brand = "Krak-On"
            case "7":
                brands.wpn_brand = "SquidForce"
            case "8":
                brands.wpn_brand = "Tentatek"
            case "9":
                brands.wpn_brand = "Kensa"
            case "10":
                brands.wpn_brand = "Zink"
            case "11":
                brands.wpn_brand = input("Whats your custom brand name?")
            case "12":
                brands.wpn_brand = "None"
            case _:
                print("No brand here, if you want a custom brand type '11'")
                time.sleep(2)
                brands.brands_2()
    def brands_3():
        print("What do you want the brand to be?(to be on this list they have to have at least one weapon in splatoon 3)")
        print("(1)Annaki\n(2)Barazushi\n(3)Cuttlegear\n(4)Emebrz\n(5)Enperry\n(6)Forge\n(7)Inkline\n(8)Krak-On\n(9)Squidforce")
        print("(10)Tentatek\n(11)Z+F\n(12)Zink\n(13)Custom\n(14)None")
        type = input()
        match type:
            case "1":
                brands.wpn_brand = "Annaki"
            case "2":
                brands.wpn_brand = "Barazushi"
            case "3":
                brands.wpn_brand = "Cuttlegear"
            case "4":
                brands.wpn_brand = "Emberz"
            case "5":
                brands.wpn_brand = "Enperry"
            case "6":
                brands.wpn_brand = "Forge"
            case "7":
                brands.wpn_brand = "Inkline"
            case "8":
                brands.wpn_brand = "Krak-On"
            case "9":
                brands.wpn_brand = "Squidforce"
            case "10":
                brands.wpn_brand = "Tentatek"
            case "11":
                brands.wpn_brand = "Z+F"
            case "12":
                brands.wpn_brand = "Zink"
            case "13":
                brands.wpn_brand = input("Whats your custom brand name?")
            case "14":
                brands.wpn_brand = "None"
            case _:
                print("No brand here, if you want a custom brand type '13'")
                time.sleep(2)
                brands.brands_3()
