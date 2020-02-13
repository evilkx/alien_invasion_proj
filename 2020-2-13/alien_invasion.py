import sys  # 由于game_functions中已导入，故此处可省略
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import Game_stats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一艘飞船,一个子弹编组，一个外星人编组
    stats = Game_stats(ai_settings)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = Game_stats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            #bullets.update()  已添加到game_function中
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            #gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        #gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button)
run_game()
