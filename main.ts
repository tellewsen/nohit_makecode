info.player1.onLifeZero(function on_player1_life_zero() {
    game.gameOver(true)
    game.setGameOverScoringType(game.ScoringType.HighScore)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    info.player1.setLife(info.life() - 1)
    player1.setFlag(SpriteFlag.GhostThroughSprites, true)
    pause(3000)
    player1.setFlag(SpriteFlag.GhostThroughSprites, false)
})
let enemySprite : Sprite = null
let enemies : Sprite[] = []
let player1 : Sprite = null
player1 = sprites.create(assets.image`
    playerSprite
`, SpriteKind.Player)
controller.moveSprite(player1)
player1.setStayInScreen(true)
let enemystart_x = [0, scene.screenWidth()]
let enemystart_y = [0, scene.screenHeight()]
game.onUpdate(function on_on_update() {
    info.changeScoreBy(1)
})
game.onUpdateInterval(100, function on_update_interval() {
    for (let spr of enemies) {
        spr.vx += randint(-10, 10)
        spr.vy += randint(-10, 10)
        if (spr.vx < 0) {
            spr.setImage(assets.image`
                ghostLeft
            `)
        }
        
        if (spr.vx > 0) {
            spr.setImage(assets.image`
                ghostRight
            `)
        }
        
    }
})
game.onUpdateInterval(3000, function on_update_interval2() {
    
    enemySprite = sprites.create(assets.image`
        ghostLeft
    `, SpriteKind.Enemy)
    enemySprite.setPosition(enemystart_x._pickRandom(), enemystart_y._pickRandom())
    enemySprite.setBounceOnWall(true)
    enemies.push(enemySprite)
})
