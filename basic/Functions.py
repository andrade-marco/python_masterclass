# Functions
import tkinter
import math

def python_food():
    width = 80
    text = 'Spam and eggs'
    separator = (width - len(text)) // 2
    print('-' * separator, text, '-' * separator)


def center_text(text):
    text = str(text)
    separator = (80 - len(text)) // 2
    print('-' * separator, text, '-' * separator)


def multiple_text(*params):
    text = ''
    for param in params:
        text += str(param) + ' '
    separator = (80 - len(text)) // 2
    print('-' * separator, text, '-' * separator)


def text_with_named(*params, sep=',', end='\n'):
    text = ''
    for param in params:
        text += str(param) + ' '
    num = (80 - len(text)) // 2
    print(sep * num, text, sep * num, end=end)


center_text('Hello')
center_text('Spam and eggs')
center_text('Spam, spam, and more spam')
center_text(206)
multiple_text('hello', 'world')
text_with_named('This is a test', sep='*')


# Parabola
def parabola(graphArea, size):
    for x in range(size):
        y = x * x / size
        plot(graphArea, x, y)
        plot(graphArea, -x, y)


def circle(graphArea, radius, g, h):
    graphArea.create_oval(g + radius, h + radius, g - radius, h - radius, outline='red', width = 2)
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
    #     plot(graphArea, x, y)
    #     plot(graphArea, x, 2 * h - y)
    #     plot(graphArea, 2 * g - x, y)
    #     plot(graphArea, 2 * g - x, 2 * h - y)


def draw_axes(graphArea):
    graphArea.update()
    x_origin = graphArea.winfo_width() / 2
    y_origin = graphArea.winfo_height() / 2
    graphArea.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    graphArea.create_line(-x_origin, 0, x_origin, 0, fill='black')
    graphArea.create_line(0, y_origin, 0, -y_origin, fill='black')


def plot(graphArea, x, y):
    graphArea.create_line(x, -y, x + 1, -y + 1, fill='red')


root = tkinter.Tk()
root.title('Parabola')
root.geometry('640x480')

canvas = tkinter.Canvas(root, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)
parabola(canvas, 200)
parabola(canvas, 100)
circle(canvas, 100, 100, 100)

root.mainloop()
