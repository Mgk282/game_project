import pygame
from PycharmProjects.game import funkc, game_heroes
from PycharmProjects.game.game_heroes import mobs, gg, mob

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1440, 800))

mob_zombie = pygame.image.load('images/mobs/zombie/zombie_1.png').convert_alpha()
mob_zombie_x = 1500
mob_zombie_timer = pygame.USEREVENT + 1
pygame.time.set_timer(mob_zombie_timer, 10000)
mobs_list_in_game = []


background_image = pygame.image.load('images/background_game.jpg').convert_alpha()
pygame.display.set_caption("game gg")

icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)

myfont = pygame.font.Font('font/DeliciousHandrawn-Regular.ttf', 40)
text_surface = myfont.render('New Game!', True, 'DarkRed')

walk_down = [
    pygame.image.load('images/gg_player_down/down_1.png').convert_alpha(),
    pygame.image.load('images/gg_player_down/down_2.png').convert_alpha(),
    pygame.image.load('images/gg_player_down/down_3.png').convert_alpha(),
    pygame.image.load('images/gg_player_down/down_4.png').convert_alpha(),
]
walk_up = [
    pygame.image.load('images/gg_player_up/up_1.png').convert_alpha(),
    pygame.image.load('images/gg_player_up/up_2.png').convert_alpha(),
    pygame.image.load('images/gg_player_up/up_3.png').convert_alpha(),
    pygame.image.load('images/gg_player_up/up_4.png').convert_alpha(),
]
walk_left = [
    pygame.image.load('images/gg_player_left/left_1.png').convert_alpha(),
    pygame.image.load('images/gg_player_left/left_2.png').convert_alpha(),
    pygame.image.load('images/gg_player_left/left_3.png').convert_alpha(),
    pygame.image.load('images/gg_player_left/left_4.png').convert_alpha(),
]
walk_right = [
    pygame.image.load('images/gg_player_right/right_1.png').convert_alpha(),
    pygame.image.load('images/gg_player_right/right_2.png').convert_alpha(),
    pygame.image.load('images/gg_player_right/right_3.png').convert_alpha(),
    pygame.image.load('images/gg_player_right/right_4.png').convert_alpha(),
]

player_anim_count = 0
background_x = 0

player_speed = 15
player_x = 300
player_y = 550

background_sound = pygame.mixer.Sound('music/rpg/bg_s.mp3')
background_sound.play(-1)

run = True

while run:
    keys = pygame.key.get_pressed()
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + 1440, 0))

    if mobs_list_in_game:
        for (i,el) in enumerate (mobs_list_in_game):
            screen.blit(mob_zombie, el)
            el.x -= 10
        if el.x <-10:
            mobs_list_in_game.pop(i)
        if player_rect.colliderect(mob_zombie_rect):
            funkc.atack(gg, mobs)
            funkc.kill_mob(gg, mobs)

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    player_rect = walk_left[1].get_rect(topleft=(player_x, player_y))
    mob_zombie_rect = mob_zombie.get_rect(topleft=(mob_zombie_x, 550))
    # screen.blit(text_surface, (500, 400))
    pygame.display.update()
    pygame.time.delay(50)

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    background_x -= 10
    if background_x == -1440:
        background_x = 0

    mob_zombie_x -= 10

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 50:
        player_x -= player_speed
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < 800:
        player_x += player_speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == mob_zombie_timer:
            mobs_list_in_game.append(mob_zombie.get_rect(topleft=(1300, 550)))
    clock.tick(10)
pygame.quit()
