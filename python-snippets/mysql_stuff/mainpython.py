import mysql.connector
import tkinter
from tkinter import messagebox



connection = mysql.connector.connect(
    host='localhost',          
    database='hospital',
    user='vipul',      
    password='3753'
)

if connection.is_connected():
    print("Connected to MySQL database")
    cursor= connection.cursor()



main_window = tkinter.Tk()
main_window.title("mysql_database interactive GUI")
main_window.geometry("800x600")

def open_window2():
    window2 = tkinter.Toplevel(main_window)
    window2.title("Enter Patient's info")
    window2.geometry("300x250")
    labels = ["Name", "Phone", "Address", "Remarks"]


    for i in range(4):
        tkinter.Label(window2, text=labels[i]).grid(row=i,column=0)
    entry1=tkinter.Entry(window2)
    entry1.grid(row=0,column=1)
    entry2=tkinter.Entry(window2)
    entry2.grid(row=1,column=1)
    entry3=tkinter.Entry(window2)
    entry3.grid(row=2,column=1)
    entry4=tkinter.Entry(window2)
    entry4.grid(row=3,column=1)

    def submit2():
        new_val = (entry1.get(),entry2.get(),entry3.get(),entry4.get())
        query = "insert into Patient(P_Name,Phone,Address,remarks) values(%s,%s,%s,%s)"
        cursor.execute(query,new_val)
        connection.commit()
        messagebox.showinfo("notification","data saved successfully")

    submit = tkinter.Button(window2, text="Submit", command=submit2)
    submit.place(x=100,y=150)

def open_window3():
    window3 = tkinter.Toplevel(main_window)
    window3.title("Enter Patient's info")
    window3.geometry("400x400")

    input = tkinter.Entry(window3)
    id = input.get()
    def Update():
        print("")

        col_list =tkinter.Listbox(window3,selectmode=tkinter.SINGLE)
        col_name=['P_name','Phone','Address','remarks']
        for a in col_name:
            col_list.insert(tkinter.END,col_name)
        selected_column =col_list.curselection()

    button1 = tkinter.Button(window3,text="select",command=Update)

    input.place(x=60,y=60)
    button1.place(x=54,y=55)






    submit = tkinter.Button(window3, text="Submit", command=submit3)
    submit.place(x=100,y=150)




#widgets
heading = tkinter.Label(main_window,text ="Dentist HealthCare",font =("Ariel",16))

input   = tkinter.Entry(main_window,width =24)
def search():
    query="select * from Patient Where Patient_id = %s"
    id = input.get()
    cursor.execute(query,(id,))


    rows=cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    display_box.delete('1.0', tkinter.END)
    display_box.insert(tkinter.END, "\t".join(column_names) + "\n")
    for row in rows:
        display_box.insert(tkinter.END, "\t".join(str(value) for value in row) + "\n")





display_box = tkinter.Text(main_window, width=60, height=15, font=("Arial", 12))
button1 = tkinter.Button(main_window,text ="Retrive Patient info",command=search)
button2 = tkinter.Button(main_window,text ="New Patient",command=open_window2)
button3 = tkinter.Button(main_window,text ="Update Patient info",command=open_window3)




heading.pack()
input.place(x=60,y=60)
button1.place(x=540,y=55)
display_box.place(x=60,y=90)
button2.place(x=60,y=500)
button3.place(x=540,y=500)

display_box.insert(tkinter.END, "Welcome! search results will appear here.")


main_window.mainloop()






























