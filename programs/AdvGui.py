import os
import tkinter

mainWindow = tkinter.Tk()
mainWindow.title('Grid Demo')
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8

# Configuring mainWindow columns and rows
colWeights = (100, 1, 1000, 600, 1000)
rowWeights = (1, 10, 1, 3, 3)
for i in range(0, 5):
    mainWindow.columnconfigure(i, weight=colWeights[i])
    mainWindow.rowconfigure(i, weight=rowWeights[i])

# Setting up components
label = tkinter.Label(mainWindow, text='Tkinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)

fileList = tkinter.Listbox(mainWindow)
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
fileList.config(border=2, relief='sunken')
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

for zone in os.listdir('/usr/bin'):
    fileList.insert(tkinter.END, zone)

# Frame for radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

# Variable to define which button is selected
rbValue = tkinter.IntVar()
rbValue.set(0)

# Creating radio buttons
radioButtons = {}
content = ['Filename', 'Path', 'Timestamp']
for i in range(0, 3):
    radioButtons[i] = tkinter.Radiobutton(optionFrame, text=content[i], value=i, variable=rbValue)
    radioButtons[i].grid(row=i, column=0, sticky='w')

# Input field
resultLabel = tkinter.Label(mainWindow, text='Result')
result = tkinter.Entry(mainWindow)
resultLabel.grid(row=2, column=2, sticky='nw')
result.grid(row=2, column=2, sticky='sw')

# Frame for spinners
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
dateFrame = tkinter.Frame(mainWindow)
timeFrame.grid(row=3, column=0, sticky='new')
dateFrame.grid(row=4, column=0, sticky='new')
timeFrame['padx'] = 36

# Date and time spinners
timeSpinners = {}
dateLabels = {}
dateSpinners = {}
labelValues = ('Day', 'Month', 'Year')
monthsAbbr = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
for i in range(0, 3):
    # Time
    time_to_value = 23 if i == 0 else 59
    time_col_value = i if i == 0 else i * 2
    timeSpinners[i] = tkinter.Spinbox(timeFrame, width=2, from_=0, to=time_to_value)
    timeSpinners[i].grid(row=0, column=time_col_value)

    # Date
    dateLabels[i] = tkinter.Label(dateFrame, text=labelValues[i])
    dateLabels[i].grid(row=0, column=i, sticky='w')
    date_from_value = 1 if i == 0 else 2000
    date_to_value = 31 if i == 0 else 2099
    if i == 1:
        dateSpinners[i] = tkinter.Spinbox(dateFrame, width=5, values=monthsAbbr)
    else:
        dateSpinners[i] = tkinter.Spinbox(dateFrame, width=5, from_=date_from_value, to=date_to_value)

    dateSpinners[i].grid(row=1, column=i)

# Separators
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)

#Buttons
okButton = tkinter.Button(mainWindow, text='OK')
cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

# Render mainWindow
mainWindow.mainloop()
