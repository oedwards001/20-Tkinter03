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
#   Now, create two different frames with different dimensions (width and
#   height) and different background colors.
#
#   Use the default pack() method to place them in the window.
#
#   Now, modify your code to make these two frames responsive in all
#   directions. Remember that these frames will no longer need a width and
#   height. You should use the fill, side, and expand keywords in your pack
#   method.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################
import tkinter as tk
window = tk.Tk()

frame1 = tk.Frame(master = window, bg = "red")
frame1.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

frame2 = tk.Frame(master = window, bg = "yellow")
frame2.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

window.mainloop()