def calculate_points(grades):
    # dictionary to assign grades to their corresponding points
    grade_points = {"A": 20, "B": 17.5, "C": 15, "D": 12.5, "E": 10, "F": 0}

    total_points = 0

    # iterate through the grades and add the corresponding points
    for grade in grades:
        grade = grade.upper()
        if grade in grade_points:
            total_points += grade_points[grade]
        else:
            print("Invalid grade entered:", grade)
    return total_points

# list of subjects
subjects = [
    "Swedish",
    "Mathematics",
    "English",
    "Physics",
    "Chemistry",
    "Biology",
    "History",
    "Geography",
    "Civics",
    "Physical Education",
    "Religion",
    "Art",
    "Music",
    "HKK",
    "Technology",
    "Mother tongue",
    "Craft"
]

# ask the user to enter their grades
grades = []
for i, subject in enumerate(subjects):
    grade = input(f"Enter grade for {subject}: ")
    grades.append(grade)

# calculate and print the total points
total_points = calculate_points(grades)
print("Total points:", total_points, "out of 340")
if total_points >= 300:
    print("\nCrazyyy!!!!")
elif total_points >= 260:
    print("\nQuite nice")
elif total_points >= 220:
    print("\nGood")
elif total_points >= 180:
    print("\not bad, but not good either..")
elif total_points >= 140:
    print("\nConcerning")
elif total_points >= 100:
    print("\nReally Concerning")
else:
    print("\nFAILURE")
