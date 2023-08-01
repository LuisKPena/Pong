
#Python 3 version of Pong


import turtle


def main():

    #UI set up

    window = turtle.Screen()
    window.title("Pong")
    window.bgcolor("black")
    window.setup(width=800, height=600)
    window.tracer(0)

    #Score display

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("pink")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Player 1: 0  Player 2: 0", align="center", font = ("Courier",20,"bold"))

    #Score keeper

    scoreA = 0
    scoreB = 0
    

    #Inputs

    #Paddle A

    paddleA = turtle.Turtle()
    paddleA.speed(0)
    paddleA.shape("square")
    paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
    paddleA.color("light blue")
    paddleA.penup()
    paddleA.goto(-350,0)

    #Paddle B

    paddleB = turtle.Turtle()
    paddleB.speed(0)
    paddleB.shape("square")
    paddleB.shapesize(stretch_wid=5, stretch_len=1)
    paddleB.color("orange")
    paddleB.penup()
    paddleB.goto(350,0)

    #Ball

    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0,0)
    ball.dx = .2
    ball.dy = .4

    #Paddle movement

    def paddleAUp():

        y = paddleA.ycor()
        y += 30
        paddleA.sety(y)

        if paddleA.ycor() > 250:

            paddleA.sety(250)

    def paddleADown():

        y = paddleA.ycor()
        y += -30
        paddleA.sety(y)

        if paddleA.ycor() < -250:

            paddleA.sety(-250)

    def paddleBUp():

        y = paddleB.ycor()
        y += 30
        paddleB.sety(y)

        if paddleB.ycor() > 250:

            paddleB.sety(250)

    def paddleBDown():

        y = paddleB.ycor()
        y += -30
        paddleB.sety(y)

        if paddleB.ycor() < -250:

            paddleB.sety(-250)

    #Keyboard input

    window.listen()
    window.onkeypress(paddleAUp, "w")

    window.listen()
    window.onkeypress(paddleADown, "s")

    window.listen()
    window.onkeypress(paddleBUp, "Up")

    window.listen()
    window.onkeypress(paddleBDown, "Down")
  
    
    #Main name loop

    while True:
        window.update()

        #Ball movement

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #Ball bounce

        if ball.ycor() > 290:

            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:

            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:

            ball.goto(0,0)
            ball.dx *= -1
            scoreA += 1
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(scoreA, scoreB), align="center",
                      font = ("Courier",20,"bold"))

        if ball.xcor() < -390:

            ball.goto(0,0)
            ball.dx *= -1
            scoreB += 1
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(scoreA, scoreB), align="center",
                      font = ("Courier",20,"bold"))

        #Paddle and ball collision

        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and
                                  ball.ycor() > paddleB.ycor() - 40):

            ball.setx(335)
            ball.dx *= -1
            ball.dx += .1
            ball.dy += .1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and
                                  ball.ycor() > paddleA.ycor() - 40):

            ball.setx(-335)
            ball.dx *= -1
            ball.dx += .1
            ball.dy += .1

        

main()
