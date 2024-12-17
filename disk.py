def find_block(block_t, b):
    while b > 0 and detailed_disk[b] != block_t:
        b -= 1
    block_begin = b

    while b > 0 and detailed_disk[b] == block_type:
        b -= 1
    block_end = b
    return block_begin, block_end

def find_space(f):
    while f < len(detailed_disk) - 1 and detailed_disk[f] != -1:
        f += 1
    free_begin = f

    while f < len(detailed_disk) - 1 and detailed_disk[f] == -1:
        f += 1
    free_end = f
    return free_begin, free_end

with open("disk_input.txt", "r") as file:
    disk = file.readline()

print(disk)
detailed_disk = list()
block = 1
for i in range(len(disk)):
    if block:
        for j in range(int(disk[i])):
            detailed_disk.append(i // 2)
    else:
        for j in range(int(disk[i])):
            detailed_disk.append(-1)
    block = 1 - block


f = 0
free_size = 0
b = len(detailed_disk) - 1
block_size = 0
block_type = len(disk) // 2 + 1
print(len(disk))
#6359578040619
#6359491896845

while block_type > 1:
    if free_size >= block_size:
        for i in range(block_size):
            detailed_disk[free_begin + i] = block_type
            detailed_disk[block_end + i + 1] = -1
        f = 0
        free_size = 0
        block_type -= 1
        block_begin, block_end = find_block(block_type, b)
        block_size = block_begin - block_end
        if block_size != 0:
            b = block_end
    else:
        free_begin, free_end = find_space(f)
        f = free_end
        free_size = free_end - free_begin
        if free_begin > block_end:
            block_size = 0

count = 0
for i in range(len(detailed_disk)):
    if detailed_disk[i] == -1:
        continue
    count += i * detailed_disk[i]

print(count)
