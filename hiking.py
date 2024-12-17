
with open("hiking_input.txt", "r") as file:
    map = []
    for line in file.readlines():
        map.append([int(i) for i in line.strip()])

lookup = {}


def bfs(queue, nine, c):
    if len(queue) == 0:
        return c

    num, x, y = queue.pop(0)

    if num == 9:
        c += 1
        nine.add((num, x, y))
        return bfs(queue, nine, c)

    if y > 0 and map[y - 1][x] == num + 1:
        queue.append((num + 1, x, y - 1))
    if y < len(map) - 1 and map[y + 1][x] == num + 1:
        queue.append((num + 1, x, y + 1))
    if x > 0 and map[y][x - 1] == num + 1:
        queue.append((num + 1, x - 1, y))
    if x < len(map[0]) - 1 and map[y][x + 1] == num + 1:
        queue.append((num + 1, x + 1, y))

    return bfs(queue, nine, c)

count = 0
rates = 0

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 0:
            nines = set()
            rate = bfs([(0, j, i)], nines, 0)
            rates += rate
            count += len(nines)
            print(rate)
print(count)
print(rates)