# 9.1
def store_grades():
    with open('grades.txt', 'w') as file:
        while True:
            try:
                grade = input("Enter a grade (or 'done' to finish): ")
                if grade.lower() == 'done':
                    break
                file.write(f"{float(grade):.1f}\n")
            except ValueError:
                print("Enter a valid number or 'done'")

# 9.2
def print_grades():
    grades = []
    with open('grades.txt', 'r') as file:
        for grade in file:
            grades.append(float(grade.strip()))

    total = sum(grades)
    count = len(grades)
    average = total / count if count > 0 else 0

    print("\nIndividual Grades:")
    for grade in grades:
        print(f"{grade:.1f}")

    print("\nTotal: {:.1f}".format(total))
    print("Count: {}".format(count))
    print("Average: {:.1f}".format(average))

store_grades()
print_grades()

# 9.3
import csv


def write_grades_csv():
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        while True:
            first_name = input(
                "\nEnter the student's first name (or 'done' to finish): ")
            if first_name.lower() == 'done':
                break
            last_name = input("Enter the student's last name: ")
            grades = []
            for i in range(1, 4):
                while True:
                    try:
                        grade = int(input(f"Enter grade for Exam {i}: "))
                        grades.append(grade)
                        break
                    except ValueError:
                        print("Enter a valid number!")

            writer.writerow([first_name, last_name] + grades)

    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

write_grades_csv()
