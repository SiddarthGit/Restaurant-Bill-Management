from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()


class LoginPage():
    def __init__(self, win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurant Management System")
        self.title_label=Label(self.win,text="Restaurant Management System",font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        self.main_frame=Frame(self.win,bg="lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=400)

        self.login_tbl=Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="lightgrey",font=('sans-serif',25,'bold'))
        self.login_tbl.pack(side=TOP,fill=X)


        self.entry_frame=LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="lightgrey",font=('sans-serif',18))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)



        self.entus_lbl=Label(self.entry_frame,text="Enter Username: ",bg="lightgrey",font=("sans-serif",15))
        self.entus_lbl.grid(row=0,column=0)


        #------------------ Variables---------

        username=StringVar()
        password=StringVar()

        #-----------------------------------------


        self.entus_ent=Entry(self.entry_frame,font=("sans-serif",15),relief=SUNKEN,bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)

        self.ent_pwdlbl=Label(self.entry_frame,text=("Enter Password: "),bg="lightgrey",font=("sans-serif",15))
        self.ent_pwdlbl.grid(row=2,column=0)

        self.entpwd_ent=Entry(self.entry_frame,font=("sans-serif",15),relief=SUNKEN,bd=6,textvariable=password,show="*")
        self.entpwd_ent.grid(row=2,column=1,padx=4,pady=4)

        #------------------functions-------------------
        def check_login():
            if username.get()==""and password.get()=="":
                self.billing_btn.config(state="normal")
            else:
                pass #------>message box 

        def reset():
            username.set("")
            password.set("")

        def billing_sect():
            self.newWindow=Toplevel(self.win)
            self.app=Window2(self.newWindow)



        #=-----------------------------------------------

        #------------------------------------------
   

        #-------------BUTTONS-----------
        self.button_frame=LabelFrame(self.entry_frame,text="Options",font=("Ariel",15),bd=7,bg="lightgrey",relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=90)


        self.login_btn=Button(self.button_frame,text="Login",font=('Ariel',15),bd=5,width=15,command=check_login )
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)

        self.billing_btn=Button(self.button_frame,text="Billing",font=('Ariel',15),bd=5,width=15,command=billing_sect )
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn=Button(self.button_frame,text="Reset",font=('Ariel',15),bd=5,width=15,command=reset )
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)


class Window2():
    def __init__(self,win):
        self.win=win
        self.win.geometry("1320x750+0+0")
        self.win.title("Restaurant Management System")

        self.title_label=Label(self.win,text="Restaurant Management System",font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        #-------------------------entry frame details

        #------------variables--------
        bill_no=random.randint(100,9999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)

        calc_var = StringVar()

        cust_nm = StringVar()
        cust_cot = StringVar()

        date_pr = StringVar()
        item_pur=StringVar()
        item_qty=StringVar()
        cone=StringVar()
        date_pr.set(datetime.now())

        total_list=[]
        self.grd_total=0



        self.entry_frame= LabelFrame(self.win,text="enter details",background="lightgrey",font=('Ariel',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)

        self.bill_no_lbl = Label(self.entry_frame,text="Bill Number",font=('Ariel',15),bg="lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)


        self.bill_no_ent = Entry(self.entry_frame,bd=5,textvariable=bill_no_tk,font=('Ariel',15))
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")

        self.cust_nm_lbl = Label(self.entry_frame,text="Customer Name ",font=('Ariel',15),bg="lightgrey")
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)


        self.cust_nm_ent = Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=('Ariel',15))
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)

        self.cust_ct_lbl = Label(self.entry_frame,text="Contact Number",font=('Ariel',15),bg="lightgrey")
        self.cust_ct_lbl.grid(row=2,column=0,padx=2,pady=2)


        self.cust_ct_ent = Entry(self.entry_frame,bd=5,textvariable=cust_cot,font=('Ariel',15))
        self.cust_ct_ent.grid(row=2,column=1,padx=2,pady=2)

        self.Date_lbl = Label(self.entry_frame,text="Date",font=('Ariel',15),bg="lightgrey")
        self.Date_lbl.grid(row=3,column=0,padx=2,pady=2)


        self.Date_ent = Entry(self.entry_frame,bd=5,textvariable=date_pr,font=('Ariel',15))
        self.Date_ent.grid(row=3,column=1,padx=2,pady=2)
        

        # self.date_lbl = Label(self.entry_frame,text="Billing Date ",font=('Ariel',15),bg="lightgrey")
        # self.date_lbl.grid(row=4,column=0,padx=2,pady=2)


        # self.date_ent = Entry(self.entry_frame,bd=5,textvariable=None,font=('Ariel',15))
        # self.date_ent.grid(row=4,column=1,padx=2,pady=2)

        self.item_pur_lbl = Label(self.entry_frame,text="Item Purchased",font=('Ariel',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=5,column=0,padx=2,pady=2)


        self.item_pur_ent = Entry(self.entry_frame,bd=5,textvariable=item_pur,font=('Ariel',15))
        self.item_pur_ent.grid(row=5,column=1,padx=2,pady=2)

        self.item_qty_lbl = Label(self.entry_frame,text="Item Quantity:  ",font=('Ariel',15),bg="lightgrey")
        self.item_qty_lbl.grid(row=6,column=0,padx=2,pady=2)


        self.item_qty_ent = Entry(self.entry_frame,bd=5,textvariable=item_qty,font=('Ariel',15))
        self.item_qty_ent.grid(row=6,column=1,padx=2,pady=2)

        self.cost_one_lbl = Label(self.entry_frame,text="Cost of One: ",font=('Ariel',15),bg="lightgrey")
        self.cost_one_lbl.grid(row=7,column=0,padx=2,pady=2)


        self.cost_one_ent = Entry(self.entry_frame,bd=5,textvariable=cone,font=('Ariel',15))
        self.cost_one_ent.grid(row=7,column=1,padx=2,pady=2)


             #functions
        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\tHeaven In Spice")
            self.bill_txt.insert(END,"\n\t\t\t 6th Avenue Guduvanchery Street")
            self.bill_txt.insert(END,"\n\t\t\t     Contact- +919456387601")
            self.bill_txt.insert(END,"\n=================================================================================")
            self.bill_txt.insert(END,f"Bill Number: {bill_no_tk.get()}")

        def genbill():
            self.bill_txt.insert(END,f"\nCustomer Name: {cust_nm.get()}")
            self.bill_txt.insert(END,f"\nCustomer Contact: {cust_cot.get()}")
            self.bill_txt.insert(END,f"\nDate : {date_pr.get()}")
            self.bill_txt.insert(END,"\n=================================================================================")
            self.bill_txt.insert(END,"Product Name\t\t       Quantity       \t\tPer Cost\t\t       Total")
            self.bill_txt.insert(END,"\n=================================================================================")
            self.add_btn.config(state="normal")
            self.total_btn.config(state="normal")
            self.save_btn.config(state="normal")


        # def total_func():

        #     for item in total_list:
        #         self.grd_total=self.grd_total+item
        #         self.bill_txt.insert(END,"\n=================================================================================")
        #         self.bill_txt.insert(END,f"\t\t\t\t\t\tGrand Total : {self.grd_total}")
        #         self.bill_txt.insert(END,"\n=================================================================================")

        def add_func():
             qty = int(item_qty.get())
             cones=int(cone.get())
             total=qty*cones
             total_list.append(total)
             self.bill_txt.insert(END,f"\n{item_pur.get()}\t\t       {item_qty.get()}              \t\t{cone.get()}\t\t         Rs. {total}")

        def clear_func():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("")

        def total_func():
            if not hasattr(self, 'grd_total_printed') or not self.grd_total_printed:
                for item in total_list:
                    self.grd_total += item
                    self.bill_txt.insert(END, "\n=================================================================================")
                    self.bill_txt.insert(END, f"\t\t\t\t Grand Total :{self.grd_total}")
                    self.bill_txt.insert(END, "\n=================================================================================")
                    self.grd_total_printed = True

       
        

        def reset_func():
            self.bill_txt.delete("1.0",END)
            default_bill()  

            


        def add_pur():
            pass



       # billing button frame 
        self.option_frame= LabelFrame(self.win,text="Options",background="lightgrey",font=('Ariel',12),bd=5,relief=GROOVE)
        self.option_frame.place(x=50,y=450,width=400,height=250)

        self.add_btn=Button(self.option_frame,text="ADD",font=('Ariel',12),bd=5,width=12,height=3,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)

        self.generate_btn=Button(self.option_frame,text="GENERATE",font=('Ariel',12),bd=5,width=12 ,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)

        self.clear_btn=Button(self.option_frame,text="Clear",font=('Ariel',12),bd=5,width=12,height=3,command=clear_func)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)

        self.total_btn=Button(self.option_frame,text="TOTAL",font=('Ariel',12),bd=5,width=12 ,height=3,command=total_func)
        self.total_btn.grid(row=1,column=0,padx=4,pady=4)

        self.reset_btn=Button(self.option_frame,text="RESET",font=('Ariel',12),bd=5,width=12 ,height=3,command=reset_func)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)

        self.save_btn=Button(self.option_frame,text="SAVE",font=('Ariel',12),bd=5,width=12,height=3)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2)

        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")

        #-----------------------------------
  
            


        #------------calculator frame------2

        self.calc_frame=Frame(self.win,bd=8,background="lightgrey",relief=GROOVE)
        self.calc_frame.place(x=600,y=95,width=690,height=325)

        self.num_ent=Entry(self.calc_frame,bd=15,background="lightgrey",textvariable=calc_var,font=('Ariel',15),width=58,justify='right')
        self.num_ent.grid(row=0,column=0,columnspan=11)

        def press_btn(event):
            text= event.widget.cget("text")
            if text=="=":
                if calc_var.get().isdigit():
                    value = int(calc_var.get())
                else:
                    try:
                        value=eval(self.num_ent.get())
                    except:
                        printf("Error")
                calc_var.set(value)
                self.num_ent.update()
            elif text == "c":   
                pass
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()
                 
            

        self.btn7=Button(self.calc_frame,bg="lightgrey",text="7",bd=12,width=12,height=1,font=('Ariel',15))
        self.btn7.grid(row=1,column=0,padx=2,pady=2)
        self.btn7.bind("<Button-1>",press_btn)

        self.btn8=Button(self.calc_frame,bg="lightgrey",text="8",bd=12,width=12,height=1,font=('Ariel',15))
        self.btn8.grid(row=1,column=1,padx=2,pady=2)
        self.btn8.bind("<Button-1>",press_btn)

        self.btn9=Button(self.calc_frame,bg="lightgrey",text="9",bd=12,width=12,height=1,font=('Ariel',15))
        self.btn9.grid(row=1,column=2,padx=2,pady=2)
        self.btn9.bind("<Button-1>",press_btn)

        self.btnadd=Button(self.calc_frame,bg="lightgrey",text="+",bd=12,width=12,height=1,font=('Ariel',15))
        self.btnadd.grid(row=1,column=3,padx=2,pady=2)
        self.btnadd.bind("<Button-1>",press_btn)

        self.btn4=Button(self.calc_frame,bg="lightgrey",text="4",bd=12,width=12,height=1,font=('Ariel',15))
        self.btn4.grid(row=2,column=0,padx=2,pady=2)
        self.btn4.bind("<Button-1>",press_btn)

        self.btn5=Button(self.calc_frame,bg="lightgrey",text="5",bd=12,width=12,height=1,font=('Ariel',15))
        self.btn5.grid(row=2,column=1,padx=2,pady=2)
        self.btn5.bind("<Button-1>",press_btn)

        self.btn6=Button(self.calc_frame,bg="lightgrey",text="6",bd=12,width=12,height=1,font=('Ariel',15))
        self.btn6.grid(row=2,column=2,padx=2,pady=2)
        self.btn6.bind("<Button-1>",press_btn)

        self.btnsub=Button(self.calc_frame,bg="lightgrey",text="-",bd=12,width=12,height=1,font=('Ariel',15))
        self.btnsub.grid(row=2,column=3,padx=2,pady=2)
        self.btnsub.bind("<Button-1>",press_btn)

        self.btn1=Button(self.calc_frame,bg="lightgrey",text="1",bd=12,width=12,height=1,font=('Ariel',15))
        self.btn1.grid(row=3,column=0,padx=2,pady=2)
        self.btn1.bind("<Button-1>",press_btn)

        self.btn2=Button(self.calc_frame,bg="lightgrey",text="2",bd=12,width=12,height=1,font=('Ariel',15))
        self.btn2.grid(row=3,column=1,padx=2,pady=2)
        self.btn2.bind("<Button-1>",press_btn)

        self.btn3=Button(self.calc_frame,bg="lightgrey",text="3",bd=12,width=12,height=1,font=('Ariel',15))
        self.btn3.grid(row=3,column=2,padx=2,pady=2)
        self.btn3.bind("<Button-1>",press_btn)

        self.btnmult=Button(self.calc_frame,bg="lightgrey",text="*",bd=12,width=12,height=1,font=('Ariel',15))
        self.btnmult.grid(row=3,column=3,padx=2,pady=2)
        self.btnmult.bind("<Button-1>",press_btn)

        self.btn0=Button(self.calc_frame,bg="lightgrey",text="0",bd=12,width=12,height=1,font=('Ariel',15))
        self.btn0.grid(row=4,column=0,padx=2,pady=2)
        self.btn0.bind("<Button-1>",press_btn)

        self.btnpoint=Button(self.calc_frame,bg="lightgrey",text=".",bd=12,width=12,height=1,font=('Ariel',15))
        self.btnpoint.grid(row=4,column=1,padx=2,pady=2)
        self.btnpoint.bind("<Button-1>",press_btn)

        self.btnclear=Button(self.calc_frame,bg="lightgrey",text="=",bd=12,width=12,height=1,font=('Ariel',15))
        self.btnclear.grid(row=4,column=2,padx=2,pady=2)
        self.btnclear.bind("<Button-1>",press_btn)

        self.btndiv=Button(self.calc_frame,bg="lightgrey",text="/",bd=12,width=12,height=1,font=('Ariel',15))
        self.btndiv.grid(row=4,column=3,padx=2,pady=2)
        self.btndiv.bind("<Button-1>",press_btn)

        #-------------------------------------
        # 
        # bill Frame
        self.bill_frame=LabelFrame(self.win,text="Bill Area",font=('Ariel',18),bd=8,background="lightgrey",relief=GROOVE,)
        self.bill_frame.place(x=600,y=425,width=690,height=320)   

        self.y_scroll=Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt=Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)

        default_bill()

    


        





if __name__ == "__main__":
    main()






























#DOC
# https://www.tutorialspoint.com/python/tk_relief.htm