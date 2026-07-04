# Ayrton Shaffer
# Grades Assignment

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


student_name = input("Enter the student name: ")

grade1 = int(input("Enter grade 1: "))
grade2 = int(input("Enter grade 2: "))
grade3 = int(input("Enter grade 3: "))
grade4 = int(input("Enter grade 4: "))
grade5 = int(input("Enter grade 5: "))

grades = [grade1, grade2, grade3, grade4, grade5]

average = sum(grades) / len(grades)
letter_grade = get_letter_grade(average)

print()
print(student_name)
print()
print("Average:", average)
print()
print("Letter Grade:", letter_grade)