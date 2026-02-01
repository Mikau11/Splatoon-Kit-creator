from splat1 import *
from splat2 import *
from splat3 import *



print("*****Welcome to My Kit Creator!!!*****")
print("  ***Choose a Game:***  ")
print("(1)Splatoon")
print("(2)Splatoon 2")
print("(3)Splatoon 3")
game = input()

if game == "1":
    print("Splatoon")
    splat1()
elif game == "2":
    print("Splatoon 2")
    splat2()
elif game == "3":
    splat3()
else:
    print("Splatoon", game)