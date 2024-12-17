import re
import itertools


def apply_rules(u):
    global regex
    for rule in regex:
        if rule.search(u) is not None:
            return False
    return True


def count_left_right(n, ns):
    global rules
    count_right = 0
    count_left = 0
    for left, right in rules:
        if right == n and left in ns:
            count_right += 1
        elif left == n and right in ns:
            count_left += 1
    return count_left, count_right


def sum_mid(lines):
    count = 0
    for u in lines:
        n = u.split(",")
        count += int(n[len(n) // 2])
    return count


goods = set()
bads = set()
later_goods = set()
rules = set()

with open("order_input.txt", "r") as file:
    is_update = False
    updates = []
    regex = []
    for line in file.readlines():
        if line == "\n":
            is_update = True
            continue

        if is_update:
            updates.append(line.strip())
        else:
            first, second = line.strip().split("|")
            regex.append(re.compile(fr'{second}.+{first}'))
            rules.add((first, second))

for update in updates:
    if apply_rules(update):
        goods.add(update)
    else:
        bads.add(update)

count = 0

for bad in bads:
    nums = bad.split(",")
    print(nums)
    for num in nums:
        left, right = count_left_right(num, nums)
        if left == right:
            count += int(num)
            break
print(count)
