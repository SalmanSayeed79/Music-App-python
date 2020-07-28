from tkinter import *
from tkinter import messagebox


#==========================================================MAIN FUNCTION=============================================================#
def work():
    global name
    global singer
    name=entry1.get()
    singer=entry2.get()
    #print(name,singer)
    total=name+' '+singer
    print(total)
    try:

        a=True
        #the main stuff
    except:
        messagebox.showerror('Invalid Name', 'Couldn\'t find the song.')

#=======================================================THE GUI=======================================================================#
root=Tk()


#making the titlebar
title_bar=LabelFrame(root,width=500,height=100,bg='white').grid(column=0,columnspan=3,row=0)


title_label=Label(root,text="Music App",bg='white',font=("Cambria",25))
title_label.grid(column=0,row=0)

#making the entry field
empty=Label(root,bg='#8BEFBA').grid(column=0,row=1)
empty2=Label(root,bg='#8BEFBA').grid(column=0,row=2)
label1=Label(root,bg='#8BEFBA',font=('Cambria',10),text="Song you want to search:").grid(column=0,row=3)
entry1=Entry(root,width=40,font=('Cambria',10))
entry1.grid(column=1,row=3)
empty3=Label(root,bg='#8BEFBA',font=('Cambria',10)).grid(column=0,row=4)
label2=Label(root,bg='#8BEFBA',font=('Cambria',10),text="The singer (optional):").grid(column=0,row=5)
entry2=Entry(root,width=40,font=('Cambria',10))
entry2.grid(column=1,row=5)

#making the button
empty4=Label(root,bg='#8BEFBA').grid(column=0,row=6)
empty5=Label(root,bg='#8BEFBA').grid(column=0,row=7)
button1=Button(root,font='Cambria',fg='white',bg='#8AD4C0',text="Search",command=work,padx=15,pady=10).grid(column=1,row=8)

#making the footer
#footer=Frame(root,width=500,height=25).pack(side=BOTTOM)
#title_label=Button(footer,text="Music App",font=("Cambria",25))

root.configure(bg='#8BEFBA')
root.title('Music App')
root.geometry('500x500')
root.iconbitmap('main.ico')
root.resizable(False,True)
root.mainloop()