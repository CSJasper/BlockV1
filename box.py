import pygame
from math import sqrt
from random import randint


class Box:
    SPEED = 10
    def __init__(self, pos_offsets: dict, square_length: int, color: tuple, surface: pygame.Surface, debug=False):
        self.pos_offsets = pos_offsets
        self.length = square_length
        self.tile_num = int(sqrt(len(pos_offsets.keys())))
        self.current_tile = (0, 0)
        self.pos_x = pos_offsets[self.current_tile][0]
        self.pos_y = pos_offsets[self.current_tile][1]
        self.color = color
        self.surface = surface
        
        self.debug_mode = debug


    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.pos_x, self.pos_y, self.length, self.length))
        '''
        if self.debug_mode:
            print(f'drawn : {(self.pos_x, self.pos_y, self.pos_x + self.length, self.pos_y + self.length)}')'''


    def set_tile_pos(self, tile_x, tile_y):
        assert 0 <= tile_x < self.tile_num and 0 <= tile_y < self.tile_num
        self.current_tile = (tile_x, tile_y)
        self.pos_x, self.pos_y = self.pos_offsets[self.current_tile]
        if self.debug_mode:
            print(f'current tile : {self.current_tile}')
            print(f'current coordinate : {(self.pos_x, self.pos_y)}')
    
    
    def set_color(self, color: tuple):
        self.color = color


class action:
    
    @staticmethod
    def __get_valid_tile_move(obj: Box):
        length = obj.tile_num
        tile_x, tile_y = obj.current_tile
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        next_moves = []
        
        for move_x, move_y in moves:
            if 0 <= tile_x + move_x < length and 0 <= tile_y + move_y < length:
                next_moves.append((tile_x + move_x, tile_y + move_y))
        
        return next_moves
    
    
    @staticmethod
    def move_left(obj: Box):
        tile_x, tile_y = obj.current_tile

        if 0 < tile_y:
            tile_y -= 1
        
        obj.set_tile_pos(tile_x, tile_y)


    @staticmethod
    def move_right(obj: Box):
        length = obj.tile_num
        tile_x, tile_y = obj.current_tile
        
        if tile_y < length - 1:
            tile_y += 1
        
        obj.set_tile_pos(tile_x, tile_y)


    @staticmethod
    def move_down(obj: Box):
        length = obj.tile_num
        tile_x, tile_y = obj.current_tile
        
        if tile_x < length - 1:
            tile_x += 1
        
        obj.set_tile_pos(tile_x, tile_y)


    @staticmethod
    def move_up(obj: Box):
        tile_x, tile_y = obj.current_tile
        
        if 0 < tile_x:
            tile_x -= 1
        
        obj.set_tile_pos(tile_x, tile_y)
    

    @staticmethod
    def move_random(obj: Box):
        next_moves = action.__get_valid_tile_move(obj)
        
        idx = randint(0, len(next_moves) - 1)
        
        obj.set_tile_pos(next_moves[idx][0], next_moves[idx][1])
    
    
    @staticmethod
    def change_color(obj: Box, color: tuple):
        obj.set_color(color)


    class Sequential:
        def __init__(self, *args):
            self.args = args
        
        def __call__(self, obj: Box):
            for arg in self.args:
                arg(obj)
