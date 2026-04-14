#Build a student Grade Trader
#stores students names and scores in a dictionary
#calculates average, highest, and lowest score
#saves results to a .txt file
#handles errors if someone enters letters instead of numbers

students = {}

while True:
    name = input("Enter student name (or 'done' to stop): ")
    
    if name.lower() == 'done':
        break
    
    # ask for score WITH error handling — right here, before storing
    while True:
        try:
            score = int(input(f"Enter score for {name}: "))
            break  # only exits if int() succeeded
        except ValueError:
            print("Invalid! Please enter a number.")
    
    students[name] = score  # store AFTER successful conversion

# stats go here — AFTER the outer loop ends
scores = list(students.values())
average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)

print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest:  {lowest}")

# file writing goes here — last step
with open("results.txt", "w") as file:
    file.write("Student Grade Report\n")
    file.write("=====================\n")
    for name, score in students.items():
        file.write(f"{name}: {score}\n")
    file.write(f"\nAverage: {average:.2f}\n")
    file.write(f"Highest: {highest}\n")
    file.write(f"Lowest:  {lowest}\n")