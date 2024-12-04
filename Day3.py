import re

def filter_operations(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        filtered_content = re.sub(r"don't\(\).*?do\(\)|don't\(\).*?$", "don't()do()", content, flags=re.DOTALL)

        with open(output_file, 'w') as file:
            file.write(filtered_content)
        print(f"Filtered content created: '{output_file}'.")
    except Exception as e:
        print(f"Error during filtering: {e}")


def extract_mul_occurrences(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, content)

        total_sum = 0
        if matches:
            for match in matches:
                num1 = int(match[0])
                num2 = int(match[1])
                product = num1 * num2
                total_sum += product
        print("\nTotal Sum:", total_sum)
    except Exception as e:
        print(f"Error: {e}")

input_file = "resources/corrupted-memory.txt"
output_file = "resources/enabled-operations.txt"
filter_operations(input_file, output_file)
extract_mul_occurrences(output_file)

