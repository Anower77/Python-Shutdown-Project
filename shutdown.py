from tkinter import *
import os 

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("Anower Hossan")
st.geometry("500x500")
st.config(bg="red")


# Restart
r_button = Button(st,text="Restart", font=("Time New Roman", 20, "bold"),
    relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

# Restart time
rt_button = Button(st,text="Restart Time", font=("Time New Roman", 20, "bold"),
    relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

# Log out
lg_button = Button(st,text="Log Out", font=("Time New Roman", 20, "bold"),
    relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

# shutdown
lg_button = Button(st,text="Shut Down", font=("Time New Roman", 20, "bold"),
    relief=RAISED,cursor="plus",command=shutdown)
lg_button.place(x=150,y=370,height=50,width=200)


st.mainloop()