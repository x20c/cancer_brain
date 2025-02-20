import random
import csv
import json
#Task 1
with open('hello.txt', 'w') as f:
    f.write('Hello world!')
#Task 2
with open('hello.txt', 'w') as f:
    f.write(f'{random.randint(1, 10)}')
#Task 3
with open('hello.txt', 'a+') as f:
    f.seek(0)
    n = int(f.read().strip())
    f.write('\n')
    li = ''
    for i in range(n):
        li += f'"{chr(65 + i)}", '
    li = li[:-2]
    f.write(li)

#Task 4
with open('hello.txt', 'r') as f:
    print(f.read())
#Task 5
warehouse = [
    {"product": "Apple", "price": 0.5, "quantity": 10},
    {"product": "Banana", "price": 0.75, "quantity": 20},
    {"product": "Orange", "price": 0.35, "quantity": 15}
]
with open("warehouse_v1.csv", "w") as f:
    f.write("product,price,quantity\n")

    for item in warehouse:
        f.write(f'{item["product"]},{item["price"]},{item["quantity"]}\n')
#Task 6
with open("warehouse_v2.csv", "w", newline='') as f:
    fieldnames = ["product", "price", "quantity"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(warehouse)
#Task 7
with open('warehouse.json', 'w') as f:
    json.dump(warehouse, f, indent=1)