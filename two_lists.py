
with open("two_lists_input.txt", "r") as file:
    left = []
    right = []
    for line in file.readlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()

distance = 0
for i in range(len(left)):
    distance += abs(left[i] - right[i])

similarity = 0
for num in left:
    num_count = num * right.count(num)
    similarity += num_count
print(similarity)
