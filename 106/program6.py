student_count = 0
answer = input("Do you want to enter student data? (Yes/No): ")

while answer.lower() == "yes":
    last_name = input("Enter last name: ")
    score1 = float(input("Enter exam score 1: "))
    score2 = float(input("Enter exam score 2: "))

    average = (score1 + score2) / 2
    student_count = student_count + 1

    print(f"{last_name} average: {average:.2f}")
    answer = input("Do you want to enter another student? (Yes/No): ")
print(f"Number of students entered: {student_count}")