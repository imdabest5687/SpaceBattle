namespace SpriteKind {
    export const Heart = SpriteKind.create()
    export const Mode = SpriteKind.create()
    export const Cake = SpriteKind.create()
    export const Mode_1 = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, Player_1, 200, 0)
    music.pewPew.play()
    if (Double_Fire && Double_Fire.lifespan > 0) {
        projectile.y += -5
        projectile = sprites.createProjectileFromSprite(img`
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
            `, Player_1, 200, 0)
        projectile.y += 5
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Heart, function (sprite, otherSprite) {
    info.changeLifeBy(1)
    otherSprite.destroy(effects.spray, 500)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite4, otherSprite3) {
    sprite4.destroy(effects.spray, 500)
    statusbars.getStatusBarAttachedTo(StatusBarKind.EnemyHealth, otherSprite3).value += -20
    scene.cameraShake(2, 500)
    music.smallCrash.play()
})
statusbars.onZero(StatusBarKind.EnemyHealth, function (status) {
    enemyDeath(status.spriteAttachedTo())
})
function enemyDeath (enemy: Sprite) {
    enemy.destroy(effects.spray, 500)
    if (Math.percentChance(5)) {
        Power_Up = sprites.create(img`
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
            `, SpriteKind.Food)
        Power_Up.x = Enemy_1.x
        Power_Up.y = Enemy_1.y
    }
    if (Math.percentChance(3)) {
        Power_Up_1 = sprites.create(img`
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
            `, SpriteKind.Heart)
        Power_Up_1.x = Enemy_1.x
        Power_Up_1.y = Enemy_1.y
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite2, otherSprite2) {
    Double_Fire = sprites.create(img`
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
        `, SpriteKind.Mode)
    Double_Fire.setPosition(48, 7)
    Double_Fire.lifespan = 20000
    otherSprite2.destroy(effects.spray, 500)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite5, otherSprite4) {
    info.changeLifeBy(-1)
    enemyDeath(otherSprite4)
    scene.cameraShake(4, 1000)
    music.bigCrash.play()
})
info.onLifeZero(function () {
    game.over(false, effects.melt)
})
sprites.onDestroyed(SpriteKind.Enemy, function (sprite3) {
    info.changeScoreBy(1)
})
let statusbar: StatusBarSprite = null
let Power_Up_1: Sprite = null
let Enemy_1: Sprite = null
let Power_Up: Sprite = null
let Double_Fire: Sprite = null
let projectile: Sprite = null
let Player_1: Sprite = null
effects.starField.startScreenEffect()
music.setVolume(10)
game.splash("Hello! Welcome to Space Battle! Destroy enemy ships and gain points and power ups! Play with your friends to make it even more fun! Enjoy!")
Player_1 = sprites.create(img`
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
    `, SpriteKind.Player)
Player_1.setStayInScreen(true)
controller.moveSprite(Player_1)
info.setLife(3)
info.setScore(0)
let Enemy_Speed = 20
let Enemy_Spawn_Time = 2000
game.onUpdateInterval(5000, function () {
    Enemy_Speed += 5
    Enemy_Speed = Math.min(Enemy_Speed, 40)
    Enemy_Spawn_Time += -75
    Enemy_Spawn_Time = Math.max(Enemy_Spawn_Time, 1500)
})
forever(function () {
    Enemy_1 = sprites.create(img`
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
        `, SpriteKind.Enemy)
    Enemy_1.x = scene.screenWidth()
    Enemy_1.vx = 0 - Enemy_Speed
    Enemy_1.y = randint(10, scene.screenHeight() - 10)
    statusbar = statusbars.create(20, 4, StatusBarKind.EnemyHealth)
    statusbar.setColor(5, 10)
    statusbar.attachToSprite(Enemy_1)
    pause(Enemy_Spawn_Time)
})
