import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("pop-up venster")
window.geometry("300x200")
label = tkinter.Label(window, text="Wat doet deze knop???")
label.pack()

def toon_messagebox():
    messagebox.showinfo("boodschap", "je code werkt!")

knop = tkinter.Button(window, text="Klik hier voor een boodschap!!!", command=toon_messagebox)
knop.pack()

window.mainloop()