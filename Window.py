from tkinter import *

window = Tk()
lebar = 500
tinggi = 400

window.resizable(0,0)
window.title("Raga Chatbot")

screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

x = int ((screenwidth/2)-(lebar/2))
y = int ((screenheight/2)-(tinggi/2)-30) 

window.geometry(f"{lebar}x{tinggi}+{x}+{y}")

window.mainloop()
