import re

input = ""

size = 140


count = 0

rotate = bytearray(input, "utf-8")
diagonal = bytearray()
anti_diagonal = bytearray()

for i in range(size):
    for j in range(size):
        rotate[(size + 1) * i + j] = input.encode()[(size + 1) * j + i]

for i in range(size):
    for j in range(size - i):
        diagonal.append(input.encode()[(size + 1) * j + i + j])
    diagonal.append(10)

for i in range(1, size):
    for j in range(size - i):
        diagonal.append(input.encode()[(size + 1) * j + (size + 1) * i + j])
    diagonal.append(10)

for i in range(1, size + 1):
    for j in range(size - i + 1):
        anti_diagonal.append(input.encode()[(size + 1) * j + size - i - j])
    anti_diagonal.append(10)

for i in range(2, size + 1):
    for j in range(size - i + 1):
        anti_diagonal.append(input.encode()[(size + 1) * j + (size + 1) * i - 2 - j])
    anti_diagonal.append(10)


count += len(re.findall(r'XMAS', input))
count += len(re.findall(r'SAMX', input))
count += len(re.findall(r'XMAS', rotate.decode()))
count += len(re.findall(r'SAMX', rotate.decode()))
count += len(re.findall(r'XMAS', diagonal.decode()))
count += len(re.findall(r'SAMX', diagonal.decode()))
count += len(re.findall(r'XMAS', anti_diagonal.decode()))
count += len(re.findall(r'SAMX', anti_diagonal.decode()))
print(count)

acount = 0

for i in range(1, size - 1):
    for j in range(1, size - 1):
        first = False
        second = False
        if input[(size + 1) * i + j] == 'A':
            if ((input[(size + 1) * (i - 1) + (j - 1)] == 'S' and input[(size + 1) * (i + 1) + (j + 1)] == 'M') or
                    (input[(size + 1) * (i - 1) + (j - 1)] == 'M' and input[(size + 1) * (i + 1) + (j + 1)] == 'S')):
                first = True
            if ((input[(size + 1) * (i - 1) + (j + 1)] == 'S' and input[(size + 1) * (i + 1) + (j - 1)] == 'M') or
                    (input[(size + 1) * (i - 1) + (j + 1)] == 'M' and input[(size + 1) * (i + 1) + (j - 1)] == 'S')):
                second = True
            if first and second:
                acount += 1
print(acount)
