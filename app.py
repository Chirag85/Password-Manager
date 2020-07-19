from tkinter import *
import sqlite3

app = Tk()
app.withdraw()
app.title('Password Manager')
app.geometry("650x600")

class win(object):
    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Input Password')
        top.geometry('{}x{}'.format(300, 100))
        top.resizable(width=False, height=False)
        self.l = Label(top, text=" Password: ", font=('Courier', 14), justify=CENTER)
        self.l.pack()
        self.e = Entry(top, show='*', width=30)
        self.e.pack(pady=7)
        self.b = Button(top, text='Submit', command = self.check,font=('Courier', 14))
        self.b.pack()
    def check(self):
        file = open("userlogondata.txt", "r")
        if file.read() == self.e.get():
            print ("Complete sucsessfull!")
            app.deiconify()
        else:
            print ("Error: (Incorrect value entered)")


def onSubmit():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    try:
        c.execute("""
        CREATE TABLE info(
        name text,
        email text,
        password text
        )
        """)
    except:
        c.execute("""
        INSERT INTO info VALUES(
        :name,:email,:pass
        )
        """,
        {
        'name':name.get(),
        'email':email.get(),
        'pass':password.get()
        })
        print('Successfully Added')

    conn.commit()
    conn.close()

def showls():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM info")
    results = c.fetchall()
    records =''
    for result in results:
        records += str(result)+'\n'


    name_label2 = Label(app, text='Name: ', font=('Courier', 14))
    email_label2 = Label(app, text='Email: ', font=('Courier', 14))
    pass_label2 = Label(app, text='Password: ', font=('Courier', 14))
    id_label2 = Label(app, text='ID: ', font=('Courier', 14))

    name_label2.grid(row=8,column = 0)
    email_label2.grid(row=8, column=1)
    pass_label2.grid(row=8, column=2)
    id_label2.grid(row=8, column=3)

    query_label = Label(app,text = records,font=('Courier', 14))
    query_label.grid(row = 9 ,column = 0 ,columnspan = 3)

    print(results)
    conn.commit()
    conn.close()

def deleteR():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE FROM info WHERE oid = "+ delete.get())
    results = c.fetchall()

    print(results)
    conn.commit()
    conn.close()



m = win(app)

entity_label = Label(app, text='Add Entity', font=('Courier', 18))
name_label = Label(app, text='Website: ', font=('Courier', 14))
email_label = Label(app, text='Email: ', font=('Courier', 14))
pass_label = Label(app, text='Password: ', font=('Courier', 14))
delete_label = Label(app, text='ID Number ', font=('Courier', 14))

name = Entry(app,width=30, font=('Courier', 14))
email = Entry(app,width=30, font=('Courier', 14))
password = Entry(app,width=30, show='*', font=('Courier', 14))
delete = Entry(app, width=30,font=('Courier', 14))

submit = Button(app, text='ADD RECORD',command = onSubmit,  font=('Courier', 14))
show = Button(app, text='SHOW LIST',command = showls,  font=('Courier', 14))
delete_btn = Button(app,text="Delete Record",command=deleteR,font=('Courier', 14))

entity_label.grid(columnspan=3, row=0)
name_label.grid(row=1,column=0)
email_label.grid(row=2,column=0)
pass_label.grid(row=3,  column=0)
delete_label.grid(row=6,  column=0)


name.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
email.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
password.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)
delete.grid(columnspan=3, row=6, column=1, padx=2, pady=2, sticky=W)

submit.grid(row=4,column = 0,columnspan=2,padx=10, pady=10,ipadx=157)
show.grid(row=5,column = 0,columnspan=2,padx=10, pady=10,ipadx=163)
delete_btn.grid(row=7,column = 0,columnspan=2,padx=10, pady=10,ipadx=140)




app.mainloop()
