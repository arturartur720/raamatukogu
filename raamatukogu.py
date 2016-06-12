from tkinter import *
root=Tk()
       
root.title('Raamatukogu')
root.geometry('300x300')
root.resizable(False, False)
nimi=StringVar()
kniga=StringVar()
isiktxt1=Entry(root, width=10,textvariable=nimi)
isiktxt1.grid(row=1,column=1)
nkniga=Entry(root, width=10,textvariable=kniga)
nkniga.grid(row=6,column=1)

listbox1=Listbox(width=15,selectmode=SINGLE)
listbox2=Listbox(width=15,selectmode=SINGLE)

list2=open('raamatud.txt')
for k in list2:
        listbox2.insert(END,k)
list2.close()

listbox1.grid(row=3,column=0)
listbox2.grid(row=3,column=2)
lbl1=Label(root, text='Введите имя: ')
lbl1.grid(row=1,column=0)
lbl2=Label(root, text='Книги y Вас: ')
lbl2.grid(row=2,column=0)
lbl3=Label(root, text='Книги в библиотеке: ')
lbl3.grid(row=2,column=2)
lbl4=Label(root, text='Найти книгy: ')
lbl4.grid(row=6,column=0)
lbl5=Label(root, text='das')
lbl5.place(x=105,y=240)

def vhod(event):
    listbox1.delete(0, END)
    listbox2.delete(0, END)
    list1=open(nimi.get()+'.txt')
    list2=open('raamatud.txt')
    for i in list1:
        listbox1.insert(END,i)
    for k in list2:
        listbox2.insert(END,k)
    list1.close()
    list2.close()

def dobavitu(event):
    if len(listbox2.curselection() and nimi.get()) !=0:
        x=listbox2.get(listbox2.curselection())
        listbox1.insert(END, x)
        listbox2.delete(ANCHOR)
        slist=list(listbox1.get(0,END))
        slist=[a.rstrip()+'\n' for a in slist]
        list1=open(nimi.get()+'.txt', 'w')
        list1.writelines(slist)
        list1.close()
        slist=list(listbox2.get(0,END))
        slist=[a.rstrip()+'\n' for a in slist]
        list2=open('raamatud.txt', 'w')
        list2.writelines(slist)
        list2.close()

def dobavitd(event):
    if len(listbox1.curselection() and nimi.get()) !=0:
        x=listbox1.get(listbox1.curselection())
        listbox2.insert(END, x)
        listbox1.delete(ANCHOR)
        slist=list(listbox1.get(0,END))
        slist=[a.rstrip()+'\n' for a in slist]
        list1=open(nimi.get()+'.txt', 'w')
        list1.writelines(slist)
        list1.close()
        slist=list(listbox2.get(0,END))
        slist=[a.rstrip()+'\n' for a in slist]
        list2=open('raamatud.txt', 'w')
        list2.writelines(slist)
        list2.close()

def naiti(event):
    f=open('raamatud.txt')
    a=1
    for i in f:
        if i==kniga.get()+'\n':
            lbl5['text']='Книга '+i+' в библиотеке!'
            break
        else:
            lbl5['text']='Книги нет\nв библиотеке!'

button1=Button(root, text='Вход')
button1.grid(row=1,column=2)
button1.bind('<Button-1>', vhod)
button2=Button(root, text='Взять\nкнигу')
button2.place(x=110,y=90)
button2.bind('<Button-1>', dobavitu)
button3=Button(root, text='Вернуть\nкнигу')
button3.place(x=105,y=140)
button3.bind('<Button-1>', dobavitd)
button4=Button(root, text='Найти книгy')
button4.grid(row=6,column=2)
button4.bind('<Button-1>', naiti)
root.mainloop()
