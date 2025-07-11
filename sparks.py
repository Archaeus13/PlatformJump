import pygame
import sys

class Hero(pygame.sprite.Sprite):
    # 主角类
    def __init__(self, x, y, weapon = 'energy', ooze = False, life=3, energy = 5):
        self.max_life = life
		self.life = life
		self.hurt = 0
		self.max_energy = energy
		self.energy = energy
		self.runa = False
		self.rund = False
		self.x_vel = 0  #移动距离
		self.y_vel = 0
		self.face_right = -1
		self.if_left_block = False
		self.if_right_block = False
		self.if_up_block = False
		self.if_down_block = False
		self.push = 0
		self.run_image = 0
		self.rect = pygame.Rect(x,y,12,34) # 坐标+尺寸
		self.x = float(x)
		self.y = float(y)  # x，y就是专门给rect.x弄成小数形式的
		self.init_weapon(weapon)

    def check_event(self, event):
		'''响应键盘'''
		#包括基础运动方式：向左滚动，向右滚动，跳跃，控制平动（？）'''
        pass
    
	def current_shape(self):
		'''返回当前形状和角度'''
		pass

	def update_location(self):
		'''更新主角位置'''
		pass

	def draw_life(self, screen):
		'''绘制生命条'''
		#生命条决定还能活多久
		pass

	def draw_energy(self, screen):
		'''绘制能量条'''
		#能量条决定能否攻击
		pass

	def draw(self, screen):
		'''绘制主角'''
		pass

	def check_update_draw(self, spikes, blocks, screen):
		'''更新状态并返回是否存活'''
		pass

	def if_haunted(self):
		'''判断是否被小鬼附身'''
		pass

	def current_home(self):
		'''返回当前存档点'''
		pass

	def if_home(self, home):
		'''判断是否存档'''
		pass
	
	def if_bounced(self, kinetic_wall):
		'''判断是否与弹性墙发生碰撞'''
		pass

	def if_pierced(self, tightr_rope):
		'''判断是否被尖刺割伤'''
		pass

	def if_pick_pieces(self, pieces):
		'''判断是否拾取碎片'''
		pass
	

	def if_door(self, door):
		'''判断是否通过门'''
		pass

	def if_pick_fruit(self, fruit):
		'''判断是否拾取果实'''
		pass

	def if_pick_chocolate(self, chocolate):
		'''判断是否拾取巧克力'''

	


class Ooze(Hero):
	'''粘液，主角可以发射粘液'''
	def __init__(self, x, y):
		pass


	def check_event(self, event):
		'''响应键盘'''
		#一个键控制粘液出现，另一个键控制粘液消失；写出粘液状态下额外的动作
		pass

	def check_ooze(self,ooze):
		'''检查此时是否有粘液'''
		pass

class Brake(Hero):
	'''刹车器，主角可以刹车，并不出现在地图上'''
	def __init__(self):
		pass

	def check_event(self, event):
		'''响应键盘'''
		#一个键控制刹车器刹车，另一个键控制刹车器加速；写出刹车状态下额外的动作
		pass

	def check_brake(self,brake):
		'''检查此时是否有刹车器'''
		pass

	def if_brake(self,brake):
		'''判断是否有刹车器,主角会进行减速'''
		pass


class Block(pygame.Rect):
	'''用来垒成墙的几何图形'''
	def __init__(self, x, y, width, height, name = '', portable = 0, hidden = False):
		'''初始化碰撞箱与其初始位置、大小'''
		pass

	def draw(self, screen, color = ()):
		'''在屏幕上绘制墙壁'''
		pass

	def update(self):
		'''更新状态'''
		pass

class Home(Block):
	'''存档点，主角经过时自动存档，下次死掉时从这里复活'''
	def __init__(self, x, y):
		pass

class KineticWall(Block):
	'''弹性墙，主角可以借助其弹性'''
	def __init__(self, x, y, width, height, name = '', portable = 0, hidden = False, bounce = False):
		pass

	def update(self):
		'''更新状态'''
		pass

	def if_bounce(self, hero):
		'''判断是否与主角发生弹性碰撞'''
		pass

class VKineticWall(KineticWall):
	'''易碎弹性墙'''
	def __init__(self, x, y, width, height, name = '', portable = 0, hidden = False, bounce = False):
		pass

	def update(self):
		'''更新状态'''
		pass

	def if_broken(self, hero):
		'''判断是否被主角打碎'''
		pass

class TightrRope(Block):
	'''钢丝，会割碎主角'''
	def __init__(self, x, y, width, height, name = '', portable = 0, hidden = False):
		pass

	def update(self):
		'''更新状态'''
		pass

	def if_pierce(self, hero):
		'''判断是否把主角割碎'''
		pass

	
class Pieces(Block):
	'''碎片，会被主角拾取,最终拼成花/火'''
	def __init__(self, x, y, width, height, name = '', portable = 0, hidden = False):
		pass

	def update(self):
		'''更新状态'''
		pass

	def if_picked(self, hero):
		'''判断是否被主角拾取'''
		pass

class Track(Pieces):
	'''记录此时有多少碎片,作为侧栏出现在一角'''
	def __init__(self, x, y, width, height):
		pass

	def update(self):
		'''更新状态'''
		pass







class React():
	'''可互动的物品'''
	def __init__(self, x, y, name, near = 20):
		'''初始化与其初始位置'''

	def draw(self, screen):
		'''绘制物品'''

	def if_near(self, hero):
		'''判定靠近'''

class Bullet(React):
	'''子弹'''
	def __init__(self, x, y, x_bullet, y_bullet, speed = 10, near = 20, if_enemy = False):

class Ghost(React):
	'''大鬼，会追着主角跑，主角可以杀死'''
	def __init__(self, x, y,x_ghost , y1, near=20, ghost_life = 3):
		pass

	def react(self, hero, screen):
		'''靠近时'''
		pass

	def near_bullet(self,bullet):
		'''靠近子弹时'''
		pass

	def check_update_draw(self, screen):
		'''更新状态并返回是否存活'''
		pass


class Spirit(React):
	'''小鬼，主角无法杀死，会粘到主角身上，小鬼上身时地图上会出现更多红果实,小鬼上身一段时间会自动下身'''
	def __init__(self, x, y, x_spirit, y_spirit, near = 20, spirit_life = 3):
		pass

	def if_haunt(self, hero, screen):
		'''判断是否在附身主角'''
		pass



class Fruit(React):
	'''果实，主角可以吃掉，小鬼上身时会出现更多果实'''
	def __init__(self, x, y, index, near = 20, if_spirit = False, invisible = False):
		pass

	def react(self, hero, screen):
		'''靠近时'''
		pass

	def eaten(self, hero, screen):
		'''吃掉时'''
		pass

class Note(Fruit):
	'''果子计数牌，不时闪现，显示现在吃了几个果子'''
	def __init__(self, x, y, near = 40):
		pass

	def react(self, fruit, screen):
		'''果子被吃时展示文字'''
		pass




class Chocolate(React):
	'''巧克力，主角可以吃掉，可以增加主角的能量条'''
	def __init__(self, x, y, index, near = 20, if_spirit = False, invisible = False):
		pass

	def react(self, hero, screen):
		'''靠近时'''
		pass

	def eat(self, hero, screen):
		'''吃掉时'''
		pass


class Door(React):
	'''门,通往地图的下一面'''
	def __init__(self, x, y, near = 10):
		pass

	def react(self, hero, screen):
		'''靠近时'''
		pass

	def if_near_hero(self, hero):
		'''判断是否靠近主角'''
		pass



