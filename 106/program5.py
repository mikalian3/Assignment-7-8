f = open("program5.txt", "r")
total_tuition = 0.0
student_count = 0
print(f"{'Last Name:':10}    {'Credits:':10}    {'Tuition:':10}")
last_name = f.readline().rstrip('\n')
while last_name != "":
    district = f.readline().rstrip('\n')
    credits = int(f.readline())

    if district == "I":
        cost_per_credit = 250.00
    else:
        cost_per_credit = 500.00

    tuition = credits * cost_per_credit
    total_tuition = total_tuition + tuition
    student_count = student_count + 1
    print(f"{last_name:10} {credits:10} {tuition:10.2f}")
    last_name = f.readline().rstrip('\n')
f.close()
print()
print(f"Total Tuition Owed: {total_tuition:.2f}")
print(f"Number of Students: {student_count}")