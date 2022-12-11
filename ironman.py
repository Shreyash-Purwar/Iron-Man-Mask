import turtle
part1=[[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],[(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]]
part2=[[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210)],[(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]]
part3=[[(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],[(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240), (60, -220), (0, -220)]]
turtle.hideturtle()
turtle.bgcolor('#ba161e')
turtle.setup(500,600)
turtle.title("I AM IRONMAN")
part1op=(0,120)
part2op=(0,-30)
part3op=(0,-220)
turtle.speed(2)
def draw_piece(part, partop):
    turtle.penup()
    turtle.goto(partop)
    turtle.pendown()
    turtle.color('#fab104') 
    turtle.begin_fill()
    for i in range(len(part[0])):
        x,y=part[0][i]
        turtle.goto(x,y)

    for i in range(len(part[1])):
        x,y=part[1][i]
        turtle.goto(x,y)
    turtle.end_fill()
draw_piece(part1,part1op)
draw_piece(part2,part2op)
draw_piece(part3,part3op)
turtle.hideturtle()
turtle.done()
