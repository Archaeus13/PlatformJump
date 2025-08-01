from hero import Hero
from utils import *
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()  # Clock对象应在循环外创建
hero = Hero("6S")

# 测试用碰撞块
blocks_in_map = [
    pygame.Rect(0, 550, 1200, 50),    # 地面
    pygame.Rect(500, 400, 50, 150),   # 中间障碍物
    pygame.Rect(900, 300, 50, 250)    # 右侧高台
]

while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        keys = pygame.key.get_pressed() 
        operation = read_keyboard(keys)
        print("------------------------------------------", operation, "-------------------------------------------")
        hero.update(operation, blocks_in_map) 
    
    # 无输入时也更新一下
    hero.update("", blocks_in_map)
    
    # 渲染
    screen.fill((255, 255, 255))
    for block in blocks_in_map:
        pygame.draw.rect(screen, (70, 70, 90), block)
    
    hero.draw(screen)  
    
    pygame.display.flip()
    clock.tick(60)  # 控制帧率