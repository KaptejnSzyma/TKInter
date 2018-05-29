try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter
mainWindow = tkinter.Tk()

mainWindow.title('Calculator')
mainWindow.geometry('200x200')
mainWindow.resizable(False, False)
mainWindow['padx'] = 10

buttons = [['CE', 'C'], ['7', '8', '9', '+'], ['4', '5', '6', '-'], ['1', '2', '3', '*'], ['0', '=', '/']]

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=1,  columnspan=5, sticky='nsew')

for r in range(0, 5):
    for b in range(len(buttons[r])):
        tkinter.Button(mainWindow, text=buttons[r][b]).grid(row=r+1, column=b)


mainWindow.mainloop()
