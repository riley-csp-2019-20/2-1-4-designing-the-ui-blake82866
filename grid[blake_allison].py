import tkinter as tk 

root = tk.Tk()

root.wm_geometry("400x300")

frame1 = tk.Frame(root)
frame1.config(width=250, height=200, bg = "blue")
frame1.grid(row = 0, column = 0)

frame2 = tk.Frame(root)
frame2.config(width=250, height=100, bg = "yellow")
frame2.grid(row = 5, column = 2)

frame3 = tk.Frame(root)
frame3.config(width=250, height=100, bg = "red")
frame3.grid(row = 5, column = 0)

frame4 = tk.Frame(root)
frame4.config(width=250, height=200, bg = "green")
frame4.grid(row = 0, column = 2)

root.mainloop()