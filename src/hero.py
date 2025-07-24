import pygame
from map import Map
from pygame.sprite import Sprite
from utils import *

class HeroShape():
	'''主角形状类 处理碰撞检测与绘制逻辑'''
	def __init__(self):
		self.x = 0
		self.y = 0
		self.rot = 0

		self.type = "3B2S"

	def update(self):
		pass

	def collides_with(self, rect: pygame.Rect):
		'''检测与另一个东西是否碰撞'''
		pass

	def draw():
		'''绘制形状'''
		# 考虑直接绘制
		pass

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
	'''主角类 为一个会平动和转动的小球'''
	def __init__(self, filename : str):
		super().__init__()

		self.items = {
			"ooze": False,  # 是否有粘液
			"brake": False,  # 是否有刹车器
			"gun": False, # 是否有枪
		}
		
		self.item_now = -1
		self.if_spirit = False

		self.shape = HeroShape()

		self.fruits = 0
		self.pieces = [0] * 20

		self.bullets = []
		self.bullets_now = 0

		self.if_reacting = False

	def update(self, operation : str, map: Map, before):
		'''根据输入与地图更新自身位置'''
		'''返回值应包含是否死亡'''

		# 根据 before 进行状态调整

		# 检测当前撞墙状态

		# 根据输入与当前状态进行尝试移动

		# 移动应由接触点 + 转速 确定

		# 检测墙 生成真实移动 (与是否撞刺) 并更新状态

		# 操作道具

		pass

	def draw(self):
		'''绘制主角相关'''
		self.draw_life()
		self.draw_fruits()
		self.shape.draw()
		for bullet in self.bullets:
			self.bullet.draw() # 注意可能需要从 bullets 中删除 bullet
		self.draw_things()

	def draw_life(self, screen):
		'''绘制生命条'''
		pass

	def draw_fruits(self, screen):
		'''绘制水果面板'''
		pass

	def draw_things(self, screen):
		'''绘制主角拿着的道具'''
		pass