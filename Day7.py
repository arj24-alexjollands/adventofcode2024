def parse_file(file_name):
    results = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    recording = int(parts[0].strip())
                    values = list(map(int, parts[1].strip().split()))
                    results.append((f"recording:{recording}", f"values:{values}"))
    except Exception as e:
        print(f"An error occurred: {e}")
    return results


def try_operations(recording, values):
    def evaluate_expression(ops):
        result = values[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += values[i + 1]
            elif op == '*':
                result *= values[i + 1]
            elif op == '||':
                result = int(str(result) + str(values[i + 1]))
        return result

    def generate_operation_combinations(n):
        if n <= 1:
            return [[]]
        ops = []
        for combo in generate_operation_combinations(n - 1):
            ops.append(combo + ['+'])
            ops.append(combo + ['*'])
            ops.append(combo + ['||'])
        return ops

    operation_combinations = generate_operation_combinations(len(values))

    for ops in operation_combinations:
        if evaluate_expression(ops) == recording:
            return True
    return False


def process_records(data):
    total_records = len(data)
    total_can_be_reached = 0
    total_sum = 0

    for record in data:
        recording_str, values_str = record
        recording = int(recording_str.split(':')[1])
        values = eval(values_str.split(':')[1])

        if try_operations(recording, values):
            total_can_be_reached += 1
            total_sum += recording

    return total_records, total_can_be_reached, total_sum


file_name = 'resources/equations.txt'
data = parse_file(file_name)
total_records, total_can_be_reached, total_sum = process_records(data)
print(f"total_records: {total_records}, total_can_be_reached: {total_can_be_reached}, total_sum={total_sum}")
