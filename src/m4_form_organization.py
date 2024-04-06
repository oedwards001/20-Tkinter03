###############################################################################
# Done: 1. (5 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 18 and
#   paste it below.
#
#   Now, use the geometry managers we have learned about and reorganize/
#   reformat your fillable form. You must use more than just the pack() method,
#   but you can still use it if it is what you need in a certain spot.
#
#   You may need to add more frames and such to move things around effectively.
#
#   Feel free to be creative on how you want your form to look.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
import tkinter as tk

window = tk.Tk()

window.columnconfigure([0, 1], weight = 1, minsize = 75)
window.rowconfigure([0, 1, 2, 3, 4, 5], weight = 1, minsize = 75)

window.title("Form")

Frame1 = tk.Frame(master = window)

Frame1Label = tk.Label(master = Frame1, text = "Enter Your Personal Information Below:")
Frame1Label.pack()

Frame1Label2 = tk.Label(Frame1, text = "Name:", fg = "red").pack()
tk.Entry(Frame1).pack()

Frame1Label3 = tk.Label(Frame1, text = "Phone Number:", fg = "DodgerBlue").pack()
tk.Entry(Frame1).pack()

tk.Label(Frame1, text = "Email Address:", fg = "Navy").pack()
tk.Entry(Frame1).pack()

Frame1.grid(row = 0, column = 0, padx = 5, pady = 20, sticky = "nsew")

button = tk.Button(Frame1, text ="Submit", fg = "black")
button.pack()

Frame2 = tk.Frame(master = window)

Frame2Label = tk.Label(master = Frame2, text = "Enter Your Address Information Below:")
Frame2Label.pack()

tk.Label(Frame2, text = "Address Line 1:", fg = "orange").pack()
tk.Entry(Frame2).pack()

tk.Label(Frame2, text = "Address Line 2:", fg = "gold").pack()
tk.Entry(Frame2).pack()

tk.Label(Frame2, text = "City:", fg = "olive").pack()
tk.Entry(Frame2).pack()

tk.Label(Frame2, text = "State:", fg = "green").pack()
tk.Entry(Frame2).pack()

tk.Label(Frame2, text = "Zip Code:", fg = "Aqua").pack()
tk.Entry(Frame2).pack()

Frame2.grid(row = 0, column = 1, padx = 5, pady = 20, sticky = "nsew")

button = tk.Button(Frame2, text ="Submit", fg = "black")
button.pack()

window.mainloop()