from tkinter import *
# Tạo cửa sổ
top = Tk()
top.title('Giải Bất Phương Trình')
top.geometry("800x400")
top.attributes('-topmost',True ) #Lệnh luôn hiển thị trên mọi cửa sổ
top['bg']= '#ffb6c1'
# Tạo label
name = Label(top, text = 'Giải Bất Phương Trình Bậc 2', font=('Time New Romans',20), fg='black',bg='#ffb6c1')
name.place(x = 220, y = 20)
# label của a
a = Label(top, text = 'Nhập hệ số a :', font=('Time New Romans',10),bg='#ffb6c1')
a.place(x = 10, y = 80)
# label của b
b = Label(top, text = 'Nhập hệ số b :', font=('Time New Romans',10),bg='#ffb6c1')
b.place(x = 10, y = 130)
# label của c
c = Label(top, text = 'Nhập hệ số c :', font=('Time New Romans',10),bg='#ffb6c1')
c.place(x = 10, y = 180)
# Tạo entry
# entry của a
entry = Entry(top, width ='20', font=('Time New Roman',10),fg='black',bg='#ffb6c1')
entry.place(x = 100, y = 80)
# entry của b
entry = Entry(top, width ='20', font=('Time New Roman',10),fg='black',bg='#ffb6c1')
entry.place(x = 100, y = 130)
# entry của c
entry = Entry(top, width ='20', font=('Time New Roman',10),fg='black',bg='#ffb6c1')
entry.place(x = 100, y = 180)
# button xac nhan
but = Button(top, text='Giải phương trình',bg='#ffb6c1')
but.place(x= 120, y= 210, width='120', height='20' )

top.mainloop()
