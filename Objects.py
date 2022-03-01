import pygame
import os

STAR = pygame.image.load(os.path.join('Assets/star', 'star.png'))


class Object:
    def __init__(self, image: pygame.image, pos_offsets: dict, screen_width: int):
        self.SCREEN_WDITH = screen_width
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = screen_width

    def draw(self, screen: pygame.surface):
        screen.blit(self.image, self.rect)


class Star(Object):
    def __init__(self, pos_offsets: dict, screen_width: int):
        super().__init__(STAR, pos_offsets, screen_width)


class Map:
    UNINT_OFFSET = 13.0
    def __init__(self, rect: tuple, color: tuple, line_width: int, map_size: int, box_offsets: dict, surface: pygame.Surface):
        self.surface = surface
        self.rect = rect
        self.box_offsets = box_offsets
        self.color = color
        self.line_width = line_width
        self.map_size = map_size
        self.top_x, self.top_y, self.bottom_x, self.bottom_y = rect
        self.box_width = abs(self.bottom_x - self.top_x)
        self.box_height = abs(self.bottom_y - self.top_y)
        self.stride_x = self.box_width / map_size
        self.stride_y = self.box_height / map_size
        self.map = []

    def draw(self):
        line_start_y = self.top_y + self.stride_y
        line_start_x = self.top_x
        line_end_y = self.top_y + self.stride_y
        line_end_x = self.top_x + self.box_width
        
        for i in range(self.map_size):
            pygame.draw.line(self.surface, self.color, (line_start_x, line_start_y), (line_end_x, line_end_y), width= 1)
        
            line_start_y += self.stride_y
            line_end_y += self.stride_y
        
        line_start_x = self.top_x + self.stride_x
        line_start_y = self.top_y
        line_end_x = self.top_x + self.stride_x
        line_end_y = self.top_y + self.box_height
        
        for i in range(self.map_size):
            pygame.draw.line(self.surface, self.color, (line_start_x, line_start_y), (line_end_x, line_end_y),width= 1)

            line_start_x += self.stride_x
            line_end_x += self.stride_x
        

    def fill(self, coord: tuple, color: tuple, screen: pygame.surface):
        x_pos, y_pos = self.box_offsets[coord]
        pygame.draw.rect(screen, color, (x_pos - Map.UNINT_OFFSET, y_pos - Map.UNINT_OFFSET, self.stride_x, self.stride_y))
    
    def read_map(self, path=None):
        assert path is not None
        with open(path, 'r') as f:
            for i in range(self.map_size):
                self.map.append(f.readline().split())
        assert len(self.map) == self.map_size
    
    def apply_map(self):
        if len(self.map) == 0:
            print('There is nothing to apply')
            return
        
        for i in range(self.map_size):
            for j in range(self.map_size):
                if self.map[i][j] == '9':
                    self.fill((i, j), (0, 0, 0), self.surface)
