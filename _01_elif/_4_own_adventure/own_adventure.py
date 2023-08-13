from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    intro = messagebox.askyesno(title = 'Adventure time!!', message= "Do you want to go an adventure?")
    if intro:
        good = messagebox.showinfo(title = "Good", message= "Good choice")
    elif not intro:
        too_bad = messagebox.showinfo(title= "Bad", mesage= "Too bad, you\'re going on an adventure!")

    right_answer = False
    while right_answer:
        message = simpledialog.askstring(title= 'Start', prompt= "Your pet raccoon has been stolen and you've come up with a list of possible suspects:\n"
                                                                "1. Adrian\n\n 2. Skyler\n\n 3.Megan\n\n 4. Carmen\n\n Select who you would like to interrogate.")
        if message == 1:
            suspect1 = simpledialog.askyesno(title= "Suspect#1", prompt= "Adrian says he was busy helping his mom pick oranges in the garden and couldn't have stolen your raccoon. Do you believe him?")
            if suspect1:
                answer = messagebox.showinfo(title= "Right Answer", message= "You seem to be right, seeing as Adrian has a orange juice stain on his shoes.")
            elif not suspect1:
                answer = messagebox.showinfo(title = "Wrong Answer", message = "You seem to be wrong and Adrian clearly seems hurt that you'd suspect him. He hands you a basket of fresh oranges as further proof.")

        elif message == 2:
            suspect2 = simpledialog.askyesno(title= "Suspect#2", prompt = "Skyler says they were busy dealing with a dispute with their little brother. Do you believe them")
            if not suspect2:
                answer = messagebox.showinfo(title= "Right Answer", message= "The raccoon in question comes waddling around the corner from Skyler's bedroom. Skyler apologies and says they only meant to borrow 'em.")
                right_answer = True
                break
            elif suspect2:
                answer = messagebox.showinfo(title= "Wrong Answer", message= "The raccoon in question comes waddling around the corner from Skyler's bedroom. Skyler apologies and says they only meant to borrow 'em.")

        elif message == 3:
            suspect3 = simpledialog.askyesno(title= "Suspect#3", prompt = "Megan says she was busy going shopping with her friends and was able to cop some really cute pieces. Do you believe her?")
            if not suspect3:
                answer = messagebox.showinfo(title= "Wrong Answer", message= "Megan feels hurt that you would ever suspect her and shows the new cute outfit as proof.")
            elif suspect3:
                answer = messagebox.showinfo(title= "Right Answer", message= "You seem to be right, as you can see her new clothes hung up on a clothing rack nearby.")
        elif message == 4:
            suspect4 = simpledialog.askyesno(title= "Suspect#4", prompt = "Carmen says she was busy painting and couldn't have stolen your raccoon. Do you believe her?")
            if suspect4:
                answer = messagebox.showinfo(title= "Right Answer", message = "You were right to believe her, as you can see fresh paint on her hands and arms. She suggests interrogating Skyler.")
            elif not suspect4:
                answer = messagebox.showinfo(title= "Wrong Answer", message = "You seem to be wrong as Carmen has fresh paint dripping from her hands but she also doesn't blame you for suspecting her because she really loves your pet raccoon.")

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story

