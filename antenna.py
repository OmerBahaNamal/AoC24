import itertools

with open("antenna_input.txt", "r") as f:
    antenna_map = f.read().split("\n")

antinodes = set()
antennas = {}
height = len(antenna_map)
width = len(antenna_map[0])
for y in range(height):
    for x in range(width):
        antenna = antenna_map[y][x]
        if antenna != '.':
            if antenna not in antennas:
                antennas[antenna] = [(x, y)]
            else:
                antennas[antenna].append((x, y))
for frequency in antennas:
    for (x1, y1), (x2, y2) in itertools.combinations(antennas[frequency], 2):
        dif_x = x1 - x2
        dif_y = y1 - y2
        p = 0
        while 0 <= x1 + dif_x * p < width and 0 <= y1 + dif_y * p < height:
            antinodes.add((x1 + dif_x * p, y1 + dif_y * p))
            p += 1
        n = 0
        while 0 <= x1 + dif_x * n < width and 0 <= y1 + dif_y * n < height:
            antinodes.add((x1 + dif_x * n, y1 + dif_y * n))
            n -= 1

print(len(antinodes))
