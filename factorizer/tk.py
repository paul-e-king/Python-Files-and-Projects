import subprocess # for me to muck about with shell output to a window
from tkinter import * # the real deal

def mkWindow(r):
    minX = minY = 200
    maxX = maxY = 500
    title = "This is my window title"
    bgColour = "dodgerblue" # can be any of the 200 or so X-windows named colours

    r.title(title)
    r.configure(background=bgColour)
    r.minsize(minX,minY)
    r.maxsize(maxX,maxY)
    r.geometry("300x300+2050+50") # width x height + x + y

def text_clicked(event):
    # Here, all we are doing is responding to a click event on the Fortune label (fortText).
    msg = subprocess.check_output(["/usr/games/fortune", "-s"])
    fortText.config(text = msg, width="400")

root = Tk()
mkWindow(root)

text = Label(root, text="Nothing will work unless you do.")
text.pack()

text2 = Label(root, text="Maya Angelou")
text2.pack()

# send the output of a command to a label
msg = subprocess.check_output(["/usr/games/fortune", "-s"])
fortText = Label(root, text=msg, justify="left", width="400")
fortText.pack()
fortText.bind("<Button-1>", text_clicked)

# output of another command
msg2 = subprocess.check_output(["ls", "-s"])
text4 = Label(root, text=msg2, justify="left")
text4.pack()

root.mainloop()
