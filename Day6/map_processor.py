class MapProcessor:
    def __init__(self, map_file):
        self.map_grid = self.read_map(map_file)
        self.character_pos = self.find_start_position()
        self.character_direction = 3
        self.visited_positions = set()
        self.visited_positions.add(tuple(self.character_pos))
        self.steps = 0

    def read_map(self, map_file):
        with open(map_file, 'r') as f:
            return [list(line.strip()) for line in f.readlines()]

    def find_start_position(self):
        for y, row in enumerate(self.map_grid):
            for x, cell in enumerate(row):
                if cell == '^':
                    return [x, y]
        return [0, 0]

    def is_valid_move(self, x, y):
        if (0 <= x < len(self.map_grid[0]) and 
            0 <= y < len(self.map_grid)):
            if self.map_grid[y][x] == '.' or self.map_grid[y][x] == '^':
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
            if tuple(self.character_pos) not in self.visited_positions:
                self.steps += 1
                self.visited_positions.add(tuple(self.character_pos))
        else:
            self.character_direction = (self.character_direction + 1) % 4
        if not (0 <= x < len(self.map_grid[0]) and 0 <= y < len(self.map_grid)):
            print(f"Game over! Total steps: {self.steps + 1}")
            return False
        return True

    def run(self):
        while self.move_character():
            pass

if __name__ == "__main__":
    map_file = "map.txt"
    game = MapProcessor(map_file)
    game.run()
