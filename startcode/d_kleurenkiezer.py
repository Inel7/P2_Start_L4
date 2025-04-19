import tkinter
from tkinter import colorchooser

window = tkinter.Tk()
window.title("Kleurkiezer Oefening")
window.geometry("300x200")

def kies_kleur():
    kleur = colorchooser.askcolor()[1]
    if kleur:
        knop.config(bg=kleur)  # Je kan hier ook window gebruiken i.p.v. knop

knop = tkinter.Button(window, text="Kies een kleur!", command=kies_kleur)
knop.pack()

window.mainloop()