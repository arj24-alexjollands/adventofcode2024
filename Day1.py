from collections import Counter

def process_location_ids(file_path):
    column_a = []
    column_b = []

    with open(file_path, 'r') as file:
        for line in file:
            nums = line.strip().split()
            if len(nums) == 2:
                column_a.append(int(nums[0]))
                column_b.append(int(nums[1]))

    column_a.sort()
    column_b.sort()

    total_difference = sum(abs(a - b) for a, b in zip(column_a, column_b))
    print(f"Total difference: {total_difference}")

    frequency_counter = Counter(column_b)
    frequency_list = [frequency_counter[a] for a in column_a]
    total_product_sum = sum(a * freq for a, freq in zip(column_a, frequency_list))
    print(f"Total product sum: {total_product_sum}")

# Specify the path to your file
file_path = "resources/locationIDs.txt"

# Process the file
process_location_ids(file_path)
