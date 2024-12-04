import numpy as np

def load_wordsearch(file_path, padding_char='#'):
    try:
        with open(file_path, 'r') as file:
            data = [list(line.strip()) for line in file if line.strip()]

        wordsearch_array = np.array(data, dtype=str)
        padded_array = np.pad(
            wordsearch_array,
            pad_width=1,
            mode='constant',
            constant_values=padding_char
        )
        return padded_array
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])

def checkHorizontal(target, wordsearch):
    total_count = 0
    for row_index, row in enumerate(wordsearch):
        row_string = ''.join(row)
        count = row_string.count(target)
        total_count += count
    print(f"Total horizontal: {total_count}")
    return total_count

def checkVertical(target, wordsearch):
    total_count = 0
    num_rows = len(wordsearch)
    num_cols = len(wordsearch[0])

    for col in range(num_cols):
        column_string = ''.join(wordsearch[row][col] for row in range(num_rows))
        count = column_string.count(target)
        total_count += count
    print(f"Total vertical: {total_count}")
    return total_count

def checkDiagonal(target, wordsearch):
    total_count = 0
    num_rows = len(wordsearch)
    num_cols = len(wordsearch[0])
    target_len = len(target)

    for start_row in range(num_rows):
        for start_col in range(num_cols):
            # Down-right
            if start_row + target_len <= num_rows and start_col + target_len <= num_cols:
                diagonal = ''.join(wordsearch[start_row + i][start_col + i] for i in range(target_len))
                if diagonal == target:
                    total_count += 1
            # Down-left
            if start_row + target_len <= num_rows and start_col - target_len + 1 >= 0:
                diagonal = ''.join(wordsearch[start_row + i][start_col - i] for i in range(target_len))
                if diagonal == target:
                    total_count += 1

    print(f"Total diagonal: {total_count}")
    return total_count

def checkXPattern(target, wordsearch):
    total_count = 0
    num_rows = len(wordsearch)
    num_cols = len(wordsearch[0])

    for row in range(num_rows):
        for col in range(num_cols):
            try:
                if wordsearch[row][col] == target[1]:

                    left_stroke_forward = check_left_stroke(col, row, target, wordsearch)
                    left_stroke_backward = check_left_stroke(col, row, target[::-1], wordsearch)
                    right_stroke_forward = check_right_stroke(col, row, target, wordsearch)
                    right_stroke_backward = check_right_stroke(col, row, target[::-1], wordsearch)
                    if (left_stroke_forward or left_stroke_backward) and (right_stroke_forward or right_stroke_backward):
                        total_count += 1

            except IndexError:
                pass

    print(f"Total {target} patterns found: {total_count}")
    return total_count


def check_left_stroke(col, row, target, wordsearch):
    if (wordsearch[row - 1][col - 1] == target[0] and
            wordsearch[row + 1][col + 1] == target[2]):
        return True

def check_right_stroke(col, row, target, wordsearch):
    if (wordsearch[row - 1][col + 1] == target[0] and
            wordsearch[row + 1][col - 1] == target[2]):
        return True


file_path = 'resources/wordsearch.txt'
wordsearch_array = load_wordsearch(file_path)

total_xmas = 0
total_xmas += checkHorizontal("XMAS", wordsearch_array)
total_xmas += checkHorizontal("SAMX", wordsearch_array)
total_xmas += checkVertical("XMAS", wordsearch_array)
total_xmas += checkVertical("SAMX", wordsearch_array)
total_xmas += checkDiagonal("XMAS", wordsearch_array)
total_xmas += checkDiagonal("SAMX", wordsearch_array)
print(f"Total Xmas: {total_xmas}")

total_x_mas = checkXPattern("MAS", wordsearch_array)
print(f"Total count Xs: {total_x_mas}")
