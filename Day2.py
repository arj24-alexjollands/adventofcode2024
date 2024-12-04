def is_only_increasing_or_decreasing(row):
    data = list(map(int, row.split()))
    is_increasing = all(data[i] <= data[i + 1] for i in range(len(data) - 1))
    is_decreasing = all(data[i] >= data[i + 1] for i in range(len(data) - 1))
    return is_increasing or is_decreasing

def passes_safety_check(numbers):
    return all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

def is_dampener_safe(row, passes_safety_check, is_only_increasing_or_decreasing):
    failchecks = list(map(int, row.split()))
    if passes_safety_check(failchecks) and is_only_increasing_or_decreasing(row):
        return True
    for i in range(len(failchecks)):
        modified_numbers = failchecks[:i] + failchecks[i + 1:]
        modified_row = " ".join(map(str, modified_numbers))
        if passes_safety_check(modified_numbers) and is_only_increasing_or_decreasing(modified_row):
            return True
    return False

with open('resources/reports.txt', 'r') as file:
    rows = file.readlines()

safetyIncrementList = []

for row in rows:
    numbers = list(map(int, row.split()))
    is_safe_change = all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))
    safetyIncrementList.append(is_safe_change)

safe_report_list = [
    safety and is_only_increasing_or_decreasing(row) for safety, row in zip(safetyIncrementList, rows)
]

safe_count = sum(safe_report_list)
print("Count of Safe Records:", safe_count)

dampener_safe_list = []

for row in rows:
    dampener_safe_list.append(is_dampener_safe(row, passes_safety_check, is_only_increasing_or_decreasing))

dampener_count = sum(dampener_safe_list)
print("Count of Dampener-Safe Records:", dampener_count)