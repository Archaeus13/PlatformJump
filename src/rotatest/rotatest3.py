from hero import Hero
from utils import *
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()  # Clock对象应在循环外创建
hero = Hero("6S")

font = pygame.font.SysFont('SimSun',32)

# 测试用碰撞块
blocks_in_map = [
    pygame.Rect(0, 550, 1200, 50),    # 地面
    pygame.Rect(200, 500, 200, 50),   
    pygame.Rect(400, 450, 100, 50),
    pygame.Rect(500, 400, 50, 50),
    pygame.Rect(550, 350, 50, 50),
    pygame.Rect(600, 250, 50, 100),
    pygame.Rect(800, 500,150, 50)   
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

    text = font.render('苯案例可见各种神奇效果……', True, (226, 0, 26))
    screen.blit(text, (50, 50))
    
    pygame.display.flip()
    clock.tick(60)  # 控制帧率