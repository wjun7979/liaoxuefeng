import sys
import os
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景设置，让pygame能够正确地工作
    ai_settings = Settings()  # 创建设置类
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # 设置游戏窗口大小
    pygame.display.set_caption('【外星人入侵】  P:开始、左右箭头:移动、空格:射击、Q:退出')  # 设置窗口标题

    # 创建Play按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)  # 监视键盘和鼠标事件
        if stats.game_active:
            ship.update()  # 根据移动标志调整飞船的位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)  # 更新子弹的位置，并删除已消失的子弹
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)  # 更新外星人的位置
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)  # 更新屏幕


os.chdir(sys.path[0])  # 将程序运行路径设置成当前文件所在的目录
run_game()
