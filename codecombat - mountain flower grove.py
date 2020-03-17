#Mountain Flower grove

# This level is a place for making flower art.
# The real goal is to experiment and have fun!
# If you draw something with at least 1000 flowers, you will "succeed" at the level.
def drawHexagon(x, y, size):
    hero.toggleFlowers(False)
    angle = 0
    hero.moveXY (x+size, y)
    hero.toggleFlowers(True)
    hero.say(Math.pi*2)
    while (angle <= Math.PI*2):
        hero.moveXY(x+size*Math.cos(angle), y + size*Math.sin(angle))
        angle+=Math.PI/3
    hero.toggleFlowers(False)

hero.setFlowerColor("white")
drawHexagon(85, 70, 10)
hero.setFlowerColor("blue")
drawHexagon(85, 70, 20)
hero.setFlowerColor("pink")
drawHexagon(85, 70, 30)
hero.setFlowerColor("yellow")
drawHexagon(85, 70, 40)
hero.setFlowerColor('red')
drawHexagon(85, 70, 50)
hero.setFlowerColor('purple')
drawHexagon(85, 70, 60)
hero.moveXY(85, 70)
