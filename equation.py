from functools import reduce
import time

add = 0
mul = 1
found_nums = []
start = time.time()


def calc(ops, nums):
    res = nums[0]
    for k in range(len(nums) - 1):
        match ops % 3:
            case 0:
                res += numbers[k + 1]
            case 1:
                res *= numbers[k + 1]
            case 2:
                res = int(str(res) + str(numbers[k + 1]))
        ops //= 3
    return res


with open("equation_input.txt", 'r') as file:
    lines = file.readlines()

    for line in lines:

        numbers = line.split()

        big = int(numbers[0][:-1])

        numbers = numbers[1:]

        numbers = list(map(int, numbers))

        for operators in range(0, 3 ** (len(numbers))):
            if calc(operators, numbers) == big:
                found_nums.append(big)
                break
    print(found_nums)
    print(reduce(lambda a, b: a + b, found_nums, 0))
    print(time.time() - start)
