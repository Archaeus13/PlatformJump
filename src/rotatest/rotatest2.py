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
    pygame.Rect(400, 450, 500, 100),   #大平台
    pygame.Rect(700, 400, 50, 50)    #小障碍
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

    text = font.render('试试在高台上不按跳跃键————你的主角会自己跃过障碍吗？', True, (226, 0, 26))
    screen.blit(text, (50, 50))
    text2 = font.render('苯测试样例中主角表现极不稳定……', True, (226, 0, 26))
    screen.blit(text2, (50, 100))
    
    pygame.display.flip()
    clock.tick(60)  # 控制帧率