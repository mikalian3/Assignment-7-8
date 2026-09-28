f = open("program4.txt", "r")
total_extended_price = 0.0
order_count = 0
print(f"{'Item:':12} {'Quantity:':10}   {'Price:':10} {'Extended:':10}")
item = f.readline().rstrip('\n')
while item != "":
    quantity = int(f.readline())
    price = float(f.readline())
    extended = quantity * price
    total_extended_price = total_extended_price + extended 
    order_count = order_count + 1
    print(f"{item:10} {quantity:10} {price:10.2f}   {extended:10.2f}")
    item = f.readline().rstrip('\n')
f.close()
average_order = total_extended_price / order_count
print()
print(f"Total Extended Price: {total_extended_price:.2f}")
print(f"Number of Orders: {order_count}")
print(f"Average Order: {average_order:.2f}")
    
    
