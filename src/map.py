from hero import Hero
from pygame.sprite import Sprite
import pygame

class Map:
	def __init__(self, filename : str, index):
		# 注意区分是否过图刷新

		self.blocks = []
		self.ooze_blocks = []
		self.bounce_blocks = []
		self.tight_ropes = []
		self.spikes = []

		self.devils = []
		self.ghosts = []

		self.switches = []
		self.gates = []

		self.doors = []

		self.fruits = []

		self.home = None

		self.tombstones = []

		self.chocolates = []

		self.pieces = []

	def update(self, hero : Hero):
		# 所有 block 更新状态
		for block in self.blocks:
			block.update()

		# 所有可互动物 react
		if self.home is not None:
			if self.home.react(self, hero):
				# 需要传输存档信号
				pass

		# 所有收集物判定收集
		
		before = []

		# react、拾取 并生成返回值 例如主角传送 下一张地图的编号等内容
		return before

	def draw(self):
		for block in self.blocks:
			block.draw()

class Block(pygame.Rect):
	'''砖块类'''

	def __init__(self):
		# 是否易碎
		self.if_easy_to_break = False
		self.if_move = False
		self.type = "N"
		# N 为普通墙
		# B 为弹性墙
		# O 为粘液墙
		# T 为钢丝
		# S 为刺

	def update_break(self):
		'''更新是否存在'''
		pass

	def update_pos(self):
		'''更新位置'''
		pass

	def update(self, hero : Hero):
		'''根据类型与 hero 中的信息, 更新位置与是否存在'''
		pass

	def draw(self):
		'''绘制'''
		pass

class React(pygame.Rect):
	'''可互动物基类'''

	# 存档点、门、碎片
	def __init__(self):
		self.pos = [0, 0]

	def if_near(self, hero: Hero):
		'''判断是否可以互动'''
		pass

	def if_react(self, hero : Hero):
		'''根据 Hero 是否互动 与 位置关系 判断是否发生互动'''
		if not self.if_near(hero):
			return False
		pass

	def draw(self):
		'''在靠近时在头上显示可以按 E'''
		# 需要调用

class Home(React):
	'''存档点'''
	def __init__(self):
		pass

	def react(self, hero : Hero):
		'''互动'''
		# 可以不输入 map, 只发出信号 在外界存档
		pass

class Pieces(React):
	'''碎片'''
	def __init__(self):
		self.show = True

	def react(self):
		'''互动'''
		# 未收集时方可互动
		self.show = False

	def draw(self):
		'''绘制'''
		if self.show:
			super().draw()

class Door(React):
	'''存档点'''
	def __init__(self):
		pass

	def react(self):
		'''互动'''
		# 返回新的位置与地图序号
		pass

class Collect(pygame.Rect):
	'''自动收集物基类'''
	def __init__(self):
		self.show = True # show 代表存在

	def if_reach(self, hero : Hero):
		'''判定是否吃到'''
		pass
		# 若吃到 需要改变 hero 的库存量

	def draw(self):
		'''绘制'''
		if not self.show:
			return
		pass

class Chocolate(Collect):
	'''回复道具使用次数'''
	def __init__(self):
		pass

class Fruit(Collect):
	'''收集物水果'''
	def __init__(self):
		pass

class Devil(Collect):
	'''小鬼'''
	def __init__(self):
		self.vanish_time = 0 # 变化到 0 时出现 消失后开始从某个数减少

class Ghost(Sprite):
	'''大鬼类'''
	def __init__(self):
		pass

	def update(self):
		'''更新大鬼位置'''
		# 追逐主角
		pass

	def check_update(self):
		'''更新状态'''
		# 检测是否被子弹击中
		pass
	
	def draw(self, screen):
		'''绘制大鬼'''
		pass


