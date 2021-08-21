#set up the screen
import turtle
import os
import math
import random
import winsound

#set up the screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("SPACE INVADERS")
wn.bgpic("IrF.gif")
wn.tracer(0)

#Registering the space
wn.register_shape("74xC.gif")
wn.register_shape("d5rt6sa-32b3d6c4-0c7f-4931-8425-e8cd6d9b86ed.gif")
#Draw border
border=turtle.Turtle()
border.speed(0)
border.color("orange")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()


score=0

#Draw the score
score_pen=turtle.Turtle()
score_pen.speed()
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-280,280)
scorestring="Score:%s"%score
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()
                
#Creating the player turtle
player=turtle.Turtle()
player.color("green")
player.shape("d5rt6sa-32b3d6c4-0c7f-4931-8425-e8cd6d9b86ed.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

player.speed=10



#chose number of enemies
number_of_enemies=30
enemies=[]

#Adding enemies
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())


enemyx=-220
enemyy=250
enemy_number=0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("74xC.gif")
    enemy.penup()
    enemy.speed(0)
    x=enemyx +(50*enemy_number)
    y=enemyy
    enemy.setposition(x,y)
    #updating enemy number
    enemy_number+=1
    if enemy_number==10:
        enemyy-=50
        enemy_number=0

enemyspeed=0.2


#Creating player's bullet
bullet=turtle.Turtle()
bullet.color("cyan")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=6

#definng bulet state
#ready to fire
#fire-bullet is firing
bulletstate="ready"



#moving the player left
def left():
    player.speed=-3
    

#moving the  player right
def right():
    player.speed=3

def move_player():
    x=player.xcor()
    x+=player.speed
    if x<-290:
        x=-290
    if x>290:
        x=290
    player.setx(x)

def fire():
    #Declare bulletstate is global
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        #Move the bullet just above the player
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance< 15:
        return True
    else:
        return False

def play_sound(sound_file,time=0):
    winsound.PlaySound(sound_file,winsound.SND_ASYNC)
    

#Create keyboard binding
turtle.listen()
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.onkey(fire,"space")

#main game loop

while True:
    wn.update()
    move_player()
    for enemy in enemies:

        #move enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor()>280:
            #Move all enemies down
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            #Change the direction
            enemyspeed*=-1

        if enemy.xcor()<-280:
             #Move all enemies down
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            #Change the direction
            enemyspeed*=-1

    #check the collision
        if isCollision(bullet,enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            #reset the enemy
            enemy.setposition(0,10000)
            #Update score
            score+=10
            scorestring="Score=%s"%score
            score_pen.clear()
            score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
        if isCollision(player,enemy):
            player_sound("invaderkilled.wav")
            enemy.hideturtle()
            player.hideturtle()
            
            print("GAME OVER!!!BETTER LUCK NEXT TIME")
            breakpoint
        
    #Moving the bullet
    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

    #bullet reach top
    if bullet.ycor()>290:
        bullet.hideturtle()
        bulletstate="ready"

    
    












wn.mainloop()

