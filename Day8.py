import math


def reduce_direction_vector(dr, dc):
    g = math.gcd(dr, dc)
    return dr // g, dc // g


def mark_line_points(r_start, c_start, dr_prime, dc_prime, rows, cols, antinodes):
    extend_in_direction(r_start, c_start, dr_prime, dc_prime, rows, cols, antinodes)
    extend_in_direction(r_start, c_start, -dr_prime, -dc_prime, rows, cols, antinodes)


def extend_in_direction(r, c, dr, dc, rows, cols, antinodes):
    while 0 <= r < rows and 0 <= c < cols:
        antinodes.add((r, c))
        r += dr
        c += dc


def process_frequency(freq, positions, rows, cols, antinodes):
    if len(positions) < 2:
        return
    for i in range(len(positions)):
        r1, c1 = positions[i]
        for j in range(i + 1, len(positions)):
            r2, c2 = positions[j]
            dr = r2 - r1
            dc = c2 - c1
            dr_prime, dc_prime = reduce_direction_vector(dr, dc)
            mark_line_points(r1, c1, dr_prime, dc_prime, rows, cols, antinodes)


def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    antennas_by_freq = {}
    for r in range(rows):
        for c in range(cols):
            ch = grid[r][c]
            if ch != '.':
                if ch not in antennas_by_freq:
                    antennas_by_freq[ch] = []
                antennas_by_freq[ch].append((r, c))

    antinodes = set()

    for freq, positions in antennas_by_freq.items():
        process_frequency(freq, positions, rows, cols, antinodes)

    return len(antinodes)


with open('resources/antennas.txt', 'r') as f:
    grid = [line.rstrip('\n') for line in f]
result = solve(grid)
print(result)
