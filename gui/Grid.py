import tkinter

mainWindow = tkinter.Tk()

mainWindow.title('Hello World')
mainWindow.geometry('640x480+8+200')

label = tkinter.Label(mainWindow, text='Hello World')
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(row=1, column=1, sticky='ns')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.config(relief='sunken', borderwidth=1)
rightFrame.columnconfigure(0, weight=1)
rightFrame.grid(row=1, column=2, sticky='new')

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')
button1.grid(row=0, column=0)
button2.grid(row=1, column=0, sticky='ew')
button3.grid(row=2, column=0)

# configure columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)
mainWindow.mainloop()
