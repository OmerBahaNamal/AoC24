input = ""


size = 131
def patrol(map):
    route = set()
    direction = "^"
    coor = map.find("^")
    x, y = coor % size, coor // size
    while 0 < x < size and 0 <= y < size - 1:
        if (x, y, direction) in route:
            return 1
        else:
            route.add((x, y, direction))

        match direction:
            case "^":
                if y == 0:
                    break
                elif map[(y - 1) * size + x] == "#":
                    direction = ">"
                else:
                    y -= 1
            case "v":
                if y == size - 2:
                    break
                elif map[(y + 1) * size + x] == "#":
                    direction = "<"
                else:
                    y += 1
            case "<":
                if x == 1:
                    break
                elif map[y * size + (x - 1)] == "#":
                    direction = "^"
                else:
                    x -= 1
            case ">":
                if x == size - 1:
                    break
                elif map[y * size + (x + 1)] == "#":
                    direction = "v"
                else:
                    x += 1
    return 0

count = 0

for i in range((size - 1) * (size)):
    if input[i] == "^" or input[i] == "\n":
        continue
    else:
        new_input = input[:i] + "#" + input[i+1:]
        count += patrol(new_input)

print(count)
