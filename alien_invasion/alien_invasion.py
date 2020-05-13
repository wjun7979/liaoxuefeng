import sys
import os
import pygame
from pygame.sprite import Group
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
    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)  # 监视键盘和鼠标事件
        ship.update()  # 根据移动标志调整飞船的位置
        gf.update_bullets(bullets)  # 更新子弹的位置，并删除已消失的子弹
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)  # 更新屏幕


os.chdir(sys.path[0])  # 将程序运行路径设置成当前文件所在的目录
run_game()
