import re

fname = "actual_data.txt"
handle = open(fname)
sum = 0
count = 0

for line in handle:

    num_list = re.findall("[0-9]+", line)

    for num in num_list:
        sum += int(num)
        count += 1

print(f"There are {count} values with a sum = {sum}")
