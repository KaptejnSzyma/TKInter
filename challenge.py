try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter
mainWindow = tkinter.Tk()

mainWindow.title('Calculator')
mainWindow.geometry('200x200')
mainWindow.resizable(False, False)
mainWindow['padx'] = 10
buttons1 = ['CE', 'C']
buttons2 = ['7', '8', '9', '+']
buttons3 = ['4', '5', '6', '-']
buttons4 = ['1', '2', '3', '*']
buttons5 = ['0', '=', '/']
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=1,  columnspan=3, sticky='nsew')

for b in range(len(buttons1)):
    tkinter.Button(mainWindow, text=buttons1[b]).grid(row=1, column=b)
for b in range(len(buttons2)):
    tkinter.Button(mainWindow, text=buttons2[b]).grid(row=2, column=b)
for b in range(len(buttons3)):
    tkinter.Button(mainWindow, text=buttons3[b]).grid(row=3, column=b)
for b in range(len(buttons4)):
    tkinter.Button(mainWindow, text=buttons4[b]).grid(row=4, column=b)
for b in range(len(buttons5)):
    tkinter.Button(mainWindow, text=buttons5[b]).grid(row=5, column=b)

mainWindow.mainloop()
