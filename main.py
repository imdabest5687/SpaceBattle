@namespace
class SpriteKind:
    Heart = SpriteKind.create()
    Mode = SpriteKind.create()
    Cake = SpriteKind.create()
    Mode_1 = SpriteKind.create()

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . 6 6 6 6 . . . .
        . . . . . 6 6 6 6 9 9 6 . . . .
        . . 6 6 6 6 6 6 6 6 9 6 . . . .
        . . 6 6 6 6 6 6 6 6 6 6 . . . .
        . . . . . 6 6 6 6 . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """),
        Player_1,
        200,
        0)
    music.pew_pew.play()
    if Double_Fire and Double_Fire.lifespan > 0:
        projectile.y += -5
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . 6 6 6 6 . . . . 
                            . . . . . 6 6 6 6 9 9 6 . . . . 
                            . . 6 6 6 6 6 6 6 6 9 6 . . . . 
                            . . 6 6 6 6 6 6 6 6 6 6 . . . . 
                            . . . . . 6 6 6 6 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Player_1,
            200,
            0)
        projectile.y += 5
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_life_by(1)
    otherSprite.destroy(effects.spray, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Heart, on_on_overlap)

def on_on_overlap2(sprite4, otherSprite3):
    sprite4.destroy(effects.spray, 500)
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite3).value += -20
    scene.camera_shake(2, 500)
    music.small_crash.play()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_on_zero(status):
    enemyDeath(status.sprite_attached_to())
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def enemyDeath(enemy: Sprite):
    global Power_Up, Power_Up_1
    enemy.destroy(effects.spray, 500)
    if Math.percent_chance(5):
        Power_Up = sprites.create(img("""
                . . . . . . . 6 . . . . . . . . 
                            . . . . . . 8 6 6 . . . 6 8 . . 
                            . . . e e e 8 8 6 6 . 6 7 8 . . 
                            . . e 2 2 2 2 e 8 6 6 7 6 . . . 
                            . e 2 2 4 4 2 7 7 7 7 7 8 6 . . 
                            . e 2 4 4 2 6 7 7 7 6 7 6 8 8 . 
                            e 2 4 5 2 2 6 7 7 6 2 7 7 6 . . 
                            e 2 4 4 2 2 6 7 6 2 2 6 7 7 6 . 
                            e 2 4 2 2 2 6 6 2 2 2 e 7 7 6 . 
                            e 2 4 2 2 4 2 2 2 4 2 2 e 7 6 . 
                            e 2 4 2 2 2 2 2 2 2 2 2 e c 6 . 
                            e 2 2 2 2 2 2 2 4 e 2 e e c . . 
                            e e 2 e 2 2 4 2 2 e e e c . . . 
                            e e e e 2 e 2 2 e e e c . . . . 
                            e e e 2 e e c e c c c . . . . . 
                            . c c c c c c c . . . . . . . .
            """),
            SpriteKind.food)
        Power_Up.x = Enemy_1.x
        Power_Up.y = Enemy_1.y
    if Math.percent_chance(3):
        Power_Up_1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 2 2 . . . 2 2 . . . . 
                            . . . . 2 2 2 2 . 2 2 2 2 . . . 
                            . . . 2 2 2 2 2 2 2 3 3 2 2 . . 
                            . . . 2 2 2 2 2 2 2 2 3 2 2 . . 
                            . . . 2 2 2 2 2 2 2 2 2 2 2 . . 
                            . . . . 2 2 2 2 2 2 2 2 2 . . . 
                            . . . . . 2 2 2 2 2 2 2 . . . . 
                            . . . . . . 2 2 2 2 2 . . . . . 
                            . . . . . . . 2 2 2 . . . . . . 
                            . . . . . . . . 2 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Heart)
        Power_Up_1.x = Enemy_1.x
        Power_Up_1.y = Enemy_1.y

def on_on_overlap3(sprite2, otherSprite2):
    global Double_Fire
    Double_Fire = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . 6 6 6 6 . . . . 
                    . . . . . 6 6 6 6 9 9 6 . . . . 
                    . . 6 6 6 6 6 6 6 6 9 6 . . . . 
                    . . 6 6 6 6 6 6 6 6 6 6 . . . . 
                    . . . . . 6 6 6 6 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . 6 6 6 6 . . . . 
                    . . . . . 6 6 6 6 9 9 6 . . . . 
                    . . 6 6 6 6 6 6 6 6 9 6 . . . . 
                    . . 6 6 6 6 6 6 6 6 6 6 . . . . 
                    . . . . . 6 6 6 6 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Mode)
    Double_Fire.set_position(48, 7)
    Double_Fire.lifespan = 20000
    otherSprite2.destroy(effects.spray, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

def on_on_overlap4(sprite5, otherSprite4):
    info.change_life_by(-1)
    enemyDeath(otherSprite4)
    scene.camera_shake(4, 1000)
    music.big_crash.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

def on_life_zero():
    game.over(False, effects.confetti)
info.on_life_zero(on_life_zero)

def on_on_destroyed(sprite3):
    info.change_score_by(1)
sprites.on_destroyed(SpriteKind.enemy, on_on_destroyed)

statusbar: StatusBarSprite = None
Power_Up_1: Sprite = None
Enemy_1: Sprite = None
Power_Up: Sprite = None
Double_Fire: Sprite = None
projectile: Sprite = None
Player_1: Sprite = None
effects.star_field.start_screen_effect()
music.set_volume(10)
game.splash("Hello! Welcome to Space Battle! Destroy enemy ships and gain points and power ups! Play with your friends to make it even more fun! Enjoy!")
Player_1 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . 4 4 6 . . . . . . . . . . . . 
            . . . 6 6 6 . . . . . . . . . . 
            . . . 6 6 6 6 6 . . . . . . . . 
            . . . 6 6 6 6 6 6 6 6 6 . . . . 
            . . . 6 6 6 6 6 6 6 6 6 9 9 . . 
            . . . 6 6 6 6 6 6 6 6 6 . . . . 
            . . . 6 6 6 6 6 6 . . . . . . . 
            . . . 6 6 6 . . . . . . . . . . 
            . 4 4 6 6 . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
Player_1.set_stay_in_screen(True)
controller.move_sprite(Player_1)
info.set_life(3)
info.set_score(0)
Enemy_Speed = 20
Enemy_Spawn_Time = 2000

def on_update_interval():
    global Enemy_Speed, Enemy_Spawn_Time
    Enemy_Speed += 5
    Enemy_Speed = min(Enemy_Speed, 40)
    Enemy_Spawn_Time += -75
    Enemy_Spawn_Time = max(Enemy_Spawn_Time, 1500)
game.on_update_interval(5000, on_update_interval)

def on_forever():
    global Enemy_1, statusbar
    Enemy_1 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . 2 2 . . . . 
                    . . . . . . . . . 2 2 2 9 9 . . 
                    . . . . . . . 2 2 2 2 2 . . . . 
                    . . . . . 2 2 2 2 2 2 2 . . . . 
                    . . . . 2 2 2 2 2 2 2 2 . . . . 
                    . . 5 5 2 2 2 2 2 2 2 2 . . . . 
                    . . . . 2 2 2 2 2 2 2 2 . . . . 
                    . . . . . 2 2 2 2 2 2 2 . . . . 
                    . . . . . . . 2 2 2 2 2 9 9 . . 
                    . . . . . . . . . 2 2 2 . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    Enemy_1.x = scene.screen_width()
    Enemy_1.vx = 0 - Enemy_Speed
    Enemy_1.y = randint(10, scene.screen_height() - 10)
    statusbar = statusbars.create(20, 4, StatusBarKind.enemy_health)
    statusbar.set_color(5, 10)
    statusbar.attach_to_sprite(Enemy_1)
    pause(Enemy_Spawn_Time)
forever(on_forever)
