import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# Done: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 2. (4 pts)
#
#   Now, create one frame dimensions 200 by 200.
#
#   Use the default pack() method to place it in the window.
#
#   Also, place 3 labels in the frame labeling them as Label A, Label B, and
#   Label C and give them different background colors.
#
#   Use the place() method to place each of these labels at different
#   coordinates such that they do not overlap.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################
window = tk.Tk()

frame1 = tk.Frame(master = window, height = 200, width = 200)
frame1.pack()

LabelA = tk.Label(master = frame1, bg = "red")
LabelA.place(x = 10, y = 20)

LabelB = tk.Label(master = frame1, bg = "blue")
LabelB.place(x = 20, y = 40)

LabelC = tk.Label(master = frame1, bg = "yellow")
LabelC.place(x = 40, y = 80)

window.mainloop()