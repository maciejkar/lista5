import turtle

def snowflake(length = 300 , level = 3, speed=5):
    def draw_koch_line(length,level):
        if level == 0:
            turtle.forward(length)
            return
        length /= 3
        draw_koch_line(length, level -1)
        turtle.left(60)
        draw_koch_line(length, level -1)
        turtle.right(120)
        draw_koch_line(length, level -1)
        turtle.left(60)
        draw_koch_line(length, level -1)

    turtle.penup()
    turtle.speed(speed)
    turtle.goto(-length/2,length/2)
    turtle.pendown()
    for _ in range(3):
        draw_koch_line(length,level)
        turtle.right(120)
    turtle.done()

if __name__ == '__main__':
    snowflake(speed=1000, level= 4)
