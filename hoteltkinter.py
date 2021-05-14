import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hashamsql",
    database="rdbms"
    )
print(mydb)

mycursor=mydb.cursor()

#mysql-connector-python
#pillow

#mycursor.execute("create table hotel5 (first_name VARCHAR(20),last_name VARCHAR(20),mobile int unique,email VARCHAR(30) unique,country VARCHAR(25),room_number int(3) unique,ckeck_in_date varchar(20),no_of_rooms int(3),check_out_date varchar(20),location varchar(20),category_room varchar(10) )")

from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.minsize(1000,800)
root.maxsize(1000,800)
root.title("RESTAURANT FORM")
my_image=PhotoImage(file="hotel11.png")
my_label=Label(image=my_image,width="1000",height="800")
my_label.place(x=0,y=0)

a=Label(root,text="WELCOME TO UBIT HOTEL",bg="grey",width="500")
a.pack()


b=Label(root,text="FIRST NAME")
b.place(x=10,y=120)
c=Label(root,text="LAST NAME")
c.place(x=10,y=160)
d=Label(root,text="MOBILE NUMBER")
d.place(x=10,y=200)
e=Label(root,text="EMAIL")
e.place(x=10,y=320)
f=Label(root,text="CHECK IN DATE")
f.place(x=10,y=360)

g=Label(root,text="NUMBER OF ROOM")
g.place(x=10,y=400)
h=Label(root,text="CHECK OUT DATE")
h.place(x=10,y=440)
i=Label(root,text="LOCATION")
i.place(x=10,y=480)

b_entry=Entry(root)
b_entry.place(x=130,y=120)
c_entry=Entry(root)
c_entry.place(x=130,y=160)
d_entry=Entry(root)
d_entry.place(x=130,y=200)
e_entry=Entry(root)
e_entry.place(x=130,y=320)
f_entry=Entry(root)
f_entry.place(x=130,y=360)
g_entry=Entry(root)
g_entry.place(x=130,y=400)
h_entry=Entry(root)
h_entry.place(x=130,y=440)
i_entry=Entry(root)
i_entry.place(x=130,y=480)

k=StringVar(root)
k.set("           SELECT YOUR COUNTRY")
j=OptionMenu(root,k,"Afghanistan","Albania","Algeria","America","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Cambodia","canada","Chile","China","Colombia","Denmark","Egypt","France","Finland","Germany","Holand","Hungary","India","Indonesia","Italy","Ireland","Iceland","Japan","Koreya","Lebia","Mexico","Malaysia","Nepal","New zealand","Norway","Oman","Pakistan","Qatar","Russia","Saudia arabia","Spain","South africa","Taiwan","Turkey","Thailand","UAE","YEMEN","ZIMBABWE")
j.pack()
j.place(x=80,y=240)


l=IntVar(root)
l.set("              SELECT YOUR ROOM")
m=OptionMenu(root,l,1,2,3,4,5,6,7,8,9,10)
m.pack()
m.place(x=80,y=280)

n=StringVar(root)
n.set("              SELECT YOUR CATEGORY")
o=OptionMenu(root,n,"VVIP","VIP","NORMAL","SUITE")
o.pack()
o.place(x=80,y=540)

def save_info():
    try:
        sql = "INSERT INTO hotel5 (first_name, last_name,mobile,email,country,room_number,ckeck_in_date,no_of_rooms,check_out_date,location,category_room) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (b_entry.get(),c_entry.get(),d_entry.get(),e_entry.get(),k.get(),l.get(),f_entry.get(),g_entry.get(),h_entry.get(),i_entry.get(),n.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        p=Label(root,text=e)
        p.place(x=80,y=600)
        p.pack()
   
q=Button(root,text="SUMBIT",width="25",command=save_info)
q.pack()
q.place(x=370,y=600)

root.mainloop()




