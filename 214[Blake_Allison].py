
##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 250 pixels.
##############################################################################
import tkinter as tk

# functions
def test_my_botton():
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_display_pass.config(text=password)

# main window
root = tk.Tk()
root.wm_geometry("300x200")
root.title("Authentication")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row = 0, column = 0, sticky = "news")

#create a username label
lbl_username = tk.Label(frame_login, text='Username:', font="courier")
lbl_username.pack()

#create place to enter username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=15, padx=85)

#write password in the frame
lbl_password = tk.Label(frame_login, text='Password:', font="courier")
lbl_password.pack()

#create place to write password
ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(padx=85, pady=15)

#create login button
btn_login = tk.Button(frame_login, text="login", command = test_my_botton)
btn_login.pack()

#create secound frame behind first
frame_auth = tk.Frame(root)
frame_auth.grid(row = 0, column = 0, sticky = "news")

#raise first frame to the top
frame_login.tkraise()

#Add a label to frame auth
lbl_display_pass = tk.Label(frame_auth, text="password", font="courier")
lbl_display_pass.pack()

root.mainloop()