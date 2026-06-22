# Student Grade Calculator

print("=== Student Grade Calculator ===")

name = input("Enter student name: ")

score1 = float(input("Enter score for Subject 1: "))
score2 = float(input("Enter score for Subject 2: "))
score3 = float(input("Enter score for Subject 3: "))
score4 = float(input("Enter score for Subject 4: "))
score5 = float(input("Enter score for Subject 5: "))

average = (score1 + score2 + score3 + score4 + score5) / 5

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== REPORT =====")
print("Student:", name)
print("Average Score:", round(average, 2))
print("Grade:", grade)

if grade == "A":
    print("Excellent Performance!")
elif grade == "B":
    print("Very Good!")
elif grade == "C":
    print("Good Job!")
elif grade == "D":
    print("Needs Improvement.")
else:
    print("Please Work Harder.")
