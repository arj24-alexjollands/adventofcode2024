import pygame
import sys

class MapAnimation:
    def __init__(self, map_file):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 24)
        self.map_grid = self.read_map(map_file)
        self.TILE_SIZE = min(800 // len(self.map_grid[0]), 600 // len(self.map_grid))
        self.SCREEN_WIDTH = len(self.map_grid[0]) * self.TILE_SIZE
        self.SCREEN_HEIGHT = len(self.map_grid) * self.TILE_SIZE
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Map Movement Animation")
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.character_image = pygame.image.load("christmas-elf-guard.png")
        self.character_image = pygame.transform.scale(self.character_image, (self.TILE_SIZE, self.TILE_SIZE))
        self.character_pos = self.find_start_position()
        self.character_direction = 3
        self.visited_positions = set()
        self.visited_positions.add(tuple(self.character_pos))
        self.steps = 0
        self.clock = pygame.time.Clock()

    def read_map(self, map_file):
        with open(map_file, 'r') as f:
            return [list(line.strip()) for line in f.readlines()]

    def find_start_position(self):
        for y, row in enumerate(self.map_grid):
            for x, cell in enumerate(row):
                if cell == '^':
                    return [x, y]
        return [0, 0]

    def draw_map(self):
        self.screen.fill(self.WHITE)
        for y, row in enumerate(self.map_grid):
            for x, cell in enumerate(row):
                rect = pygame.Rect(
                    x * self.TILE_SIZE, 
                    y * self.TILE_SIZE, 
                    self.TILE_SIZE, 
                    self.TILE_SIZE
                )
                if cell == '#':
                    pygame.draw.rect(self.screen, self.BLACK, rect)
                elif cell == '^':
                    pygame.draw.rect(self.screen, self.GREEN, rect)
                elif cell == 'E':
                    pygame.draw.rect(self.screen, self.RED, rect)

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
            pygame.quit()
            sys.exit()

    def draw_step_counter(self):
        step_text = self.font.render(f"Steps: {self.steps}", True, (0, 0, 0))
        self.screen.blit(step_text, (10, 10))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.move_character()
            self.draw_map()
            self.draw_step_counter()
            character_rect = pygame.Rect(
                self.character_pos[0] * self.TILE_SIZE, 
                self.character_pos[1] * self.TILE_SIZE, 
                self.TILE_SIZE, 
                self.TILE_SIZE
            )
            self.screen.blit(self.character_image, character_rect)
            pygame.display.flip()
            self.clock.tick(10)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    map_file = "map-small.txt"
    game = MapAnimation(map_file)
    game.run()
