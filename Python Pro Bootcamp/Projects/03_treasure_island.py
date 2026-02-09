
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welocme to Treasure Island!")
print("Your mission is to find treasure")
choice = input("You are at a cross road. Where do you want to go? \n Type 'left' or 'right' ").strip().lower()

if choice != "left":
    print("Fall into a hole. GAME OVER ! ")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice = input("Type 'wait' to wait for a boat. Type 'swim' to swim acros ").strip().lower()
    if choice != "wait":
        print("Attacked by trout. GAME OVER ! ")
    else:
        print("You've met the door.")
        choice = input("What colour of the door you want to go. Red, Blue, Yellow ? ").strip().lower()
        if choice == 'red':
            print("Burned by fire. GAME OVER !")
        elif choice == 'blue':
            print("Eaten by beasts. GAME OVER !")
        elif choice == 'yellow':
            print("You WIN !!!")
        else:
            print("GAME OVER !!!")
