@namespace
class SpriteKind:
    difivil = SpriteKind.create()
    lemurrose = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    pause(100)
    sprites.destroy(mySprite)
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.difivil, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    global mySprite2
    sprites.destroy(mySprite2, effects.spray, 500)
    pause(100)
    mySprite2 = sprites.create(img("""
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
        """),
        SpriteKind.projectile)
    mySprite2.set_position(-3, 31)
    mySprite2.set_velocity(100, 0)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.food, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    global my_sptrite_4
    sprites.destroy(my_sptrite_4)
    my_sptrite_4 = sprites.create(img("""
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
        """),
        SpriteKind.difivil)
    my_sptrite_4.set_position(159, 5)
    my_sptrite_4.set_velocity(-100, 0)
sprites.on_overlap(SpriteKind.difivil, SpriteKind.lemurrose, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    pause(100)
    sprites.destroy(mySprite)
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap4)

my_sptrite_4: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
mySprite.set_position(30, 80)
controller.move_sprite(mySprite, 100, 100)
mySprite2 = sprites.create(img("""
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
    """),
    SpriteKind.projectile)
scene.set_background_image(assets.image("""
    read
"""))
mySprite2.set_position(-3, 31)
mySprite2.set_velocity(100, 0)
mySprite3 = sprites.create(img("""
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
    """),
    SpriteKind.player)
mySprite3.set_position(164, 33)
mySprite3.set_kind(SpriteKind.food)
my_sptrite_4 = sprites.create(img("""
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
    """),
    SpriteKind.difivil)
my_sptrite_4.set_position(159, 5)
my_sptrite_4.set_velocity(-100, 0)
mur_rose = sprites.create(img("""
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
    """),
    SpriteKind.lemurrose)
