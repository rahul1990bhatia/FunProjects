from tkinter import *
from generate_qr import *

def show_qr(link):
    qrcode_generator(link)

root = Tk()
root.geometry("500x400")
frame = Frame(root)
frame.pack()

label = Label(frame, text = "Quick QR Code Generator")
label.pack()

my_entry = Entry(frame, width = 100)
my_entry.insert(0,'paste your link here...')
my_entry.pack(padx = 10, pady = 10)

canvas = Canvas(root, width=200, height=200)
canvas.pack()
image = PhotoImage(file='qrcode.jpg')


button = Button(frame, text = "Generate", command = show_qr(my_entry.get()))
button.pack()


root.title("QR Code Generator")
root.mainloop()