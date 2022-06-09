import csv
import random

file = open("young_transposed.csv", "r")
csv_reader = csv.reader(file)

lists_from_csv = []
for row in csv_reader:
    lists_from_csv.append(row)

print(lists_from_csv)

random_num = (random.randint(0, 112))

print(lists_from_csv[random_num])
