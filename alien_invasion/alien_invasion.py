import sys
import os
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景设置，让pygame能够正确地工作
    ai_settings = Settings()  # 创建设置类
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # 设置游戏窗口大小
    pygame.display.set_caption('Alien Invasion')  # 设置窗口标题
    ship = Ship(ai_settings, screen)  # 创建一艘飞船

    # 开始游戏的主循环
    while True:
        gf.check_events(ship)  # 监视键盘和鼠标事件
        ship.update()  # 根据移动标志调整飞船的位置
        gf.update_screen(ai_settings, screen, ship)  # 更新屏幕


os.chdir(sys.path[0])  # 将程序运行路径设置成当前文件所在的目录
run_game()
