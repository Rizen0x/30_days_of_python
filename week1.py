#buid a "personal profile generator" write a python program that: asks the user for their
#  name, age, and favorite hobby uses if/else to give
#  them a custom message based on their age group uses a loop to let them enter 3 different hobbies 
# print a formatted "profile card" at the end.

#step1: ask for name and age name=input("enter your name: ") age=int(input("enter your age: "))
name = input("ENTER YOUR NAME: ")
age = int(input("ENTER YOUR AGE: "))

#step2: age group message using if/else statements
if age < 18:
    message = "You are a Teenager!"
elif age < 30:
    message = "You are a Young Adult"
else:
   message = "You are an Adult"

#step3: loop to collect 3 hobbies
hobbies = []
for i in range(3):
    hobby = input(f"Enter hobby  {i+1}:")
    hobbies.append(hobby)

# step4: print the profile card
print("\n--- YOUR PROFILE CARD---")
print(f"Name: {name}")
print(f"age: {age} -- {message}")
print(f"Hobbies: {', '.join(hobbies)}")




