import turtle

def hilbert_line(level = 4,angle =90, size =300 , speed = 5):


    def draw_hilbert_line(level, angle, step):
        if level == 0:
            return
        turtle.right(angle)
        draw_hilbert_line(level - 1, -angle, step)

        turtle.forward(step)
        turtle.left(angle)
        draw_hilbert_line(level - 1, angle, step)

        turtle.forward(step)
        draw_hilbert_line(level - 1, angle, step)

        turtle.left(angle)
        turtle.forward(step)
        draw_hilbert_line(level - 1, -angle, step)
        turtle.right(angle)
    
    turtle.penup()
    turtle.speed(speed)
    turtle.goto(-size/2, size/2)
    turtle.pendown()
    draw_hilbert_line(level , angle, size/(2**level -1))
    turtle.done()


if __name__ == '__main__':
    hilbert_line()
