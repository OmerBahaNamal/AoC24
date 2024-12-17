
with open("garden_test.txt", "r") as file:
    garden = list(map(str.strip, file.readlines()))

def calculate_perimeter(a):
    p = 0
    s = set()
    for x, y in a:
        if (x - 1, y) not in a:
            if not ((x - 1, y - 1, x, y - 1) in s or (x - 1, y + 1, x, y + 1) in s):
                p += 1
            if (x - 1, y - 1, x, y - 1) in s and (x - 1, y + 1, x, y + 1) in s:
                p -= 1
            s.add((x - 1, y, x, y))

        if (x + 1, y) not in a:

            if not ((x + 1, y - 1, x, y - 1) in s or (x + 1, y + 1, x, y + 1) in s):
                p += 1
            if (x + 1, y - 1, x, y - 1) in s and (x + 1, y + 1, x, y + 1) in s:
                p -= 1
            s.add((x + 1, y, x, y))

        if (x, y + 1) not in a:

            if (x - 1, y + 1, x - 1, y) in s and (x + 1, y + 1, x + 1, y) in s:
                p -= 1
            if not ((x - 1, y + 1, x - 1, y) in s or (x + 1, y + 1, x + 1, y) in s):
                p += 1
            s.add((x, y + 1, x, y))

        if (x, y - 1) not in a:

            if (x - 1, y - 1, x - 1, y) in s and (x + 1, y - 1, x + 1, y) in s:
                p -= 1
            if not ((x - 1, y - 1, x - 1, y) in s or (x + 1, y - 1, x + 1, y) in s):
                p += 1
            s.add((x, y - 1, x, y))
    return p

def calculate_preis(a):
    p = calculate_perimeter(a)
    return len(a) * p

height = len(garden)
width = len(garden[0])

plant_types = {}

for y in range(height):
    for x in range(width):
        if garden[y][x] not in plant_types:
            plant_types[garden[y][x]] = [{(x, y)}]
        else:
            found = -1
            for i, area in enumerate(plant_types[garden[y][x]]):
                if (x - 1, y) in area or (x + 1, y) in area or (x, y + 1) in area or (x, y - 1) in area:
                    if found != -1:
                        base_area = plant_types[garden[y][x]][found]
                        plant_types[garden[y][x]][found] = base_area.union(area)
                        plant_types[garden[y][x]].remove(area)
                        continue
                    area.add((x, y))
                    found = i
            if found == -1:
                plant_types[garden[y][x]].append({(x, y)})


count = 0

print(*plant_types.values())
