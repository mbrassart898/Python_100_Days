print("\nWelcome to Treasure Island.\n")
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
  question_1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()
  if question_1 == "left":
     # continue the game
     question_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat. Type "swim" to swim accross.').lower()
     if question_2 == "wait":
        #game continue
        question_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which door do you choose? red, yellow, or blue: ").lower()
        if question_3 == "yellow":
          print("You found the treasure! You Win!")
        elif question_3 == "red":
          print("It's a room full of fire. Game is over!")
        elif question_3 == "blue":
          print("you enter a room of beasts. Game is over!")
        else:
          Print()
     else:   
        print("You were eaten by a shark. Game Over!")
  else:
     print("Fall into a hole. Game Over.")
     
 
  end_game = input("Do you want to play again? Y or N: ").lower()
  if end_game != "y":
     print("Thank you for playing!")
     break       

