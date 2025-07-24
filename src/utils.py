import pygame
from hero import Hero
from map import Map

def read_keyboard(event):
    '''读取键盘输入转化为字符串
    第一位 W/S/A/D/  表示方向或不动
    第二位 K/ 表示是否跳跃
    第三位 E/ 表示是否交互
    第四位 C/ 表示切换道具
    第五位 X/ 表示使用道具
    第六位 R/ 表示返回存档点
    第七位 P/ 表示暂停/继续'''
    pass

def save_now(filename : str, maps : list[Map], map_now : int, hero : Hero):
    '''存档入文件'''
    pass

def read_storage(filename : str) -> tuple[list[Map], int, Hero]:
    '''从文件读出当前在哪张地图'''
    map_now = 0
    maps = []
    for i in range(60):
        maps.append(Map("save.txt", i))
    hero = Hero(filename)
    
    return maps, map_now, hero