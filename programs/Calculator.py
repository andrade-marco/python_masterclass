# Calculator interface
import tkinter

root = tkinter.Tk()
root.title('Calculator')
root.geometry('350x350-8-200')
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.maxsize(500, 500)
root['padx'] = 8
root['pady'] = 8

for i in range(0, 4):
    root.columnconfigure(i, weight=1)
for i in range(0, 6):
    root.rowconfigure(i, weight=1)

# Result field
tkinter.Entry(root).grid(row=0, column=0, columnspan=4, sticky='nsew')

# Buttons
textCount = 0
buttonText = ('7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'X')
for i in range(1, 6):
    if i == 1:
        tkinter.Button(root, text='C').grid(row=1, column=0, sticky='nsew')
        tkinter.Button(root, text='CE').grid(row=1, column=1, sticky='nsew')
    elif i == 5:
        tkinter.Button(root, text='0').grid(row=5, column=0, sticky='nsew')
        tkinter.Button(root, text='=').grid(row=5, column=1, columnspan=2, sticky='nsew')
        tkinter.Button(root, text='/').grid(row=5, column=3, sticky='nsew')
    else:
        for j in range(0, 4):
            tkinter.Button(root, text=buttonText[textCount]).grid(row=i, column=j, sticky='nsew')
            textCount += 1

# Render mainWindow
root.mainloop()
