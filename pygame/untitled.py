import turtle

import time
screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(1366,768)

player=turtle.Turtle()
player.penup()
player.ht()
player.color("blue")
player.shape("square")
player.shapesize(0.2,0.2)
player.goto(0,0)
player.pendown()
parts=[]
parts2=[]
player2=turtle.Turtle()
player2.penup()
player2.ht()
player2.color("red")
player2.goto(-100,0)
player2.pendown()
player2.direction="stop"
border=turtle.Turtle()
border.ht()
border.penup()
border.speed(0)
border.color("red")
border.goto(-673,294)
border.pendown()
for i in range(2):
	border.fd(1256)
	border.rt(90)
	border.fd(598)
	border.rt(90)
player.direction="stop"
def go_up():
    if player.direction != "down":
        player.direction = "up"

def go_down():
    if player.direction != "up":
        player.direction = "down"

def go_left():
    if player.direction != "right":
        player.direction = "left"

def go_right():
    if player.direction != "left":
        player.direction = "right"

def go_up2():
    if player2.direction != "down":
        player2.direction = "up"

def go_down2():
    if player2.direction != "up":
        player2.direction = "down"

def go_left2():
    if player2.direction != "right":
        player2.direction = "left"

def go_right2():
    if player2.direction != "left":
        player2.direction = "right"
def move():
    
    if player.direction == "up":
        x=player.xcor()
        y = player.ycor()
        player.sety(y + 20)

    if player.direction == "down":
        x=player.xcor()
        y = player.ycor()
        player.sety(y - 20)
    if player.direction == "left":
        x = player.xcor()
        y=player.ycor()
        player.setx(x - 20)
    if player.direction == "right":
        x = player.xcor()
        y=player.ycor()
        player.setx(x + 20)
def move2():    
    if player2.direction == "up":        
        y = player2.ycor()
        x=player2.xcor()
        player2.sety(y + 20)

    if player2.direction == "down":
        y = player2.ycor()
        x=player2.xcor()
        player2.sety(y - 20)

    if player2.direction == "left":
        x = player2.xcor()
        y=player2.ycor()
        player2.setx(x - 20)

    if player2.direction == "right":
        x = player2.xcor()
        y=player2.ycor()
        player2.setx(x + 20)

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_up2, "w")
screen.onkeypress(go_left2, "a")
screen.onkeypress(go_down2, "s")
screen.onkeypress(go_right2, "d")
while True:
	
	screen.update()
	#move
	move()
	move2()
	new_part=turtle.Turtle()
	new_part.speed(0)
	new_part.color("grey")
	new_part.ht()
	new_part.penup()
	parts.append(new_part)

	for index in range(len(parts)-1,0,-1):
		x=parts[index-1].xcor()
		y=parts[index-1].ycor()
		parts[index].goto(x,y)
	if len(parts)>=0:
		x=player.xcor()
		y=player.ycor()
		parts[0].goto(x,y)
	for part in parts:
		if part.distance(player2)<0.2:
			player2.clear()
			player2.goto(-100,0)
			print("player 1 wins")
	new_part2=turtle.Turtle()
	new_part2.speed(0)
	new_part2.color("grey")
	new_part2.ht()
	new_part2.penup()
	parts2.append(new_part2)
	for inde in range(len(parts2)-1,0,-1):
		x=parts2[inde-1].xcor()
		y=parts2[inde-1].ycor()
		parts2[inde].goto(x,y)
	if len(parts2)>=0:
		x=player2.xcor()
		y=player2.ycor()
		parts2[0].goto(x,y)
	for part2 in parts2:
		if part2.distance(player)<0.2:
			player.clear()
			player.goto(-100,0)
			print("player 2 wins")
	#border
	if player.xcor()>593:
		player.setx(593)
	if player.xcor()<-593: 
		player.setx(-593)
	if player.ycor()<-274: 
		player.sety(-274)
	if player.ycor()>274:
		player.sety(274)
	if player2.xcor()>593:
		player2.setx(593)
	if player2.xcor()<-593: 
		player2.setx(-593)
	if player2.ycor()<-274: 
		player2.sety(-274)
	if player2.ycor()>274:
		player2.sety(274)
	time.sleep(0.01)


screen.mainloop()

