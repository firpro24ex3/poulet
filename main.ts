namespace SpriteKind {
    export const difivil = SpriteKind.create()
    export const lemurrose = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.difivil, function (sprite, otherSprite) {
    pause(100)
    sprites.destroy(mySprite)
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Food, function (sprite2, otherSprite2) {
    sprites.destroy(mySprite2, effects.spray, 500)
    pause(100)
    mySprite2 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . 2 2 2 2 2 e . . . . 
        . . . . . 2 2 2 2 d 2 2 e . . . 
        . . . . e 2 2 2 2 2 2 2 e . . . 
        . . . . e 2 2 2 2 2 2 2 e . . . 
        . . . . e 2 2 2 2 2 e f f c c . 
        . . . . e e 2 2 e f f f f b c . 
        . . e e e f e 2 2 b f f f d c . 
        . e e 2 2 d f e 2 1 1 1 1 b c . 
        . e e 2 2 d f e e e c c c . . . 
        . b 1 1 e e 2 2 e e c . . . . . 
        . . f d d 2 2 2 f f f d d . . . 
        e e f d d e e e . f f d d . . . 
        e e e f f f f f . . . . . . . . 
        e e . . . . f f f . . . . . . . 
        . . . . . . f f f f . . . . . . 
        `, SpriteKind.Projectile)
    mySprite2.setPosition(-3, 31)
    mySprite2.setVelocity(100, 0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite4, otherSprite4) {
    pause(100)
    sprites.destroy(mySprite)
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.difivil, SpriteKind.lemurrose, function (sprite3, otherSprite3) {
    sprites.destroy(my_sptrite_4)
    my_sptrite_4 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . e 2 2 2 2 2 . . . . . . 
        . . . e 2 2 d 2 2 2 2 . . . . . 
        . . . e 2 2 2 2 2 2 2 e . . . . 
        . . . e 2 2 2 2 2 2 2 e . . . . 
        . c c f f e 2 2 2 2 2 e . . . . 
        . c b f f f f e 2 2 e e . . . . 
        . c d f f f b 2 2 e f e e e . . 
        . c b 1 1 1 1 2 e f d 2 2 e e . 
        . . . c c c e e e f d 2 2 e e . 
        . . . . . c e e 2 2 e e 1 1 b . 
        . . . d d f f f 2 2 2 d d f . . 
        . . . d d f f . e e e d d f e e 
        . . . . . . . . f f f f f e e e 
        . . . . . . . f f f . . . . e e 
        . . . . . . f f f f . . . . . . 
        `, SpriteKind.difivil)
    my_sptrite_4.setPosition(159, 5)
    my_sptrite_4.setVelocity(-100, 0)
})
let my_sptrite_4: Sprite = null
let mySprite2: Sprite = null
let mySprite: Sprite = null
mySprite = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . 2 2 . . . . . . 
    . . . . . . . 2 2 2 2 . . . . . 
    . . . . . . 1 1 1 1 1 1 . . . . 
    . . . . . . 2 1 1 1 1 2 . . . . 
    . . . . . . 1 1 1 1 1 1 . . . . 
    . . . . . . 1 1 1 1 1 1 . . . . 
    . . . . . . 1 1 1 1 1 1 . . . . 
    . . . . . . 1 1 1 1 1 1 . . . . 
    . . . . . . 1 1 1 1 1 1 . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
mySprite.setPosition(30, 80)
controller.moveSprite(mySprite, 100, 100)
mySprite2 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . 2 2 2 2 2 e . . . . 
    . . . . . 2 2 2 2 d 2 2 e . . . 
    . . . . e 2 2 2 2 2 2 2 e . . . 
    . . . . e 2 2 2 2 2 2 2 e . . . 
    . . . . e 2 2 2 2 2 e f f c c . 
    . . . . e e 2 2 e f f f f b c . 
    . . e e e f e 2 2 b f f f d c . 
    . e e 2 2 d f e 2 1 1 1 1 b c . 
    . e e 2 2 d f e e e c c c . . . 
    . b 1 1 e e 2 2 e e c . . . . . 
    . . f d d 2 2 2 f f f d d . . . 
    e e f d d e e e . f f d d . . . 
    e e e f f f f f . . . . . . . . 
    e e . . . . f f f . . . . . . . 
    . . . . . . f f f f . . . . . . 
    `, SpriteKind.Projectile)
scene.setBackgroundImage(assets.image`read`)
mySprite2.setPosition(-3, 31)
mySprite2.setVelocity(100, 0)
let mySprite3 = sprites.create(img`
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    `, SpriteKind.Player)
mySprite3.setPosition(164, 33)
mySprite3.setKind(SpriteKind.Food)
my_sptrite_4 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . e 2 2 2 2 2 . . . . . . 
    . . . e 2 2 d 2 2 2 2 . . . . . 
    . . . e 2 2 2 2 2 2 2 e . . . . 
    . . . e 2 2 2 2 2 2 2 e . . . . 
    . c c f f e 2 2 2 2 2 e . . . . 
    . c b f f f f e 2 2 e e . . . . 
    . c d f f f b 2 2 e f e e e . . 
    . c b 1 1 1 1 2 e f d 2 2 e e . 
    . . . c c c e e e f d 2 2 e e . 
    . . . . . c e e 2 2 e e 1 1 b . 
    . . . d d f f f 2 2 2 d d f . . 
    . . . d d f f . e e e d d f e e 
    . . . . . . . . f f f f f e e e 
    . . . . . . . f f f . . . . e e 
    . . . . . . f f f f . . . . . . 
    `, SpriteKind.difivil)
my_sptrite_4.setPosition(159, 5)
my_sptrite_4.setVelocity(-100, 0)
let mur_rose = sprites.create(img`
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    . . . . . . . . . . . 3 . . . . 
    `, SpriteKind.lemurrose)
