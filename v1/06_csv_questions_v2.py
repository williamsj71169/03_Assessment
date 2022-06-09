import csv
import random

with open('young_transposed.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

random_num = (random.randint(0, 112))

print(data[random_num])
