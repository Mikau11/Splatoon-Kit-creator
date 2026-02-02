import time

class brands():
    wpn_brand = "null"
    def brands_3():
        print("What do you want the brand to be?(to be on this list they have to have at least one weapon in splatoon 3)")
        print("(1)Annaki\n(2)Barazushi\n(3)Cuttlegear\n(4)Emebrz\n(5)Enperry\n(6)Firefin\n(7)Forge\n(8)Inkline\n(9)Krak-On\n(10)Squidforce")
        print("(11)Tentatek\n(12)Z+F\n(13)Zink(14)Custom\n(15)None")
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
                brands.wpn_brand = "Firefin"
            case "7":
                brands.wpn_brand = "Forge"
            case "8":
                brands.wpn_brand = "Inkline"
            case "9":
                brands.wpn_brand = "Krak-On"
            case "10":
                brands.wpn_brand = "Squidforce"
            case "11":
                brands.wpn_brand = "Tentatek"
            case "12":
                brands.wpn_brand = "Z+F"
            case "13":
                brands.wpn_brand = "Zink"
            case "14":
                brands.wpn_brand = input("Whats your custom brand name?")
            case "15":
                brands.wpn_brand = "None"
            case _:
                print("No brand here, if you want a custom brand type '14'")
                time.sleep(2)
                brands.brands_3()
