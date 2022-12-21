from tkinter import*
from tkinter import ttk
from time import*
import csv
win=Tk()
win.title('Taxi Calculator')
date_distance_price_list=[]    #เก็บวันที่ ระยะทาง ค่าโดยสาร

tabControl = ttk.Notebook(win) 
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='หน้าแรก') 
tabControl.add(tab2, text ='รายการ') 
tabControl.pack(expand = 1, fill ='both')

image3 = Canvas(tab1, width = 1000, height = 400)
image3.grid(sticky=NW,columnspan=50,rowspan=16,column=0)
my_image3 = PhotoImage(file='C:\\Users\Admin\Desktop\โปรเจค\image\\ภาพพื้นหลัง.png')
image3.create_image(0, 0, anchor = NW, image=my_image3)

image4 = Canvas(tab2, width = 1000, height = 400)
image4.grid(sticky=NW,columnspan=50,rowspan=16,column=0)
my_image4 = PhotoImage(file='C:\\Users\Admin\Desktop\โปรเจค\image\\ภาพพื้นหลัง.png')
image4.create_image(0, 0, anchor = NW, image=my_image4)

#ฟังก์คำนวณ
def calculator_price_taxi(distance,time_late):
  if distance<=1: 
    price_distance=35   #1กม.แรก35บาท
  elif distance<=10:
    price_distance=int(35+5.5*(distance-1))   #1กม.แรก+ราคากม.2-10(ระยะทาง-1)
  elif distance<=20:
    price_distance=int(84.5+6.5*(distance-10))
  elif distance<=40:
    price_distance=int(149.5+7.5*(distance-20))
  elif distance<=60:
    price_distance=int(299.5+8*(distance-40))
  elif distance<=80:
    price_distance=int(459.5+9*(distance-60))
  elif distance>80:
    price_distance=int(639.5+10.5*(distance-80))

  if price_distance%2==0:  #ตรวจคู่คี่ 
    price_distance+=1   #ถ้าคู่ให้+1

  price_taxi=price_distance+int(time_late)*2  #ราคาจากระยะทาง+ราคาจากระยะเวลาที่รถติด*2 (*2เพราะ1นาทีช2บาท)
  return price_taxi

#ปุ่มคำนวณ
def button_cal(*args):
  time_cal=strftime('%H:%M')
  date_month_year_namefile=strftime('%d'+'_'+'%b'+'_'+'%Y')
  filepath=('income{}.csv'.format(date_month_year_namefile))
  try:
    time_late=int(et_time.get())  #ถ้าช่องระยะเวลาที่รถติดไม่มีจะerror
  except Exception:
    time_late=0  #errorแล้วให้ค่า=0
  try:
    distance=int(et_distance.get()) 
    price_taxi=calculator_price_taxi(distance,time_late)  #เรียกใช้functionแล้วคืนค่ากลับมา
    lb_price.config(text='ราคา {} บาท'.format(price_taxi))
    date_distance_price_list=('{},{},{}'.format(time_cal,distance,price_taxi)).split(',')#แบ่งด้วยเครื่องหมาย,
    with open(filepath,'a',encoding='utf-8')as file:  #a=update 
      writer=csv.writer(file,lineterminator='\n')
      writer.writerow(date_distance_price_list)
  except Exception:
    lb_price.config(text='ใส่ระยะทาง')  

#ปุ่มค้นหา
def search():
  try:
    total_price=0
    total_distance=0
    time_show=''
    distance_show=''
    price_show=''
    filepath=('income{}_{}_{}.csv'.format(et_date.get(),et_month.get(),et_year.get()))
    with open(filepath,'r',encoding='utf-8')as file:
      read_file=csv.reader(file)
      read_file_list=list(read_file)
    for i in read_file_list:
      time_show+=str(i[0])+' น.'+'\n'
      distance_show+=str(i[1])+' Km'+'\n'
      price_show+=str(i[2])+' BTH'+'\n'
      total_price+=eval(i[2])
      total_distance+=eval(i[1])
      
    win2 = Toplevel(win)  #เรียกหน้าต่างwin2 ขึ้นมา
    image5 = Canvas(win2, width = 500, height = 450)
    image5.grid(sticky=NW,columnspan=50,rowspan=16,column=0)
    my_image5 = PhotoImage(file='C:\\Users\Admin\Desktop\โปรเจค\image\\ภาพพื้นหลัง.png')
    image5.create_image(0, 0, anchor = NW, image=my_image4)
    lb_time_show = Label(win2,text=' ',font='Helvetica 15 bold italic', fg='black',bg='white')
    lb_time_show.grid(row=3,column=1,padx=20)
    lb_distance_show = Label(win2,text=' ',font='Helvetica 15 bold italic',bg='white')
    lb_distance_show.grid(row=3,column=3,padx=10)
    lb_price_show = Label(win2,text=' ',font='Helvetica 15 bold italic',bg='white')
    lb_price_show.grid(row=3,column=5)
    lb_total_price_distance = Label(win2,text=' ',font='Helvetica 15 bold italic', fg='red',bg='white')
    lb_total_price_distance.grid(row=4,column=1,sticky=E,columnspan=8)
    bt_close3 = Button(win2,text='ออก',font='Helvetica 15 bold',width=9,bg='#c1e7e3',command=win2.destroy)
    bt_close3.grid(row=6,column=1,columnspan=8,pady=20)

    lb_time_show.config(text=time_show)
    lb_distance_show.config(text=distance_show,fg='black')
    lb_price_show.config(text=price_show)
    lb_total_price_distance.config(text='ระยะทางรวม: {} Km เป็นเงิน: {} BTH '.format(total_distance,total_price),bg='white')
    lb_toppic_time = Label(win2,text='เวลา',font='Helvetica 15 bold italic',bg='white')
    lb_toppic_time.grid(row=2,column=1)
    lb_toppic_distance = Label(win2,text='ระยะทาง',font='Helvetica 15 bold italic',bg='white')
    lb_toppic_distance.grid(row=2,column=3)
    lb_toppic_price = Label(win2,text='ราคา',font='Helvetica 15 bold italic',bg='white')
    lb_toppic_price.grid(row=2,column=5)
  except Exception:
    win_notfound = Toplevel(win)
    win_notfound.minsize(150,100)
    win_notfound.config(bg='white')
    Label(win_notfound,text='ไม่พบข้อมูล',font='Helvetica 15 bold italic',bg='white').grid(row=0,padx=5,pady=10)
    Button(win_notfound,text='ตกลง',font='Helvetica 15 bold',command=win_notfound.destroy,bg='#c1e7e3').grid(row=1,padx=5,pady=10)
    
##หน้าต่างหน้าแรก##
lb_topic_index = Label(tab1,text='โปรแกรมคำนวณค่า Taxi',font='Helvetica 30 bold italic',bg='white')
lb_topic_index.grid(sticky=W,padx=5,pady=10,row=0,columnspan=16)

date_month_year=strftime('%d'+' / '+'%b'+' / '+'%Y ')
lb_date_month_year = Label(tab1,text='วันที่ / เดือน / ปี',font='Helvetica 10 bold italic', fg='red',bg='white')
lb_date_month_year.grid(sticky=E,row=1,column=2)
lb_date_month_year2 = Label(tab1,text=date_month_year,font='Helvetica 10 bold italic', fg='red',bg='white')
lb_date_month_year2.grid(sticky=E,row=2,column=2)  

lb_topic_distance = Label(tab1,text='ระยะทาง',font='Helvetica 15 bold italic',bg='white')
lb_topic_distance.grid(sticky=E,pady=5,row=3,column=0)
lb_kg = Label(tab1,text='กิโลเมตร',font='Helvetica 15 bold italic',bg='white')
lb_kg.grid(sticky=W,row=3,column=2)
et_distance = Entry(tab1,font='Helvetica 15 bold',width=9)#ช่องใช่ระยะทาง
et_distance.grid(row=3,column=1)
et_distance.focus()

lb_topic_time = Label(tab1, text='ระยะเวลาที่รถติด', font='Helvetica 15 bold',bg='white')
lb_topic_time.grid(sticky=E,row=4,column=0)
lb_minute = Label(tab1, text='นาที', font='Helvetica 15 bold',bg='white')
lb_minute.grid(sticky=W,row=4,column=2)
et_time = Entry(tab1, font='Helvetica 15 bold', width=9)#ช่องใส่เวลาที่รถติด
et_time.grid(row=4,column=1)

lb_price = Label(tab1, text='0 บาท', font='Helvetica 20 bold', fg='red',bg='white')#แสดงราคา
lb_price.grid(sticky=E,row=5,pady=30,column=1,columnspan=3)

bt_cal = Button(tab1,text='คำนวณ',font='Helvetica 15 bold',command=button_cal,width=9,bg='#c1e7e3')
bt_cal.grid(sticky=E,row=6,column=0)
bt_close1 = Button(tab1,text='ออก',font='Helvetica 15 bold',command=win.destroy,bg='#c1e7e3')#ปุ่มต่างๆ
bt_close1.grid(row=6,column=2)

image = Canvas(tab1, width = 540, height = 375)
my_image = PhotoImage(file='C:\\Users\Admin\Desktop\โปรเจค\image\\รูปราคาแท็กซี่.jpg')
image.create_image(0, 0, anchor = NW, image=my_image)
image.grid(sticky=W,row=0,rowspan=8,column=30)

##หน้าต่างแสดงวันอื่นๆ##
lb_topic_other_day = Label(tab2,text='แสดงรายวัน',font='Helvetica 60 bold italic',bg='white')
lb_topic_other_day.grid(columnspan=5,column=8,row=0)
et_date = ttk.Combobox(tab2, font='Helvetica 20 bold',value=[x for x in range(1,32)],width=3)
et_date.grid(row=1,column=8,sticky=E,pady=50,padx=20)
et_date.current(0)
lb_1 = Label(tab2,text='/',font='Helvetica 60 bold',bg='white')
lb_1.grid(row=1,column=9,sticky=W,pady=50)
et_month = ttk.Combobox(tab2, font='Helvetica 20 bold',value=('Jan','Feb','Mar','Apr','May',
                                                              'Jun','Jul','Aug','Sep','Oct',
                                                              'Nov','Dec'),width=4)
et_month.grid(row=1,column=9,padx=40)
et_month.current(0)
lb_2 = Label(tab2,text='/',font='Helvetica 60 bold',bg='white')
lb_2.grid(row=1,column=9,sticky=E,pady=50)
et_year =ttk.Combobox(tab2, font='Helvetica 20 bold',value=[x for x in range(2020,3001)],width=4)
et_year.grid(row=1,column=10,sticky=W,pady=50,padx=20)
et_year.current(0)

bt_search = Button(tab2,text='ค้นหา',font='Helvetica 15 bold',command=search,width=9,bg='#c1e7e3')
bt_search.grid(row=5,column=7,columnspan=2,padx=32,pady=30) 
bt_close2 = Button(tab2,text='ออก',font='Helvetica 15 bold',command=win.destroy,width=9,bg='#c1e7e3')
bt_close2.grid(row=5,column=9,columnspan=2,padx=10,pady=25)

image2 = Canvas(tab2, width = 540, height = 375)
my_image2 = PhotoImage(file='C:\\Users\Admin\Desktop\โปรเจค\image\\รูปราคาแท็กซี่.jpg')
image2.create_image(0, 0, anchor = NW, image=my_image2)
image2.grid(sticky=NW,row=0,rowspan=8,column=20)

def focus_et_distance(*args):
  et_distance.focus()
def focus_et_time(*args):
  et_time.focus()
win.bind('<Return>',button_cal)
win.bind('<Key-Up>',focus_et_distance)
win.bind('<Key-Down>',focus_et_time)

win.mainloop()
















