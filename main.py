import turtle
import random
import time

text_font = ("Arial", 30, "normal")   # ekrandaki text'lerin font'u
score = 0
t = 20


def turtle_moving():
    turtle_instance.hideturtle()
    turtle_instance.goto(random.randint(-250, 250), random.randint(-250, 250))
    turtle_instance.showturtle()


def get_click_pos(x,y):
    turtle_click.goto(x,y)


# ekran özellikleri
drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch the Turtle")
drawing_board.setup(1000,1000)


# text_score turtle oluşturulması
turtle_text_score = turtle.Turtle()
turtle_text_score.hideturtle()
turtle_text_score.penup()
turtle_text_score.goto(-100,300)
turtle_text_score.pencolor("blue")
turtle_text_score.write("Skor:", align= "left", font=text_font)


# text_time turtle oluşturulması
turtle_text_time = turtle.Turtle()
turtle_text_time.hideturtle()
turtle_text_time.penup()
turtle_text_time.goto(-100,250)
turtle_text_time.write("Zaman:", align="left", font=text_font)


# turtle_score oluşturulması
turtle_score = turtle.Turtle()
turtle_score.hideturtle()
turtle_score.penup()
turtle_score.pencolor("blue")
turtle_score.goto(50,300)


# turtle_countdown oluşturulması
turtle_countdown = turtle.Turtle()
turtle_countdown.hideturtle()
turtle_countdown.penup()
turtle_countdown.goto(70,250)


# turtle_instance oluşturulması
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(3,3,3)
turtle_instance.penup()


# turtle_click oluşturulması
turtle_click = turtle.Turtle()
turtle_click.hideturtle()
turtle_click.shape("turtle")
turtle_click.penup()


while True:
    turtle_score.write(score, align="center", font=text_font)
    turtle_countdown.write(t, align="center", font=text_font)
    turtle_countdown.clear()
    time.sleep(1)
    t -= 1
    drawing_board.ontimer(turtle_moving(), 50)
    drawing_board.listen()
    drawing_board.onscreenclick(get_click_pos)

    if turtle_instance.distance(turtle_click) < 200:
        print(turtle_instance.distance(turtle_click))
        score = score +1
        turtle_score.clear()
        turtle_score.write(score, align="center", font=text_font)

    if t == 0:
        turtle_countdown.write("0", align="center", font=text_font)
        turtle_instance.hideturtle()
        turtle_instance.home()
        turtle_instance.write("Oyun Bitti", align="center", font=text_font)
        break

turtle.mainloop()