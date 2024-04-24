print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
# below picture comes from http://ascii.co.uk/art 
# print(r''' text ''')  the r is for raw string to ingnore character that could be interpreted as escape
# fixing this error message: D:\Michel\Projects\Python_100_Days\treasure_island.py:4: SyntaxWarning: invalid escape sequence '\`'
print(r'''
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

while True:
  question_1 = input("Turn Right or Left? ").lower()
  if question_1 == "right":
     print("Fall into a hole. Game Over.")
  else:
     question_2 = input("Swim or Wait? ").lower()
     if question_2 == "swim":
        print("You were eaten by a shark. Game Over!")
     else:
        question_3 = input("Which door? Red, Blue or Yellow: ").lower()
        if question_3 == "yellow":
          print("You Win!")
        else:
          print("Game Over")

  end_game = input("Do you want to play again? Y or N: ").lower()
  if end_game != "y":
     print("Thank you for playing!")
     break       

