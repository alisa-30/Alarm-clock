from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.configure(bg="blue")
root.title("ALARM CLOCK-12Hr clock")
C = Canvas(root,height=10,width=10)
root.resizable(False,False)
filename = ImageTk.PhotoImage(Image.open(r'alarmpic.jpg'))
background_label = Label(root,image=filename )
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.grid()
hrs=StringVar()
mins=StringVar()
secs=StringVar()
pers=StringVar()
greet=Label(root, font = ('forte', 20, 'bold'),
text="Take a short nap!").grid(row=1,columnspan=3,column=2)
hrbtn=Entry(root,textvariable=hrs,width=5,borderwidth=5,font =('arial', 20, 'bold'))
hrbtn.grid(row=3,column=1,pady=30)
minbtn=Entry(root,textvariable=mins,
width=5,borderwidth=5,font = ('arial', 20, 'bold')).grid(row=3,column=2,pady=30,padx=30)
secbtn=Entry(root,textvariable=secs,
width=5,borderwidth=5,font = ('arial', 20, 'bold')).grid(row=3,column=3,pady=30)
period=Entry(root,textvariable=pers,
width=5,borderwidth=5,font = ('arial', 20, 'bold')).grid(row=3,column=4,pady=30,padx=30)
from datetime import datetime
from playsound import playsound
def validate_time():
    alarm_time=f"{hrs.get()}:{mins.get()}:{secs.get()}:{pers.get()}"
    if len(alarm_time) != 11:
        from tkinter import messagebox
        messagebox.showerror("ERROR", "Invalid HOUR format! Please try again.. ")
    else:
        if int(alarm_time[0:2]) > 12:
            from tkinter import messagebox
            messagebox.showerror("ERROR", "Invalid HOUR format! Please try again.. ")
        elif int(alarm_time[3:5]) > 59:
            from tkinter import messagebox
            messagebox.showerror("ERROR", "Invalid MINUTE format! Please try again.. ")
        elif int(alarm_time[6:8]) > 59:
           from tkinter import messagebox 
           messagebox.showerror("ERROR", "Invalid SECOND format! Please try again.. ")
        else:
            alarmclock(alarm_time)       
def alarmclock(alarm_time):    
        alarm_hour = alarm_time[0:2]
        alarm_min = alarm_time[3:5]
        alarm_sec = alarm_time[6:8]
        alarm_period=alarm_time[9:].upper()
        while True:
            now = datetime.now()
            current_hour = now.strftime("%I")
            current_min = now.strftime("%M")
            current_sec = now.strftime("%S")
            current_period = now.strftime("%p")
            if alarm_sec == current_sec and alarm_period == current_period and alarm_hour == current_hour and alarm_min == current_min :
                playsound('alarm.wav')
                from tkinter import messagebox
                messagebox.showinfo("INFO", "WAKE UP")
                root.destroy()
                break
greet1=Label(root, font = ('arial', 13, 'bold'),
text="HOUR").grid(row=4,column=1)
greet2=Label(root, font = ('arial', 13, 'bold'),
text="MIN").grid(row=4,column=2)
greet3=Label(root, font = ('arial', 13, 'bold'),
text="SEC").grid(row=4,column=3)
greet4=Label(root, font = ('arial', 13, 'bold'),
text="AM/PM").grid(row=4,column=4)
Button(root,text="SET ALARM",foreground ="blue",command=validate_time,font = ("Forte", 13)).grid(row = 10,pady=70,column=2)  
mainloop() 
