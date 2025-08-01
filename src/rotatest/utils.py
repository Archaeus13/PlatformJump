import pygame


def read_keyboard(keys):
    '''读取键盘输入转化为字符串
    第一位 W/S/A/D/  表示方向或不动
    第二位 K/ 表示是否跳跃
    第三位 E/ 表示是否交互
    第四位 C/ 表示切换道具
    第五位 X/ 表示使用道具
    第六位 R/ 表示返回存档点
    第七位 P/ 表示暂停/继续'''
    
    operation = ""
    if keys[pygame.K_a]:
        operation += "A"

    if keys[pygame.K_d]:
        operation += "D"

    if keys[pygame.K_w]:
        operation += "W"

    if keys[pygame.K_k]:
        operation += "K"

    if keys[pygame.K_s]:
        operation += "S"

    if keys[pygame.K_e]:
        operation += "E"

    if keys[pygame.K_c]:
        operation += "C"

    if keys[pygame.K_x]:
        operation += "X"

    if keys[pygame.K_r]:
        operation += "R"

    if keys[pygame.K_p]:
        operation += "P"

    return operation
    

