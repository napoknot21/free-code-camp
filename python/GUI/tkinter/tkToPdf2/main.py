import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

root = tk.Tk()


canvas = tk.Canvas(
    root,
    width=600,
    height=300,
    bg="white"
)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('userphoto.jpeg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(
    image=logo,
    bg="white"
)
logo_label.image = logo
logo_label.grid(column=1, row=0)


#instructions
instructions = tk.Label(
    root, 
    text="Select a pdf file on your computer to extract all its text",
    font="Raleway",
    bg="white"
)
instructions.grid(columnspan=3, column=0, row=1)

#browser button
browse_text = tk.StringVar()
browse_btn = tk.Button(
    root,
    textvariable=browse_text,
    font="Raleway"
)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

root.mainloop()
