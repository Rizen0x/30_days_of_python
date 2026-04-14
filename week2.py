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
    
    while True:
        try:
            score = int(input(f"Enter score for {name}: "))
            break
        except ValueError:
            print("Invalid! Please enter a number.")

    if score >= 70:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    elif score >= 50:
        grade = 'C'
    elif score >= 40:
        grade = 'D'
    else:
        grade = 'F'
    
    students[name] = {"score": score, "grade": grade}

if len(students) == 0:
    print("No students entered.")
else:
    scores = [data["score"] for data in students.values()]
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest:  {lowest}")
    print("\nStudent Results:")
    for name, data in students.items():
        print(f"{name}: {data['score']} - grade: {data['grade']}")

    with open("results.txt", "w") as file:
        file.write("Student Grade Report\n")
        file.write("=====================\n")
        for name, data in students.items():
            file.write(f"{name}: {data['score']} - grade: {data['grade']}\n")
        file.write(f"\nAverage: {average:.2f}\n")
        file.write(f"Highest: {highest}\n")
        file.write(f"Lowest:  {lowest}\n")