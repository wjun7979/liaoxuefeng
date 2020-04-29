import sys
import pygame


def check_keydown_events(event, ship):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # 单击游戏窗口的关闭按钮时，退出程序
        elif event.type == pygame.KEYDOWN:  # 键被按下时响应
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:  # 键被松开时响应
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)  # 每次循环时都重绘屏幕
    ship.blitme()  # 将飞船绘制到屏幕上
    pygame.display.flip()  # 让最近绘制的屏幕可见
