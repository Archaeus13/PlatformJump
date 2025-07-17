import pygame
from pygame.sprite import Sprite
import sys

#主角部分
class Hero(Sprite):
	'''主角类,为一个会平动和转动的小球'''
	def __init__(self, x, y, weapon = 'hand', ooze = False, brake = False,life=3, energy = 5):
		super().__init__()
		self.max_life = life
		self.life = life
		self.hurt = 0
		self.max_energy = energy
		self.energy = energy
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.face_right = -1
		self.if_left_block = False
		self.if_right_block = False
		self.if_up_block = False
		self.if_down_block = False
		self.push = 0
		self.rect = pygame.Rect(x,y,12,34) # 坐标+尺寸
		self.x = float(x)
		self.y = float(y)  # x，y就是专门给rect.x弄成小数形式的
		self.init_weapon(weapon)

		self.items = {
			"fruit": 0,  # 红果实数量
			"chocolate": 0,  # 巧克力数量
			"pieces": 0,  # 碎片数量
			"ooze": 0,  # 是否有粘液
			"brake": 0,  # 是否有刹车器
		}

	def check_event(self, event):
		'''响应键盘'''
		#包括基础运动方式：向左滚动，向右滚动，跳跃，平动，射击，发射粘液，刹车
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
		pass


class Shape:
    '''主角形状类，处理碰撞检测逻辑'''
    def __init__(self):
        '''初始化形状'''
        pass

    def update_position(self, x: float, y: float):
        """更新形状位置"""
        pass

    def collides_with(self, other):
        """检测与另一个东西是否碰撞"""
        pass



class Bullet(pygame.Rect):
	'''子弹'''
	def __init__(self, x, y, x_bullet, y_bullet, speed = 10, near = 20, if_enemy = False):
		'''初始化飞行物'''
		pass

	def update(self):
		'''更新飞行物位置'''
		pass

	def draw(self, screen):
		'''绘制飞行物'''
		pass




#地图部分
class Map:
    '''地图类：管理多个小地图实例并处理切换'''
    def __init__(self,hero:Hero):
        # 存储所有小地图实例
        self.mini_maps = []  # 每个元素是一个小地图的配置
        self.map_index = 1  # 当前活动小地图的索引

        self.hero = hero  # 主角实例
        self.items = {
			"home":{}, # 存档点
			"door":{}, # 门
            "fruit": 0,  # 果实数量
            "chocolate":0,  # 巧克力数量
			"pieces": 0,  # 碎片数量            
			"Block": None,  # 可移动的方块
			"KineticWall": None,  # 弹性墙
			"VKineticWall": None,  # 易碎弹性墙
			"TightrRope": None,  # 钢丝
			"Ooze": None,  # 粘液
			"Brake": None,  # 刹车器			
			"Ghost": None,  # 大鬼
			"Devil": None,  # 小鬼
        }
    
    def switch_to_map(self, map_index, home:Home):
        '''切换到指定索引的小地图'''
        if 0 <= map_index < len(self.mini_maps):
            # 保存当前小地图的临时状态
            self.save_current_mini_map_state()
            
            # 更新当前小地图索引
            self.current_mini_map_index = map_index
            
            # 加载目标小地图状态
            self.load_mini_map_state(map_index)
            
            # 设置主角位置（从存档点进入）
            
    def save_current_map(self):
        '''保存当前小地图的临时状态'''
        pass
    
    def load_mini_map_state(self, map_index: int):
        """加载指定小地图的状态"""
        pass

    def update(self):
        """更新当前小地图状态"""
        pass
    
    def draw(self, screen: pygame.Surface):
        """绘制当前小地图"""
        pass
	


class Block():
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

class KineticWall(Block):
	'''弹性墙，主角可以借助其弹性'''
	def __init__(self, x, y, width, height, name = '', portable = 0, hidden = False, bounce = False,vulnerable = False):
		pass

	def update(self):
		'''更新状态'''
		pass

	def if_vulnerable(self):
		'''判断是否易碎'''
		pass

	def if_bounce(self, hero):
		'''判断是否与主角发生弹性碰撞'''
		pass

class VKineticWall(Block):
	'''易碎弹性墙'''
	def __init__(self, x, y, width, height, name = '', portable = 0, hidden = False, bounce = False,vulnerable = True):
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


class Item:
	'''道具基类'''
	def __init__(self, name: str, icon_path: str = None):
		pass

class Fruit(Item):
	'''果实，主角可以吃掉，小鬼上身时会出现更多果实'''
	def __init__(self, x, y, index, near = 20, if_spirit = False, invisible = False):
		pass

	def react(self, hero, screen):
		'''靠近时'''
		pass

	def eaten(self, hero, screen):
		'''吃掉时,地图中的果实数减一,主角的生命值增加'''
		pass


class Chocolate(Item):
	'''巧克力，主角可以吃掉，可以增加主角的能量条'''
	def __init__(self, x, y, index, near = 20, if_spirit = False, invisible = False):
		pass

	def react(self, hero, screen):
		'''靠近时'''
		pass

	def eat(self, hero, screen):
		'''吃掉时'''
		pass

class Piece(Item):
	def Pieces(React):
		'''碎片，会被主角拾取,最终拼成花/火'''
		def __init__(self, x, y, width, height, name = '', portable = 0, hidden = False):
			pass

		def update(self):
			'''更新状态'''
			pass

		def if_picked(self, hero):
			'''判断是否被主角拾取'''
			pass

		def record(self, x, y, width, height):
			'''记录此时有多少碎片,作为侧栏出现在一角'''
			pass

class Ooze(Item):
	'''粘液道具，主角得到后获得发射粘液实现爬墙能力'''
	def __init__(self, x, y, near = 20):
		pass

class Brake(Item):
	'''刹车器，主角得到后获得刹车能力'''
	def __init__(self, x, y, near = 20):
		pass

class board():
	'''计数板，显示果子数，生命数，能量数，碎片数,现有道具等'''
	def __init__(self, x, y):
		'''初始化计数板属性'''
		pass
	
    
	def show(self):
		'''显示计数板'''
		pass

	def prep_fruit(self):
		'''准备果子计数图像'''
		pass

	def prep_life(self):
		'''准备生命计数图像'''
		pass

	def prep_energy(self):
		'''准备能量计数图像'''
		pass

	def prep_pieces(self):
		'''准备碎片计数图像'''
		pass

	def prep_ooze(self):
		'''准备粘液显示图像'''
		pass

	def prep_brake(self):
		'''准备刹车器显示图像'''
		pass



class Ghost(Sprite):
	'''大鬼，会追着主角跑，主角可以杀死'''
	def __init__(self, x, y,x_ghost , y1, near=20, ghost_life = 3):
		pass

	def update(self):
		'''更新大鬼位置'''
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

class Devil(Sprite):
	'''小鬼，主角无法杀死，会粘到主角身上，小鬼上身时地图上会出现更多红果实,小鬼上身一段时间会自动下身'''
	def __init__(self, x, y, x_devil, y_devil, near = 20, devil_life = 3):
		pass

	def if_haunt(self, hero, screen):
		'''判断是否在附身主角'''
		pass



class Home:
    '''存档点，主角经过时自动存档，下次死亡时从此处复活'''
    def __init__(self):
        pass

class Door:
	'''门，主角通过时可以进入下一个小地图'''
	def __init__(self):
		pass



'''
一个可能的用layout做地图的图例:(参照lab0 q5,lab1 layout.py)
H：主角（进入这张小地图时的初始位置）【假如一面地图有3条不同通道可以进入，那么要分别画3张txt示例）
' ':空地
$:存档点
#：门*
%：普通墙壁
B：可推动的墙壁*
K:弹性墙
V:易碎弹性墙
T:钢丝
G:大鬼*
D:小鬼*
F:果实*
C:巧克力*
P:碎片
O:粘液
B:刹车器


'''

class MapLayout:
    '''地图布局类，获取地图的基本信息和方法，并画出地图'''
    # 包括地图尺寸，以上所有元素的位置，带星号元素还要有计数和编号。

	def __init__(self, layout_file):
		self.size = self.get_map_size(layout_file)

	def get_map_size(self):
		'''获取地图尺寸'''
		pass

	def get_item_position(self, item_name):
		'''获取指定元素的位置'''
		pass

	def get_item_count(self, item_name):
		'''获取指定元素的数量'''    
		pass

	def get_item_id(self, item_name):
		'''获取指定元素的编号'''
		pass

	def draw(self, screen):
		'''绘制地图'''
		pass
