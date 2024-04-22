print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = (name1 + name2).lower()
score_a = 0
score_b = 0
for char in combined_names:
  if char == "t" or char == "r" or char == "u" or char == "e":
    score_a +=1
for char in combined_names:
  if char == "l" or char == "o" or char == "v" or char == "e":
    score_b +=1

final_score = str(score_a) + str(score_b)
  
love_score = int(final_score)

# For Scores less than 10 or greater than 90, the message should be
if love_score < 10 or love_score >=90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >=40 and love_score <=50:
  print(f"Your score is {love_score}, you are alright together.")
# For Scores between 40 and 50, the message should be:
else:
  print(f"Your score is {love_score}.")