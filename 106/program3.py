f = open("program3.txt", "r")
total_bonus = 0.0
print(f"{'Last Name':10}    {'Salary':10}    {'Bonus':10}")
last_name = f.readline().rstrip('\n')

while last_name != "":
    salary = float(f.readline())
    
    if salary >= 100000:
        bonus_rate = 0.20
    elif salary >= 50000:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10
        
    bonus = salary * bonus_rate
    total_bonus = total_bonus + bonus
    print(f"{last_name:10} {salary:10.2f}   {bonus:10.2f}")
    last_name = f.readline().rstrip('\n')
f.close()
print()
print(f"Total Bonuses Paid: {total_bonus:.2f}")
        
    
        
    
    
