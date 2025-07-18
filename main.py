from utils import *
from hero import Hero
from map import Map

pygame.init()

filename = "save.txt"

maps, map_now, hero = read_storage(filename)

before = []

# 进入游戏循环

# 一张大图 写按 E 继续 继续以后就按初始存档来

# 游戏中循环
while True:
    # 控制帧数
    operation = read_keyboard("event")
    if operation[6] == 'P':
        while True:
            # 放暂停画面 按 P 继续 按 esc 退出
            pass
    else:
        if_alive = hero.update(operation, map_now, before)
        before = maps[map_now].update(hero)
        if not if_alive or operation[5] == 'R':
            maps, map_now, hero = read_storage(filename)
            continue
        if before[0]: # before 第一位代表是否存档
            save_now(filename, maps, map_now, hero)
        # before 里面还有位表示结局
