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

        # 子弹设置
        self.bullet_speed_factor = 1  # 子弹的飞行速度
        self.bullet_width = 3  # 子弹的宽度
        self.bullet_height = 15  # 子弹的高度
        self.bullet_color = 60, 60, 60  # 子弹的颜色
        self.bullets_allowed = 3  # 最大子弹数
