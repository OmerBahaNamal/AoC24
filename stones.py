import functools
import time
test = ""
input = ""

stones = list(map(int, input.strip().split()))
@functools.cache
def grave(stn, c):
    if c == 75:
        return 1

    length = len(str(stn))
    if length % 2 == 0:
        half = length // 2
        return grave(stn // (10 ** half), c + 1) + grave(stn % (10 ** half), c + 1)
    elif stn == 0:
        return grave(1, c + 1)
    else:
        return grave(stn * 2024, c + 1)

print(sum(grave(stone, 0) for stone in stones))
start = time.time()
print(time.time() - start)
