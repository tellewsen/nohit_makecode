def on_player1_life_zero():
    game.game_over(True)
    game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)
info.player1.on_life_zero(on_player1_life_zero)

def on_on_overlap(sprite, otherSprite):
    info.player1.set_life(info.life() - 1)
    player1.set_flag(SpriteFlag.GHOST_THROUGH_SPRITES, True)
    pause(3000)
    player1.set_flag(SpriteFlag.GHOST_THROUGH_SPRITES, False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

enemySprite: Sprite = None
enemies: List[Sprite] = []
player1: Sprite = None
player1 = sprites.create(assets.image("""
    playerSprite
"""), SpriteKind.player)
controller.move_sprite(player1)
player1.set_stay_in_screen(True)
enemystart_x = [0, scene.screen_width()]
enemystart_y = [0, scene.screen_height()]

def on_on_update():
    info.change_score_by(1)
game.on_update(on_on_update)

def on_update_interval():
    for spr in enemies:
        spr.vx += randint(-10, 10)
        spr.vy += randint(-10, 10)
        if spr.vx < 0:
            spr.set_image(assets.image("""
                ghostLeft
            """))
        if spr.vx > 0:
            spr.set_image(assets.image("""
                ghostRight
            """))
game.on_update_interval(100, on_update_interval)

def on_update_interval2():
    global enemySprite
    enemySprite = sprites.create(assets.image("""
        ghostLeft
    """), SpriteKind.enemy)
    enemySprite.set_position(enemystart_x._pick_random(), enemystart_y._pick_random())
    enemySprite.set_bounce_on_wall(True)
    enemies.append(enemySprite)
game.on_update_interval(3000, on_update_interval2)
