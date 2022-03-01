from turtle import back
import pygame
from box import Box
from Objects import Map

import importlib


def draw_tile(surface, color, rect_pos, line_width, tile_per_length):
    top_x, top_y, bottom_x, bottom_y = rect_pos
    box_width = abs(bottom_x - top_x)
    box_height = abs(bottom_y - top_y)
    pygame.draw.rect(surface, color, rect_pos, line_width)
    stride_x = box_width / tile_per_length
    stride_y = box_height / tile_per_length
    
    line_start_y = top_y + stride_y
    line_start_x = top_x
    line_end_y = top_y + stride_y
    line_end_x = top_x + box_width
    
    for i in range(tile_per_length):
        pygame.draw.line(surface, color, (line_start_x, line_start_y), (line_end_x, line_end_y), width= 1)
        
        line_start_y += stride_y
        line_end_y += stride_y
    
    line_start_x = top_x + stride_x
    line_start_y = top_y
    line_end_x = top_x + stride_x
    line_end_y = top_y + box_height
    
    for i in range(tile_per_length):
        pygame.draw.line(surface, color, (line_start_x, line_start_y), (line_end_x, line_end_y),width= 1)

        line_start_x += stride_x
        line_end_x += stride_x


def get_box_offsets(rect_pos, tiles_per_length):
    top_x, top_y, bottom_x, bottom_y = rect_pos
    box_width = abs(bottom_x - top_x)
    box_height = abs(bottom_y - top_y)

    stride_x = box_width / tiles_per_length
    stride_y = box_height / tiles_per_length 

    box_offsets = dict()
    UNIT_OFFSET = 13.0
    box_offset_x, box_offset_y = UNIT_OFFSET, UNIT_OFFSET
    for i in range(tiles_per_length):
        box_offset_x = UNIT_OFFSET
        for j in range(tiles_per_length):
            box_offsets[(i, j)] = (box_offset_x, box_offset_y)
            box_offset_x += stride_x
        box_offset_y += stride_y
    
    return box_offsets


pygame.init()

window_size = [640, 640]
screen = pygame.display.set_mode(window_size)

title = 'Move Block!'
pygame.display.set_caption(title)

# 게임 내 필요한 설정
clock = pygame.time.Clock()

###############     COLORS      ##################
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 100, 100)
##################################################

###############     TILES       ##################
TILE_POS = (0, 0, 640, 640)
TILE_NUM_PER_LINE = 4
TILE_SIZE = 135
##################################################

###############     STATE       ##################

##################################################

offsets = get_box_offsets(TILE_POS, TILE_NUM_PER_LINE)
red_box = Box(offsets, TILE_SIZE, RED, screen, debug=True)
actions = None
get_actions = None
module = None
background = Map(TILE_POS, BLACK, 5, TILE_NUM_PER_LINE, offsets, screen)
background.read_map('maps/sample.txt')

# main event
sb = 0
while sb == 0:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sb = 1
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                if actions is None:
                    print('You should complete your code and load first!')
                    continue
                if len(actions) != 0:
                    actions[0](red_box)
                    actions.pop(0)
                else:
                    print('There is no more commands!')
            elif event.key == pygame.K_l:
                if get_actions is None:
                    module = importlib.import_module('move')
                else:
                    module = importlib.reload(module)
                get_actions = module.get_actions
                actions = get_actions()
                print('Loaded!')
            elif event.key == pygame.K_u:
                # unload
                actions = None
                print('unloaded sucessfully!')
            elif event.key == pygame.K_q:
                sb = 1

    screen.fill(WHITE)
    
    # draw_tile(screen, BLACK, TILE_POS, 5, TILE_NUM_PER_LINE)
    background.draw()
    background.apply_map()
    red_box.draw()

    pygame.display.flip()

pygame.quit()


