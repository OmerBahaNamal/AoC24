import itertools
def increasing_or_decreasing(arr):
    return sorted(arr) == arr or sorted(arr, reverse=True) == arr


def max_difference(arr):
    for i in range(len(arr) - 1):
        dif = abs(arr[i] - arr[i + 1])
        if dif < 1 or dif > 3:
            return False
    return True


def apply_rules(arr):
    return increasing_or_decreasing(arr) and max_difference(arr)


with open("reports_input.txt", "r") as file:
    reports = []
    for line in file.readlines():
        reports.append(list(map(int, line.split())))

safe = list(filter(apply_rules, reports))

unsafe = list(itertools.filterfalse(apply_rules, reports))

new_safe = 0
for report in unsafe:
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        if apply_rules(new_report):
            new_safe += 1
            break

print(new_safe)
print(len(safe))
print(len(safe) + new_safe)