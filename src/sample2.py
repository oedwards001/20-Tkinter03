import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master = window, width = 200, bg = "red")
frame1.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

frame2 = tk.Frame(master = window, width = 100, bg = "yellow")
frame2.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

frame3 = tk.Frame(master = window, width = 25, bg = "blue")
frame3.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

window.mainloop