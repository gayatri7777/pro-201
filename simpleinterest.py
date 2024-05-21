from tkinter import *
window=Tk()

window.title('Simple Interest')
window.geometry("300x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p = float(principle_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100
    interest = round(i, 2)
    
    
app_label=Label(window, text="Simple Interest", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principle_label=Label(window, text="Enetr principle interest", fg = "black", bg="lightcyan",font=("Calibri", 12),bd=1)
principle_label.place(x=20,y=90)

principle_entry=Entry(window, text="", bd = 2, width=15)
principle_entry.place(x=150, y=142)

rate_label=Label(window, text="Enter the rate of interest",fg = "black",  bg = "lightcyan", font= ("calibri", 12))
rate_label.place(x= 120, y=185)

rate_entry=Entry(window, text="", bd=2, width=15)
rate_entry.place(x=150, y=186)

time_label = Label(window, text="Enter the time taken", fg = "black", bg="cyan", font = ("calibri", 12))
time_label.place(x= 10, y = 186)

time_entry = Entry(window, text="",bd=2, width = 15)
time_entry.place(x=150, y=187)



result_frame = LabelFrame(window, text="result", bg = "grey", font=("calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

showlabel = Label(result_frame,text="your result will be displayed here", bg = "grey", font=("calibri, 12"))
showlabel.place(x=20, y=20)
showlabel.pack()

message=Label(result_frame, text="Interest on it."+str(p)+"at rate of interest"+str(r)+"N for "+str(t)+"yours in Rs"+str(interest),bg = "gray", font=("calibri",12),width = 55)
message.place(x=33, y=33)
message.pack()

window.mainloop()







