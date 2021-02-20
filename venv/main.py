from tkinter import *
from datetime import datetime

with open("tim's diner menu.txt") as f:
    a=f.read()
    print(a)

window = Tk()
window.geometry("1500x700")
window.title("Tim's Diner")


canvas = Canvas(window, width = 2000, height = 2000, bg = 'black')
canvas.pack()
burger_img = PhotoImage(file = "burger10.gif")
canvas.create_image(650, 100,anchor='center', image = burger_img)


label6 = Label(window, text='Tim\'s Diner',font='times 30 bold', bg = 'black', fg='gold').place(x=650,y=28,anchor='center')
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")
print(dt_string)
time_label = Label(window, text=dt_string,font='times 20', bg = 'black', fg = 'white').place(x=560,y=300)

#Table

label20 = Label(window, text='Enter your table number:',font='times 20 bold', bg = 'black', fg = 'gold').place(x=510,y=180)
a= IntVar()
e20 = Entry(window, textvariable=a)
e20.place(x=600,y=220)

#menucard
label1=Label(window,text='MENU',font='times 28 bold', bg = 'black', fg = 'gold').place(x=1015,y=70)

#Breakfast
label1=Label(window,text='------BREAKFAST------',font='times 18 bold', bg = 'black', fg = 'orange').place(x=950,y=120)

label1=Label(window,text='All Day (large)        $5.50',font='times 18', bg = 'black', fg = 'white').place(x=950,y=150)

label1=Label(window,text='AllDay(small)         $3.30',font='times 18', bg = 'black', fg = 'white').place(x=950,y=180)

#Mains
label1=Label(window,text='-----------MAINS-----------',font='times 18 bold',bg = 'black', fg = 'orange').place(x=950,y=210)

label1=Label(window,text='HotDog                   $3.50',font='times 18', bg = 'black', fg = 'white').place(x=950,y=240)

label1=Label(window,text='Burger                     $4.00',font='times 18', bg = 'black', fg = 'white').place(x=950,y=270)

label1=Label(window,text='Cheese Burger        $4.20',font='times 18', bg = 'black', fg = 'white').place(x=950,y=300)

label1=Label(window,text='Chicken Goujons    $3.50',font='times 18', bg = 'black', fg = 'white').place(x=950,y=330)

#Extras
label1=Label(window,text='----------EXTRAS----------',font='times 18 bold', bg = 'black', fg = 'orange').place(x=950,y=360)

label1=Label(window,text='Fries                        $1.75',font='times 18', bg = 'black', fg = 'white').place(x=950,y=390)

label1=Label(window,text='Salad                       $2.20',font='times 18', bg = 'black', fg = 'white').place(x=950,y=420)

#Drinks
label1=Label(window,text='----------DRINKS----------',font='times 18 bold', bg = 'black', fg = 'orange').place(x=950,y=450)

label1=Label(window,text='Milkshake               $2.20',font='times 18', bg = 'black', fg = 'white').place(x=950,y=480)

label1=Label(window,text='Soft Drinks              $1.30',font='times 18', bg = 'black', fg = 'white').place(x=950,y=510)

label1=Label(window,text='Still Water               $0.90',font='times 18', bg = 'black', fg = 'white').place(x=950,y=540)

label1=Label(window,text='Sparkling Water      $0.90',font='times 18', bg = 'black', fg = 'white').place(x=950,y=570)

#Billing section
label7 = Label(window, text='Select the items',font='times 20 bold', bg = 'black', fg = 'gold').place(x=100,y=70)

label8 = Label(window, text='All Day(large)',font='times 18', bg = 'black', fg = 'orange').place(x=20,y=120)
a = IntVar()
e1 = Entry(window, textvariable=a)
e1.place(x=20,y=150)

label9 = Label(window, text='All Day(small)',font='times 18', bg = 'black', fg = 'orange').place(x=250,y=120)
a= IntVar()
e2 = Entry(window, textvariable = a)
e2.place(x=250,y=150)

label13 = Label(window, text='Hot Dog',font='times 18', bg = 'black', fg = 'orange').place(x=20,y=180)
a= IntVar()
e3 = Entry(window, textvariable = a)
e3.place(x=20,y=210)

label14 = Label(window, text='Burger',font='times 18', bg = 'black', fg = 'orange').place(x=250,y=180)
a= IntVar()
e4 = Entry(window, textvariable = a)
e4.place(x=250,y=210)

label15 = Label(window, text='Cheese Burger',font='times 18', bg = 'black', fg = 'orange').place(x=20,y=240)
a= IntVar()
e5 = Entry(window, textvariable = a)
e5.place(x=20,y=280)

label16 = Label(window, text='Chicken Goujons',font='times 18', bg = 'black', fg = 'orange').place(x=250,y=240)
a= IntVar()
e6 = Entry(window, textvariable = a)
e6.place(x=250,y=280)

label21 = Label(window, text='Fries',font='times 18', bg = 'black', fg = 'orange').place(x=20,y=310)
a= IntVar()
e8 = Entry(window, textvariable = a)
e8.place(x=20,y=340)

label22 = Label(window, text='Salad',font='times 18', bg = 'black', fg = 'orange').place(x=250,y=310)
a= IntVar()
e9 = Entry(window, textvariable = a)
e9.place(x=250,y=340)

label23 = Label(window, text='Milkshake',font='times 18', bg = 'black', fg = 'orange').place(x=20,y=380)
a= IntVar()
e10 = Entry(window, textvariable = a)
e10.place(x=20,y=420)

label24 = Label(window, text='Soft Drinks',font='times 18', bg = 'black', fg = 'orange').place(x=250,y=380)
a= IntVar()
e11 = Entry(window, textvariable = a)
e11.place(x=250,y=420)

label24 = Label(window, text='Still Water',font='times 18', bg = 'black', fg = 'orange').place(x=20,y=450)
a= IntVar()
e12 = Entry(window, textvariable = a)
e12.place(x=20,y=480)

label25 = Label(window, text='Sparkling Water',font='times 18', bg = 'black', fg = 'orange').place(x=250,y=450)
a= IntVar()
e13 = Entry(window, textvariable = a)
e13.place(x=250,y=480)






def calculate():
    all_day_large = e1.get()
    all_day_small = e2.get()
    hot_dog = e3.get()
    burger = e4.get()
    cheese_burger = e5.get()
    chicken_goujons = e6.get()
    fries = e8.get()
    salad = e9.get()
    milkshake = e10.get()
    soft_drinks = e11.get()
    still_water = e12.get()
    sparkling_water = e13.get()
    total = ((int(all_day_large)*5.50)+(int(all_day_small)*3.50)+(int(hot_dog)*3)+(int(burger)*4)+(int(cheese_burger)*4.25)+(int(chicken_goujons)*3.50)+(int(fries)*1.75)+(int(salad)*2.20)+(int(milkshake)*2.20))+(int(soft_drinks)*1.30+(int(still_water)*0.90)+(int(sparkling_water)*0.90))
    label12 = Label(window, text= 'Total: ' + '$' + str(round (total,3)), font='times 18', bg = 'black', fg = 'orange').place(x=550, y=500)
    table = e20.get()
    table_label = Label(window, text='Table no. ' + str(table), font = 'times 18', bg = 'black', fg = 'orange').place(x=550, y=530)

#Receipt
item_list=[]
qty_list=[]
amt_list=[]

def second_win():
    all_day_large = e1.get()
    all_day_small = e2.get()
    hot_dog = e3.get()
    burger = e4.get()
    cheese_burger = e5.get()
    chicken_goujons = e6.get()
    fries = e8.get()
    salad = e9.get()
    milkshake = e10.get()
    soft_drinks = e11.get()
    still_water = e12.get()
    sparkling_water = e13.get()
    menu = [['All Day(Large)',all_day_large, 5.50],['All Day(Small)',all_day_small,3.50],['Hot Dog',hot_dog,3.00],['Burger',burger,4.00],['Cheese Burger',cheese_burger,4.25],['Chicken Goujons',chicken_goujons,3.50],['Fries',fries,1.75],['Salad',salad,2.20],['Milkshake',milkshake,2.20],['Soft Drinks',soft_drinks,1.30],['Still Water',still_water,0.90],['Sparkling Water',sparkling_water,0.90]]
    root=Tk()
    root.title('Receipt')
    root.geometry('500x500')
    item = Label(root, text = 'Item', font = 'times 15 bold', width = 10).place(x=30,y=0)
    quantity = Label(root, text = 'Quantity', font = 'times 15 bold', width = 10).place(x=195,y=0)
    amount = Label(root, text = 'Amount', font = 'times 15 bold', width = 10).place(x=350,y=0)
    for i in menu:
        if int(i[1]) >0:
            item_list.append(i[0])
            qty_list.append(i[1])
            x = round(int(i[1]) * i[2], 3)
            amt_list.append(str(x))
    line = Label(root, text='-'*110, width=75).place(x=0, y=385)
    total = ((int(all_day_large) * 5.50) + (int(all_day_small) * 3.50) + (int(hot_dog) * 3) + (int(burger) * 4) + (int(cheese_burger) * 4.25) + (int(chicken_goujons) * 3.50) + (int(fries) * 1.75) + (int(salad) * 2.20) + (int(milkshake) * 2.20)) + (int(soft_drinks) * 1.30 + (int(still_water) * 0.90) + (int(sparkling_water) * 0.90))
    ttl_lbl = Label(root, text='Total: ', font='times 15 bold', width=10).place(x=30, y=400)
    ttl_num = Label(root, text='$' + str(round (total,3)), font='times 15', width=15).place(x=320, y=400)
    return_but = Button(root, text='Return', width = 20, command = root.destroy).place(x=10,y=450)
    item_lbl = Label(root, text='\n'.join(item_list), font='times 15', width=15).place(x=10, y=30)
    qty_lbl =ttl_lbl = Label(root, text= '\n'.join(qty_list), font='times 15', width=10).place(x=200, y=30)
    amt_lbl = Label(root, text= '\n'.join(amt_list), font='times 15', width=10).place(x=355, y=30)

#buttons
bill_button = Button(window,text='Bill', font = 'times 15', width=20,command=calculate, bg = 'black', fg = 'gold').place(x=550,y=450)

button_quit = Button(window, text = 'Exit', font = 'times 15', width = 20, command = window.quit, bg = 'black', fg = 'gold').place(x=550,y=400)

rec_button = Button(window,text='Receipt', font = 'times 15', width=20,command=second_win, bg = 'black', fg ='gold').place(x=550,y=350)
mainloop()



window.mainloop()

