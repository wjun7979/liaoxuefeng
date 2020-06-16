class GameStats():
    '''跟踪游戏的统计信息'''

    def __init__(self, ai_settings):
        '''初始化统计信息'''
        self.ai_settings = ai_settings
        self.reset_stats()
        # 让游戏一开始处于非活动状态
        self.game_active = False
        # 从文件中读取历史最高分，在任何情况下都不应重置最高得分
        with open('high_score.txt', 'a+') as f:
            f.seek(0)
            old_high_score = f.read()
            old_high_score = 0 if old_high_score.strip() == '' else int(old_high_score)
            self.high_score = old_high_score

    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0  # 得分
        self.level = 1  # 当前等级
