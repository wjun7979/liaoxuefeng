class Settings():
    '''存储《外星人入侵》的所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5  # 飞船的移动速度
        self.ship_limit = 3  # 玩家拥有的飞船数量

        # 子弹设置
        self.bullet_speed_factor = 3  # 子弹的飞行速度
        self.bullet_width = 3  # 子弹的宽度
        self.bullet_height = 15  # 子弹的高度
        self.bullet_color = 60, 60, 60  # 子弹的颜色
        self.bullets_allowed = 3  # 最大子弹数

        # 外星人设置
        self.alien_speed_factor = 1  # 外星人左右移动的速度
        self.fleet_drop_speed = 10  # 外星人群向下移动的速度
        self.fleet_direction = 1  # 为1表示向右移，为-1表示向左移
