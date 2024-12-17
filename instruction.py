import re

with open("instruction_input.txt", "r") as file:
    instructions = file.readline()
muls = re.findall(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))', instructions)
count = 0
do = True
for mul in muls:
    if mul[2] == "do()":
        do = True
        continue
    if mul[3] == "don't()":
        do = False
        continue
    if do:
        count += int(mul[0]) * int(mul[1])
print(count)