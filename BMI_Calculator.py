height = float(input("What is your height in meters e.g. 1.82:  "))  # in meters e.g., 1.55
weight = int(input("What is your weight in kilograms e.g. 72:  "))  # in kilograms e.g., 72
# Your code below this line 👇
bmi = weight / (height * height)
formatted_bmi = f"{bmi:.2f}"
if bmi < 18.5:
  print(f"Your BMI is {formatted_bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {formatted_bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {formatted_bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {formatted_bmi}, you are obese.")
else:
  print(f"Your BMI is {formatted_bmi}, you are clinically obese.")