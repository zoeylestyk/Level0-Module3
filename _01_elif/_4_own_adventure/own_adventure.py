from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    intro = messagebox.askyesno(title = 'Adventure time!!', message= "Do you want to go an adventure?")
    if intro == True:
        good = messagebox.showinfo(title = "Good", message= "Good choice")
    elif intro == False:
        toobad = messagebox.showinfo(title= "Bad", mesage= "Too bad, you\'re going on an adventure!")
    message = messagebox.askint(title= 'Start', message= "Your pet raccoon has been stolen and you\'ve come up with a list of possible suspects:\n"
                                                            "1. Adrian\n 2. Skyler\n 3.Megan\n and 4. Steve\n Select who you would like to interrogate.")
    if message == 1:
        suspect1 = messagebox.askyesno(title= "Suspect#1", message= "Adrian says he was busy helping his mom pick lemons in the garden and couldn't have stolen your raccoon. Do you believe him?")
        if suspect1 == True:
            answer= messagebox.showinfo(title= "Right Answer", message= "You seem to be right, seeing as Adrian has a yellow lemon juice stain on his shoes.")


# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story

