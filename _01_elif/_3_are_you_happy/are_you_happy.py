from tkinter import Tk, simpledialog, messagebox
#import tkinter as tk
#from tkinter import ttk
#from tkinter.messagbox import askyesno


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    #message = simpledialog.askstring(title = 'Big Question', prompt = "Are you happy?")
    yes = messagebox.askyesno(title = 'Big Question', message = 'Are you happy?')
    if yes == True:
        messageyes1 = messagebox.askyesno(title='Question#2', message='Keep doing whatever you\'re doing')
        exit()
    elif yes == False:
        messageno11 = messagebox.askyesno(title='Question#2.0', message='Do you want to be happy?')
        if messageno11 == True:
            messageno2 = messagebox.showinfo(title='Final remarks', message= 'Change something.')
            exit()
        elif messageno11 == False:
            messageyes1 = messagebox.askyesno(title='Question#2', message='Keep doing whatever you\'re doing')
            exit()

    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements

    pass
