import csv
import random

file = open("young_transposed.csv", "r")
csv_reader = csv.reader(file)

lists_from_csv = []
for row in csv_reader:
    lists_from_csv.append(row)

# print(lists_from_csv)
# print("***********************************")
print(lists_from_csv[0])
print(lists_from_csv[1])

questions = lists_from_csv[0]
answers = lists_from_csv[1]

random_num = random.randint(0, 113)

print("Question:{} | Answer:{}".format(questions[random_num],
                                       answers[random_num]))
