#SETUP PYGAME ZERO
import pgzrun
import pygame
import random
pygame.init()
score=0
check=0
#SCREEN
HEIGHT=800
WIDTH=800
#SETUP SCORE
#SETUP BRICK
brick=Actor("brick")
brick.x=100
brick.y=200
#SETUP WALLS
  #SETUP UPPER WALL
upper_wall=Actor("wall-top")
upper_wall.x=400
upper_wall.y=random.randrange(-60,120)
  #SETUP LOWER WALL
lower_wall=Actor("wall-bottom")
lower_wall.x=400
lower_wall.y=upper_wall.y+400
#SETUP GAME OVER SIGN
gameover=pygame.font.Font("freesansbold.ttf",40)
pygame.display.set_caption("flappy bird")
icon=pygame.image.load("a330.png")
pygame.display.set_icon(icon)
#BUTTON PRESSES
def game_over():
  global check
  check=1
  brick.y=250
  lower_wall.x=9999999999
  upper_wall.x=9999999999
def on_mouse_down():
  print("You clicked the mouse")
  if brick.y>38:
    brick.y=brick.y-25
  else:
    print("You cannot go above the screen.")
#DRAW STUFF TO SCREEN
def draw():
  global check
  screen.fill("black")
  brick.draw()
  upper_wall.draw()
  lower_wall.draw()
  if check==1:
    screen.draw.text("game over",(200,200))
  screen.draw.text(str(score),(50,50))
#MOVEMENTS
def update():
  global score
  brick.y=brick.y+1
  lower_wall.x=lower_wall.x-3
  upper_wall.x=lower_wall.x
  if lower_wall.x<1:
    lower_wall.x=800
    upper_wall.y=random.randrange(-60,120)
    lower_wall.y=upper_wall.y+400
    score=score+1
  if brick.colliderect(upper_wall) or brick.colliderect(lower_wall):
    game_over()
#EACH CYCLE THROUGH THE LOOP
#COLLISIONS
#RESET
#RUN PYGAME ZERO
pgzrun.go()