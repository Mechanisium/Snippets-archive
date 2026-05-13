import tkinter as tk

#calcwindow
calcwindow=tk.Tk()
calcwindow.title('product sheet')
calcwindow.geometry('500x250+10+20')


#assigning variables

provar=tk.StringVar()
quavar=tk.StringVar()




try:
    from pricetag import *

except:
    print('file not found')
    
    
    
    
label1=tk.Label(calcwindow,text='Product',font=['quicksand',20,'bold'])

label2=tk.Label(calcwindow,text='Quantity',font=['quicksand',20,'bold'])





entry1=tk.Entry(calcwindow,textvariable=provar,font=['suranna',18])

entry2=tk.Entry(calcwindow,textvariable=quavar,font=['suranna',18])



def moneyfind():
    qua=''
    intpro=''
    pro=provar.get()
    qua=quavar.get()
    rat=''
    
    if pro in product:
        intpro=int(product[pro])
        out=tk.Label(calcwindow,text=intpro*int(qua),font=['calibri',28,'bold'])
        out.grid(row=5,column=0)
        
        
        rat='Rate of '+pro+' =>'+str(product[pro])+'rupees'
        label3=tk.Label(calcwindow,text=rat,font=['quicksand',20,'bold'])
        label3.grid(row=2,column=0)
        
        
    else:
      
        noitems=tk.Label(calcwindow,text='!!!no such items!!!',font=['calibri',28,'bold'])
        noitems.grid(row=4,column=0)
    
    
    provar.set('')
    quavar.set('')

gobutton=tk.Button(calcwindow,text='Enter',font=['calibri',20,'bold'],command=moneyfind)


'''
def showrat():
    ratewindow=tk.Toplevel(calcwindow)
    ratewindow.geometry('300x200+10+10')
    
    ratelabel=tk.Label(ratewindow,text=product,font=["ariel",20])
    ratelabel.grid(row=0,column=0)
    
    
ratebutton=tk.Button(calcwindow,text='show rate',font=['calibri',18],command=showrat)
'''


#placing stuff on the window
label1.grid(row=1,column=0)
label2.grid(row=3,column=0)
entry1.grid(row=1,column=2)
entry2.grid(row=3,column=2)
gobutton.grid(row=4,column=0)
#ratebutton.grid(row=4,column=0)



calcwindow.mainloop()



















