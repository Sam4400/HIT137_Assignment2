import turtle

from random import randint

# Returns a list with (limit) number of random hexadecimal colours
def random_colors(limit):
    return_colors = []

    x = 0

    for x in range(limit):
        ss = '#%02X%02X%02X' % (randint(0, 255), randint(0, 255), randint(0, 255))

        return_colors.append(ss)

    return return_colors


def random_spiral():
    color_count = randint(105,170)

    rainbow = random_colors(color_count)

    t = turtle

    t.tracer(0,0)

    bgcolor = random_colors(1)
    t.bgcolor(bgcolor[0])

    t.speed(4)
    #t.hideturtle()

    tp = t.Pen()

    for i in range(1000):
        tp.pencolor(rainbow[i % color_count])
        tp.forward(i)
        tp.left((360 / color_count)-color_count*4)

    t.update()

    turtle.done()


random_spiral()

