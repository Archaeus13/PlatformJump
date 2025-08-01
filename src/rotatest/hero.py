import pygame
vec = pygame.math.Vector2
import time

from pygame.sprite import Sprite
from utils import *

class HeroShape():
    '''主角形状类 处理碰撞检测与绘制逻辑'''
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rot = 0  # 当前旋转角度

        self.type = "6S" #【测试用】
        self.original_image = pygame.image.load("6S_test.png")  # 原始图像
        self.original_image = pygame.transform.scale(self.original_image,(50,50)) # 调整尺寸
        self.image = self.original_image  # 旋转后的图像
        # #用一个列表表示主角的形态，6个数表示6条边，1为直边0为弧边
        self.edges = [1, 1, 1, 1, 1, 1]  # 【测试用】
        # 当前着地边的编号
        self.index = 0  

        self.rect = self.image.get_rect()
        #self.original_rect = self.image.get_rect()
        #top = self.original_rect.top -10
        #self.rect = pygame.Rect(self.original_rect.left, top,
                                #self.original_rect.width, self.original_rect.height)
        
        
        

    def update_image(self):
        """更新旋转后的图像"""
        self.image = pygame.transform.rotate(self.original_image, self.rot)
        # 保持中心点不变
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def collides_with(self, rect):
        """将主角处理成矩形做碰撞检测"""
        return self.rect.colliderect(rect)
    
    def draw(self,screen):
        '''绘制主角形状'''
        screen.blit(self.image, self.rect)

class Bullet():
	'''主角的枪发出的子弹'''
	def __init__(self):
		pass

	def update(self):
		'''更新位置'''
		pass

	def draw(self):
		pass


class Hero(Sprite):
    '''主角类 '''
    def __init__(self, filename: str):
        super().__init__()
        
        self.items = {
            "ooze": False,  # 粘液
            "brake": False,  # 刹车器
            "gun": False,    # 枪
        }
        self.item_now = -1
        self.if_spirit = False
        
        self.shape = HeroShape()
        
        self.fruits = 0
        self.pieces = [0] * 20
        
        self.bullets = []
        self.bullets_now = 0
        
        self.is_jumping = False
        self.is_falling = False
        self.if_reacting = False
        self.is_rotating = False  # 是否正在旋转
        self.rot_steps = 0     # 当前旋转步数
        self.rot_direction = 0 # 旋转方向，1左，-1右
        self.omiga = 10    # 每步旋转度数（每次按键转满60度，分6步进行，每10度做一次碰撞检测）
        
        
        self.velx = 0
        self.vely = 0
        self.vel = vec(self.velx, self.vely)
        self.acc_x = 0
        self.acc_y = 2
        self.max_vy = 20
        self.jump_force = -20
        
        # 初始化位置【测试用】
        self.shape.rect.center = (50, 0) #地面高度550；主角尺寸50,50



    def update(self, operation: str, blocks_in_map = []):
        '''主更新函数'''
        #print("update")
        

        self.check_event(operation)
        print("x = ", self.shape.rect.centerx)
        print("y =", self.shape.rect.centery)
        self.update_rotation(blocks_in_map)
        print("x = ", self.shape.rect.centerx)
        print("y =", self.shape.rect.centery)
        self.update_vely(blocks_in_map)

        

    def check_event(self, operation):
        '''处理输入指令'''
        #print("check_event")
        #if self.is_rotating:  # 旋转过程中不响应新输入
            #return
            
        
        if "A" in operation:
            self.rot_left()
        elif "D" in operation:
            self.rot_right()
        if "K" in operation:
            self.jump()


    # 转动部分
    def rot_left(self):
        '''向左旋转的准备工作'''
        print("rot_left")
        if not self.is_rotating: #确保当前不在旋转状态，才能开启新的旋转
            self.is_rotating = True
            self.rot_steps = 0
            self.rot_direction = 1
            self.velx = -3
            # 每旋转60度，移动水平移动距离24；分成6步后，每步移动距离为4
            

    def rot_right(self):
        '''向右旋转的准备工作'''
        print("rot_right")
        if not self.is_rotating:
            self.is_rotating = True
            self.rot_steps = 0
            self.rot_direction = -1
            self.velx = 3
            

    def update_rotation(self, blocks_in_map):
        '''处理分步旋转  每10度一步做碰撞检测'''
        # 暂时认为地图中所有砖块都在map文件中被列在一个叫blocks_in_map的列表里，可以遍历
            
        # 保存当前状态，若某次检测到碰撞，则回到该状态
        if self.is_rotating:
            current_state = self.get_state()
            self.rot_steps = 0
            current_y = self.shape.rect.y
            #current_x, current_y = current_state['pos']
            print("original_y =", current_y)
            while self.rot_steps <= 6:
                # 执行一小步旋转和移动
                self.shape.rot = (self.shape.rot + self.rot_direction * self.omiga) % 360
                self.shape.rect.centerx += self.velx
                self.shape.rect.centery = current_y
                print("actual_y =", self.shape.rect.centery)
                print("current_y =", current_y)
            
                #self.shape.update_image()
                
                # 碰撞检测
                if not self.if_movable(blocks_in_map):
                    print("unmovable")
                    self.back_to_state(current_state)
                    self.stop_rotation()
                    return
                    
                self.rot_steps += 1
                
                # 检查是否完成60度旋转
                if self.rot_steps == 6:
                    self.shape.update_image()
                    self.complete_rotation()
                    return

    def complete_rotation(self):
        '''完成完整60度旋转后的处理'''
        self.is_rotating = False
        # 更新着地面的index
        if self.rot_direction == 1:  # 向左转
            if self.shape.index <= 4:
                self.shape.index += 1
            elif self.shape.index == 5:
                self.shape.index = 0
        else:  # 向右转
            if self.shape.index >= 1:
                self.shape.index -= 1
            elif self.shape.index == 0:
                self.shape.index = 5
        self.velx = 0

    def stop_rotation(self):
        '''中止旋转'''
        self.is_rotating = False
        self.velx = 0
        self.rot_steps = 0
        


    def if_movable(self, blocks_in_map):
        '''检查当前移动是否有效'''
        for block in blocks_in_map:
            if self.shape.collides_with(block):
                return False
        #if self.is_falling:
            #if self.on_ground:
                #return False
        return True

# 竖直方向基础运动
    def update_vely(self, blocks_in_map):
        '''计算竖直速度'''
        if self.on_ground(blocks_in_map):
            if self.is_jumping == False or self.is_falling == True:
                self.vely = 0
            acc_y = 0
            self.is_falling = False
            self.is_jumping = False

        else:
            acc_y = self.acc_y
            self.is_falling = True

        if self.vely < self.max_vy:
            self.vely += acc_y
        else:
            self.vely = self.max_vy

        self.shape.rect.y += self.vely
        print("acc_y = ", acc_y)
        print("vy = ", self.vely)
        
    def on_ground(self, blocks_in_map):
        '''检测是否在地面上'''
        test_rect = self.shape.rect.copy()
        test_rect.bottom += 2
        for block in blocks_in_map:
            if block.left <= test_rect.right and block.right >= test_rect.left and block.top <= self.shape.rect.bottom and test_rect.colliderect(block):
                self.shape.rect.centery = block.top - 0.5*self.shape.rect.height
                print("on_ground, test_rect.bottom =", test_rect.bottom, "height =", self.shape.rect.height)
                return True
        print("not on_ground, test_rect.bottom =", test_rect.bottom)
        return False
        

    def jump(self):
        '''跳跃'''
        print("jump")
        if not self.is_jumping:  # 用来限制二段跳
            self.vely = self.jump_force
            self.is_jumping = True


# 关于状态    
    def get_state(self):
        '''获取当前状态'''
        return {
            'rect': self.shape.rect.copy(),
            'pos': (self.shape.x, self.shape.y),
            'rot': self.shape.rot,
            'index': self.shape.index,
            'vel': self.vel.copy()
        }
        

    def back_to_state(self, state):
        '''回到之前的状态'''
        print("back_to_state")
        self.shape.rect = state['rect']
        self.shape.x, self.shape.y = state['pos']
        self.shape.rot = state['rot']
        self.shape.index = state['index']
        self.vel = state['vel']

    
# 关于绘制
    def draw(self, screen):
        '''绘制主角相关'''
        self.draw_life(screen)
        self.draw_fruits(screen)
        self.shape.draw(screen)
        for bullet in self.bullets:
            self.bullet.draw(screen) # 注意可能需要从 bullets 中删除 bullet
        self.draw_things(screen)

    def draw_life(self, screen):
        '''绘制生命条'''
        pass

    def draw_fruits(self, screen):
        '''绘制水果面板'''
        pass

    def draw_things(self, screen):
        '''绘制主角拿着的道具'''
        pass