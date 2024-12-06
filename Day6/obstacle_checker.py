import copy

class MapProcessor:
    def __init__(self, map_grid):
        self.map_grid = map_grid
        self.character_pos = self.find_start_position()
        self.character_direction = 3
        self.visited_positions = set()
        self.visited_positions.add(tuple(self.character_pos))
        self.steps = 0
        self.total_steps = 0
        self.last_positions = []

    def find_start_position(self):
        for y, row in enumerate(self.map_grid):
            for x, cell in enumerate(row):
                if cell == '^':
                    return [x, y]
        return [0, 0]

    def is_valid_move(self, x, y):
        if 0 <= x < len(self.map_grid[0]) and 0 <= y < len(self.map_grid):
            if self.map_grid[y][x] in ['.', '^']:
                return True
        return False

    def detect_loop(self):
        current_state = (tuple(self.character_pos), self.character_direction)
        self.last_positions.append(current_state)
        if len(self.last_positions) > 500:
            self.last_positions.pop(0)
            if self.last_positions.count(current_state) > 4:
                return True
        return False

    def move_character(self):
        x, y = self.character_pos
        if self.character_direction == 0:
            x += 1
        elif self.character_direction == 1:
            y += 1
        elif self.character_direction == 2:
            x -= 1
        elif self.character_direction == 3:
            y -= 1

        if self.is_valid_move(x, y):
            self.character_pos = [x, y]
            self.total_steps += 1
            if tuple(self.character_pos) not in self.visited_positions:
                self.steps += 1
                self.visited_positions.add(tuple(self.character_pos))
        else:
            self.character_direction = (self.character_direction + 1) % 4

        if not (0 <= x < len(self.map_grid[0]) and 0 <= y < len(self.map_grid)):
            return False

        if self.detect_loop() or self.total_steps > 15000:
            return None
        return True

    def run(self):
        while True:
            result = self.move_character()
            if result is None:
                return True
            if result is False:
                return False

def read_map(map_file):
    with open(map_file, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def check_infinite_loops(map_file):
    original_map = read_map(map_file)
    infinite_loops = 0
    total_positions = sum(row.count('.') for row in original_map)
    checked_positions = 0

    for y, row in enumerate(original_map):
        for x, cell in enumerate(row):
            if cell == '.':
                test_map = copy.deepcopy(original_map)
                test_map[y][x] = '0'
                game = MapProcessor(test_map)
                if game.run():
                    infinite_loops += 1
                    print(f"Found infinite loop at position ({x}, {y})")
                checked_positions += 1
                print(f"Checked {checked_positions}/{total_positions} positions. Infinite loops found: {infinite_loops}")

    print(f"Number of possible spots that result in an infinite loop: {infinite_loops}")

if __name__ == "__main__":
    map_file = "map.txt"
    check_infinite_loops(map_file)
