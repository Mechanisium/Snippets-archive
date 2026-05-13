import tkinter
from tkinter import messagebox
import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    database='student',
    user='vipul',
    password='3753'
)

if connection.is_connected():
    print("Connected to MySQL database")
    cursor= connection.cursor()



main_window = tkinter.Tk()
main_window.title("mysql_database interactive GUI")
main_window.geometry("800x600")








#widgets
heading = tkinter.Label(main_window,text ="Student Registration Form",font =("Ariel",18))

entry1 = tkinter.Entry(main_window,width = 25)
entry2 = tkinter.Listbox(main_window,selectmode = 'single',height = 5,exportselection=False)
course = ["MCA","MTECH","MBA","MSC","MA"]
for each_course in course:
    entry2.insert(tkinter.END,each_course)

entry3 = tkinter.Entry(main_window,width = 18)
entry4 = tkinter.Entry(main_window,width = 35)
entry5 = tkinter.Listbox(main_window, selectmode='single',height = 3,exportselection=False)
items = ["Male","Female"]
for each_gender in items:
    entry5.insert(tkinter.END, each_gender)

def submit():

    new_val = (entry1.get(),entry2.get(entry2.curselection()[0]),entry3.get(),entry4.get(),entry5.get(entry5.curselection()[0]))
    query = "insert into student_r values(%s,%s,%s,%s,%s)"
    cursor.execute(query,new_val)
    connection.commit()
    messagebox.showinfo("notification","data saved successfully")


label1 = tkinter.Label(main_window,text ="Student Name: ",font = ("Ariel",14))
label2 = tkinter.Label(main_window,text ="Course: ")
label3 = tkinter.Label(main_window,text ="Phone Number: ")
label4 = tkinter.Label(main_window,text ="Email Id: ")
label5 = tkinter.Label(main_window,text ="Gender: ")
submit_button = tkinter.Button(main_window,text = "SUBMIT",command =submit)












heading.pack()
label1.place(x=60,y=60)
entry1.place(x=280,y=60)

label2.place(x=480,y=120)
entry2.place(x=560,y=120)

label3.place(x=60,y=120)
entry3.place(x=200,y=120)

label4.place(x=60,y=180)
entry4.place(x=200,y=180)

label5.place(x=60,y=240)
entry5.place(x=300,y=240)

submit_button.place(x=360,y=360)

main_window.mainloop()




















