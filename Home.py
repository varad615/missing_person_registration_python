from tkinter import *
from tkinter import ttk
import time
import tkinter as tk
from datetime import date
from tkinter import *
from tkinter import ttk
import mysql.connector
from fpdf import FPDF

def main():
    wind = Tk()
    app = Home(wind)
    wind.mainloop()

#========Database Connection===========
mydb = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="", #Enter MYSQL Password 
    database="missing_person" #create a database if not created
)

mycursor = mydb.cursor()

class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("Missing Person Registration | Home")
        self.root.geometry("900x750+0+0")
        

        #=========Date=================

        todaydate = date.today()
        d1 = todaydate.strftime("%d/%m/%y")
        
        #=========Time=================
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        #=========Database Connection========
        def submit():
            today =date.today()
            birthdate = date(int(dobyear.get()), int(dobmonth.get()), int(dobdate.get()))
            ageenter = tk.StringVar()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            ageEntry = Entry(DataFrameLeft,highlightthickness=1,textvariable=ageenter, font=("arial", 10, "bold"), bd=2, width=20,relief='flat')
            ageenter.set(age)
            ageEntry.grid(row=9,column=3)
            mycursor.execute("insert into persons (Name,phnumber,Gender,Date,Time,DOB_Day,DOB_Month,DOB_Year,Age,Last_Reported_Place,Complainants_name,Description,Police_Station_Reported,Missing_Person_Status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(root.name_var.get(),root.ph_var.get(),n.get(),d1,current_time,root.dobday.get(),root.dobmonth.get(),root.dobyear.get(),age,root.lastplace.get(),root.complainname.get(),desription.get("1.0",END),policeincharge.get(),s.get()))
            mycursor.execute("select * from persons;")


            for x in mycursor:
                print(x)

            mydb.commit()

        lbltitle = Label(self.root, text="Missing Person Registration", fg="black",
                font=("ar", 20, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        DataFrameLeft = Frame(self.root, bd=12, padx=20,relief=FLAT)
        DataFrameLeft.place(x=0, y=40, width=900, height=710)


        #========Lable Widget Creation========
        name = Label(DataFrameLeft, text="Name",font="ar 12")
        PhoneNumber = Label(DataFrameLeft, text="Phone Number", font="ar 12")
        Gender = Label(DataFrameLeft, text="Gender", font="ar 12")
        Birthdate = Label(DataFrameLeft, text="Date Of Birth", font="ar 12")
        Lastplace = Label(DataFrameLeft, text="Last Reported Place", font="ar 12")
        Complainants_Name = Label(DataFrameLeft, text="Complainant's Full Name", font="ar 12")
        missing_persons_description = Label(DataFrameLeft, text="Description About Missing Person",font="ar 12")
        police_stn_incharge = Label(DataFrameLeft, text="Police Station Incharge", font="ar 12")
        status = Label(DataFrameLeft, text="Missing Person Status", font="ar 12")
        age = Label(DataFrameLeft, text="Age", font="ar 9")

        #========DOB sub lables==============
        dobdatetxt = Label(DataFrameLeft, text="Day", font="ar 9")
        month = Label(DataFrameLeft, text="Month", font="ar 9")
        dobyeartxt = Label(DataFrameLeft, text="Year", font="ar 9")

        #=======Age Lable====================
        agelable = Label(DataFrameLeft, text="Age", font="ar 9")
        #=========Lable Widget Location=======

        name.grid(row=3, column=1, sticky=W, padx=20)
        PhoneNumber.grid(row=4, column=1, sticky=W, padx=20)
        Gender.grid(row=5, column=1, sticky=W, padx=20)
        Birthdate.grid(row=6, column=1, sticky=W, padx=20)
        dobdatetxt.grid(row=6, column=2, padx=20)
        month.grid(row=7, column=2, padx=20)
        dobyeartxt.grid(row=8, column=2, padx=20)
        age.grid(row=9,column=2,padx=20)
        Lastplace.grid(row=10, column=1,sticky=W, padx=20 )
        Complainants_Name.grid(row=11, column=1,sticky=W,padx=20)
        missing_persons_description.grid(row=12, column=1,sticky=W,padx=20)
        police_stn_incharge.grid(row=13, column=1,sticky=W,padx=20)
        status.grid(row=14,column=1,sticky=W,padx=20)

        #========Widget Variable===========
        root.name_var = StringVar()
        root.ph_var = StringVar()
        root.dobyear = StringVar()
        root.dobmonth = StringVar()
        root.dobday = StringVar()
        root.lastplace = StringVar()
        root.complainname = StringVar()
        root.policeincharge = StringVar()
        root.age = StringVar()

        #========Inout Widget Creation======
        txtname = Entry(DataFrameLeft,textvariable=root.name_var,highlightthickness=1, font=("arial", 10, "bold"), bd=2, width=20,relief='flat')
        phnumber = Entry(DataFrameLeft,textvariable=root.ph_var,highlightthickness=1, font=("arial", 10, "bold"), bd=2, width=20,relief='flat')
        dobdate = Entry(DataFrameLeft,textvariable=root.dobday,highlightthickness=1, font=("arial", 10, "bold"), bd=2, width=20,relief='flat')
        dobmonth = Entry(DataFrameLeft,textvariable=root.dobmonth,highlightthickness=1, font=("arial", 10, "bold"), bd=2, width=20,relief='flat')
        dobyear = Entry(DataFrameLeft,textvariable=root.dobyear,highlightthickness=1, font=("arial", 10, "bold"), bd=2, width=20,relief='flat')
        lastplace = Entry(DataFrameLeft, textvariable=root.lastplace,highlightthickness=1, font=("arial", 10, "bold"), bd=2, width=20,relief='flat')
        compalinname = Entry(DataFrameLeft, textvariable = root.complainname,highlightthickness=1, font=("arial", 10, "bold"), bd=2, width=20,relief='flat')
        desription = Text(DataFrameLeft, height=10,width=30,highlightthickness=1,relief='flat')
        policeincharge = Entry(DataFrameLeft,textvariable = root.policeincharge,highlightthickness=1, font=("arial", 10, "bold"), bd=2, width=20,relief='flat')
        ageEntry = Entry(DataFrameLeft,highlightthickness=1, font=("arial", 10, "bold"), bd=2, width=20,relief='flat')

        # =====Dropdown box======
        n = tk.StringVar()
        genderchoose = ttk.Combobox(DataFrameLeft, width=20, textvariable=n)
        genderchoose['values'] = ('   ',' Male',
                                  ' Female',
                                  ' Others',)

        s = tk.StringVar()
        Statuschoose = ttk.Combobox(DataFrameLeft, width=20, textvariable=s)
        Statuschoose['values'] = (' Missing',
                                  ' Found',)

        #=========Border Colour Config============
        txtname.config(highlightbackground= "black")
        phnumber.config(highlightbackground= "black")
        dobyear.config(highlightbackground= "black")
        dobmonth.config(highlightbackground= "black")
        dobdate.config(highlightbackground= "black")
        lastplace.config(highlightbackground= "black")
        compalinname.config(highlightbackground= "black")
        desription.config(highlightbackground= "black")
        policeincharge.config(highlightbackground= "black")
        desription.config(highlightbackground= "black")

        #======= Location of widgets ==========
        txtname.grid(row=3, column=3,padx=5,pady=5)
        phnumber.grid(row=4, column=3,padx=5,pady=5)
        dobdate.grid(row=6, column=3,padx=5,pady=5)
        dobmonth.grid(row=7, column=3,padx=5,pady=5)
        dobyear.grid(row=8, column=3,padx=5,pady=5)
        genderchoose.grid(row=5, column=3,padx=5,pady=5)
        genderchoose.current(0)
        lastplace.grid(row=10,column=3,padx=5,pady=5)
        compalinname.grid(row=11,column=3,padx=5,pady=5)
        desription.grid(row=12,column=3,padx=5,pady=5)
        policeincharge.grid(row=13,column=3,padx=5,pady=5)
        Statuschoose.grid(row=14,column=3,padx=5,pady=5)
        Statuschoose.current(0)

        #======Submit Button======
        Button(DataFrameLeft,text="Register",command=submit,width=20,font=("arial", 12),bg="blue",fg="white",relief='flat').grid(row=15, column=2, padx=5,pady=7)
        Button(DataFrameLeft,text="Result",command=self.Result_win,width=20,font=("arial", 12),bg="green",fg="white",relief='flat').grid(row=16, column=2, padx=5,pady=7)
        Button(DataFrameLeft,text="Exit",command=root.destroy,width=20,font=("arial", 12),bg="red",fg="white",relief='flat').grid(row=17, column=2, padx=5,pady=7)

    def Result_win(self):
        self.new_window = Toplevel(self.root)
        self.appp = result(self.new_window)

class result:
    def __init__(self, root):
        self.root = root
        self.root.title("Result")   
        self.root.geometry("1000x750+200+42")

        lbltitle = Label(self.root, text="Result", fg="black",
                         font=("ar", 20, "bold"))
        lbltitle.pack(side=TOP, fill=X)
        # =========FRAMES==========================

        frame = Frame(self.root, bd=12)
        frame.place(x=0, y=100, width=1000, height=400)

        DataFrameLeft = Frame(frame, bd=12, padx=20)
        DataFrameLeft.place(x=0, y=0, width=700, height=360)

        ButtonFrame = Frame(frame, bd=12, padx=20)
        ButtonFrame.place(x=701, y=0, width=540, height=350)

        DetailsFrame = Frame(self.root, bd=10, relief=RIDGE)
        DetailsFrame.place(x=0, y=500, width=1000, height=250)

        # ================Lables======================
        lblsrl = Label(DataFrameLeft, text="Serial Number",font=("ar",12,"bold"), padx=2, pady=6)
        lblsrl.grid(row=0, column=0)

        lblname = Label(DataFrameLeft, text="Name", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lblname.grid(row=1, column=0)

        lblgender = Label(DataFrameLeft, text="Gender", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lblgender.grid(row=2, column=0)

        lbldate = Label(DataFrameLeft, text="Date", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lbldate.grid(row=3, column=0)

        lbltime = Label(DataFrameLeft, text="Time", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lbltime.grid(row=4, column=0)

        lbldobday = Label(DataFrameLeft, text="DOB Day", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lbldobday.grid(row=5, column=0)

        lbldobmonth = Label(DataFrameLeft, text="DOB Month", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lbldobmonth.grid(row=6, column=0)

        lbldobyear = Label(DataFrameLeft, text="DOB Year", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lbldobyear.grid(row=7, column=0)

        lblphno = Label(DataFrameLeft, text="Phone Number", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lblphno.grid(row=0, column=3)

        lblage = Label(DataFrameLeft, text="Age", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lblage.grid(row=1, column=3)

        lbllastrepoetplace = Label(DataFrameLeft, text="Last Reported Place", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lbllastrepoetplace.grid(row=2, column=3)

        lblcomplainantfullname = Label(DataFrameLeft, text="Complainant's Full Name", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lblcomplainantfullname.grid(row=3, column=3)

        lbldescription = Label(DataFrameLeft, text="Description", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lbldescription.grid(row=4, column=3)

        lblpolicestnincharge = Label(DataFrameLeft, text="Police Station Incharge", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lblpolicestnincharge.grid(row=5, column=3)

        lblstatus = Label(DataFrameLeft, text="Status", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lblstatus.grid(row=6, column=3)


        # ===========Text Entry=============

        self.name_var = StringVar()
        self.ph_var = StringVar()
        self.dobyear = StringVar()
        self.dobmonth = StringVar()
        self.dobday = StringVar()
        self.lastplace = StringVar()
        self.complainname = StringVar()
        self.policeincharge = StringVar()
        self.desc = StringVar()
        self.age = StringVar()
        self.time = StringVar()
        self.date = StringVar()
        self.srl = StringVar()
        self.gender = StringVar()
        self.status = StringVar()

        
        txtname = Entry(DataFrameLeft, textvariable=self.name_var, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        txtname.grid(row=1, column=1)
        phnumber = Entry(DataFrameLeft, textvariable=self.ph_var, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        phnumber.grid(row=0, column=4)
        dobdate = Entry(DataFrameLeft, textvariable=self.dobday, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        dobdate.grid(row=5, column=1)
        dobmonth = Entry(DataFrameLeft, textvariable=self.dobmonth, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        dobmonth.grid(row=6, column=1)
        dobyear = Entry(DataFrameLeft, textvariable=self.dobyear, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        dobyear.grid(row=7, column=1)
        lastplace = Entry(DataFrameLeft, textvariable=self.lastplace, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        lastplace.grid(row=2, column=4)
        complainname = Entry(DataFrameLeft, textvariable=self.complainname, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        complainname.grid(row=3, column=4)
        policeincharge = Entry(DataFrameLeft, textvariable=self.policeincharge, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        policeincharge.grid(row=5, column=4)
        ageEntry = Entry(DataFrameLeft, textvariable=self.age, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        ageEntry.grid(row=1, column=4)
        desription = Entry(DataFrameLeft, textvariable=self.desc, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        desription.grid(row=4, column=4)
        Serialno = Entry(DataFrameLeft, textvariable=self.srl, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        Serialno.grid(row=0, column=1)
        Date = Entry(DataFrameLeft, textvariable=self.date, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        Date.grid(row=3, column=1)
        Time = Entry(DataFrameLeft, textvariable=self.time, highlightthickness=1, font=("arial", 10, "bold"),
                        bd=2, width=20, relief='flat')
        Time.grid(row=4, column=1)

        #================Combo Box=========

        comGender=ttk.Combobox(DataFrameLeft,font=("arial", 10, "bold"),width=20,textvariable=self.gender)
        comGender["values"]=("Male","Female")
        comGender.grid(row=2,column=1)

        comStatus=ttk.Combobox(DataFrameLeft,font=("arial", 10, "bold"),width=20,textvariable=self.status)
        comStatus["values"]=("Missing","Found")
        comStatus.grid(row=6,column=4)

        # ==========Config==================
        txtname.config(highlightbackground="black")
        phnumber.config(highlightbackground="black")
        dobdate.config(highlightbackground="black")
        dobmonth.config(highlightbackground="black")
        dobyear.config(highlightbackground="black")
        lastplace.config(highlightbackground="black")
        complainname.config(highlightbackground="black")
        policeincharge.config(highlightbackground="black")
        ageEntry.config(highlightbackground="black")
        desription.config(highlightbackground="black")
        Serialno.config(highlightbackground="black")
        Time.config(highlightbackground="black")
        Date.config(highlightbackground="black")

        
        #============Button Frame============
        
        Button(ButtonFrame,text="Update",command=self.update,width=20,font=("arial", 12),bg="blue",fg="white",relief='flat').grid(row=15, column=2, padx=5,pady=7)
        Button(ButtonFrame,text="Generate PDF",command=self.pdf,width=20,font=("arial", 12),bg="blue",fg="white",relief='flat').grid(row=16, column=2, padx=5,pady=7)
        Button(ButtonFrame,text="send Result sms",command=self.sms,width=20,font=("arial", 12),bg="blue",fg="white",relief='flat').grid(row=17, column=2, padx=5,pady=7)
        Button(ButtonFrame,text="Back",command=root.destroy,width=20,font=("arial", 12),bg="red",fg="white",relief='flat').grid(row=18, column=2, padx=5,pady=7)

        #============Table Frame=============
        DetailsFrame = Frame(self.root, bd=10, relief=RIDGE)
        DetailsFrame.place(x=0, y=500, width=1000, height=250)

        xscroll = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
        self.missing_table = ttk.Treeview(DetailsFrame, column=(
            "sr", "name", "ph", "Gender", "Date", "Time", "Day", "Month", "Year", "Age", "LastReport", "Complain",
            "Desc", "Policestn", "Status"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        xscroll.config(command=self.missing_table.xview)
        yscroll.config(command=self.missing_table.yview)

        self.missing_table.heading("sr", text="Serial Number")
        self.missing_table.heading("name", text="Name")
        self.missing_table.heading("ph", text="Phone Number")
        self.missing_table.heading("Gender", text="Gender")
        self.missing_table.heading("Time", text="Time")
        self.missing_table.heading("Date", text="Date")
        self.missing_table.heading("Day", text="DOB Day")
        self.missing_table.heading("Month", text="DOB Month")
        self.missing_table.heading("Year", text="DOB Year")
        self.missing_table.heading("Age", text="Age")
        self.missing_table.heading("LastReport", text="Last Reported Place")
        self.missing_table.heading("Complain", text="Complainant's Full Name")
        self.missing_table.heading("Desc", text="Description About Missing Person")
        self.missing_table.heading("Policestn", text="Police Station Incharge")
        self.missing_table.heading("Status", text="Status")

        self.missing_table.column("sr", width="100")
        self.missing_table.column("name", width="100")
        self.missing_table.column("ph", width="100")
        self.missing_table.column("Gender", width="100")
        self.missing_table.column("Date", width="100")
        self.missing_table.column("Time", width="100")
        self.missing_table.column("Day", width="100")
        self.missing_table.column("Month", width="100")
        self.missing_table.column("Year", width="100")
        self.missing_table.column("Age", width="100")
        self.missing_table.column("LastReport", width="100")
        self.missing_table.column("Complain", width="100")
        self.missing_table.column("Desc", width="100")
        self.missing_table.column("Policestn", width="100")
        self.missing_table.column("Status", width="100")

        self.missing_table["show"] = "headings"

        self.missing_table.pack(fill=BOTH, expand=1)
        self.missing_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetchdata()

    def update(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", #Enter MYSQL Password 
            database="missing_person")  #create a database if not created
        mycursor = mydb.cursor()
        mycursor.execute("update persons set Name=%s,phnumber=%s,Gender=%s,Date=%s,Time=%s,DOB_Day=%s,DOB_Month=%s,DOB_Year=%s,Age=%s,Last_Reported_Place=%s,Complainants_name=%s,Description=%s,Police_Station_Reported=%s,Missing_Person_Status=%s WHERE Persons_id=%s",(
            self.name_var.get(),
            self.ph_var.get(),
            self.gender.get(),
            self.date.get(),
            self.time.get(),
            self.dobday.get(),
            self.dobmonth.get(),
            self.dobyear.get(),
            self.age.get(),
            self.lastplace.get(),
            self.complainname.get(),
            self.desc.get(),
            self.policeincharge.get(),
            self.status.get(),
            self.srl.get()            
        ))
        
        mydb.commit()
        self.fetchdata()
        mycursor.execute("select * from persons")
        for x in mycursor:
            print(x) 
        

    def fetchdata(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", #Enter MYSQL Password 
            database="missing_person")  #create a database if not created
        mycursor = mydb.cursor()
        mycursor.execute("select * from persons")
        rows = mycursor.fetchall()
        if len(rows) != 0:
            self.missing_table.delete(*self.missing_table.get_children())
            for i in rows:
                self.missing_table.insert("", END, values=i)
            mydb.commit()
        mydb.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.missing_table.focus()
        content=self.missing_table.item(cursor_row)
        row=content["values"]
        self.srl.set(row[0])
        self.name_var.set(row[1])
        self.ph_var.set(row[2])
        self.date.set(row[4])
        self.time.set(row[5])
        self.lastplace.set(row[10])
        self.age.set(row[9])
        self.complainname.set(row[11])
        self.desc.set(row[12])
        self.policeincharge.set(row[13])
        self.dobyear.set(row[8])
        self.dobmonth.set(row[7])
        self.dobday.set(row[6])
        self.gender.set(row[3])
        self.status.set(row[14])
      
    def sms(self):
        import requests
        import json
        from tkinter.messagebox import showerror,showinfo

        def send_sms(number, message):
            url = "https://www.fast2sms.com/dev/bulk"

            #Create a account on fast2sms using www.fast2sms.com and get 

            prams = {
                "authorization" : "",
                "sender_id" : "sender_id",
                "route" : "p",
                "language" : "unicode",
                "numbers" : number,
                "message" : message
            }
            response = requests.get(url, params= prams)
            dic = response.json()
            print(dic)
            return dic.get('return')

        def btn_clk():
             num = textNumber.get()
             msg = textMessage.get("1.0", END)
             r = send_sms(num, msg)
             if r:
                 showinfo("msg info", "sent succesfully")
             else:
                 showerror("msg info", "not sent")

            

        sms_window = Toplevel(master=None)
        sms_window.title("SMS")
        sms_window.geometry("500x700")

        smsframe = Frame(sms_window, bd=12, relief=RIDGE)
        smsframe.place(x=0, y=0, width=500, height=700)

        Label(smsframe, text ="NUMBER", relief = FLAT, width = 10).grid(row = 1, column = 0)
        textNumber = Entry(smsframe, relief = SUNKEN, font = ("arial", 12), bg ="white", fg ="black", width = 20)
        textNumber.insert(0, "")
        textNumber.configure(state = "normal")
        textNumber.grid(row = 1, column = 1)

        Label(smsframe, text ="MESSAGE", relief = FLAT, width = 10).grid(row = 3, column = 0)
        textMessage = Text(smsframe, relief = SUNKEN, font = ("arial", 12), height = 10, width = 20)
        textMessage.insert('1.0',"Serial Number :- "+self.srl.get() + "\n" + "Name :- "+self.name_var.get()+ "\n" + "Status :- "+ self.status.get())
        textMessage.grid(row = 3, column =1)

        sendbtm = Button(smsframe, text ="SEND",relief = FLAT, bg="green", fg ="white", command = btn_clk).grid(row = 4, column =2)
        qtbtn = Button(smsframe, text ="QUIT", bg ="red", fg ="white", command = quit).grid(row = 4, column = 0)


    

    def pdf(self):
        new_window = Toplevel(master=None)
        new_window.title("PDF")
        new_window.geometry("500x700")
        
        frame = Frame(new_window, bd=12, relief=RIDGE)
        frame.place(x=0, y=0, width=500, height=700)

        Name = Label(frame, text="Name :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        Name.grid(row=0, column=1)
        NameEntry = Label(frame, text=self.name_var.get(), font=(
            "ar", 12, "bold"), padx=2, pady=6)
        NameEntry.grid(row=0, column=2)

        Gender = Label(frame, text="Gender :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        Gender.grid(row=1, column=1)
        GenderEntry = Label(frame, text=self.gender.get(), font=(
            "ar", 12, "bold"), padx=2, pady=6)
        GenderEntry.grid(row=1, column=2)

        Date = Label(frame, text="Date of registration :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        Date.grid(row=2, column=1)
        DateEntry = Label(frame, text=self.date.get(), font=(
            "ar", 12, "bold"), padx=2, pady=6)
        DateEntry.grid(row=2, column=2)

        Time = Label(frame, text="Time of Registration :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        Time.grid(row=3, column=1)
        TimeEntry = Label(frame, text=self.time.get(), font=(
            "ar", 12, "bold"), padx=2, pady=6)
        TimeEntry.grid(row=3, column=2)

        date = self.dobday.get() +" / "+ self.dobmonth.get() +" / "+ self.dobyear.get()

        dobday = Label(frame, text="DOB Date :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        dobday.grid(row=4, column=1)
        dobdayEntry = Label(frame, text=date, font=(
            "ar", 12, "bold"), padx=2, pady=6)
        dobdayEntry.grid(row=4, column=2)

        phno = Label(frame, text="Phone Number :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        phno.grid(row=5, column=1)
        phnoEntry = Label(frame, text=self.ph_var.get(), font=(
            "ar", 12, "bold"), padx=2, pady=6)
        phnoEntry.grid(row=5, column=2)

        Age = Label(frame, text="Age :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        Age.grid(row=6, column=1)
        AgeEntry = Label(frame, text=self.age.get(), font=(
            "ar", 12, "bold"), padx=2, pady=6)
        AgeEntry.grid(row=6, column=2)

        lastopalce = Label(frame, text="Last Reported Place :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lastopalce.grid(row=7, column=1)
        lastopalceEntry = Label(frame, text=self.lastplace.get(), font=(
            "ar", 12, "bold"), padx=2, pady=6)
        lastopalceEntry.grid(row=7, column=2)

        complainname = Label(frame, text="Complainant's Name :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        complainname.grid(row=8, column=1)
        complainnameEntry = Label(frame, text=self.complainname.get(), font=(
            "ar", 12, "bold"), padx=2, pady=6)
        complainnameEntry.grid(row=8, column=2)

        Description = Label(frame, text="Description :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        Description.grid(row=9, column=1)
        DescriptionEntry = Label(frame, text=self.desc.get(), font=(
            "ar", 12, "bold"), padx=2, pady=6)
        DescriptionEntry.grid(row=9, column=2)

        policestation = Label(frame, text="Police Station Incharge :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        policestation.grid(row=10, column=1)
        policestationEntry = Label(frame, text=self.policeincharge.get(), font=(
            "ar", 12, "bold"), padx=2, pady=6)
        policestationEntry.grid(row=10, column=2)

        Status = Label(frame, text="Status :- ", font=(
            "ar", 12, "bold"), padx=2, pady=6)
        Status.grid(row=11, column=1)
        StatusEntry = Label(frame, text=self.status.get(), font=(
            "ar", 12, "bold"), padx=2, pady=6)
        StatusEntry.grid(row=11, column=2)

        def pdf():
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size = 25)
            
            pdf.set_text_color(255,0,0)
            pdf.cell(200, 40,txt = "Missing Person Report",
            ln = 1, align = 'C')

            pdf.set_font("Arial", size = 15)
            pdf.set_text_color(0,0,0)
            pdf.cell(200, 10, txt = "Serial Number :- " + self.srl.get(),
            ln = 2, align = 'C')

            pdf.cell(200, 10, txt = "Name :- " + self.name_var.get(),
            ln = 2, align = 'L')

            pdf.cell(200, 10, txt = "Gender :- " + self.gender.get(),
            ln = 4, align = 'L')

            pdf.cell(200, 10, txt = "Date of Birth :- " + date,
            ln = 5, align = 'L')

            pdf.cell(200, 10, txt = "Age :- " + self.age.get(),
            ln = 6, align = 'L')

            pdf.cell(200, 10, txt = "Phone Number :- " + self.ph_var.get(),
            ln = 7, align = 'L')

            pdf.cell(200, 10, txt = "Date Of Registration :- " + self.date.get(),
            ln = 8, align = 'L')

            pdf.cell(200, 10, txt = "Time Of Registration :- " + self.time.get(),
            ln = 9, align = 'L')

            pdf.cell(200, 10, txt = "Complainant's Name :- " + self.complainname.get(),
            ln = 10, align = 'L')

            pdf.cell(200, 10, txt = "Last Reported Place :- " + self.lastplace.get(),
            ln = 11, align = 'L')

            pdf.cell(200, 10, txt = "Description :- " + self.desc.get(),
            ln = 12, align = 'L')

            pdf.cell(200, 10, txt = "Police Station Incharge :- " + self.policeincharge.get(),
            ln = 13, align = 'L')

            pdf.cell(200, 10, txt = "Status :- " + self.status.get(),
            ln = 14, align = 'L')
            
            
            # save the pdf with name .pdf
            pdf.output(self.name_var.get()+"_"+self.age.get()+"_"+self.ph_var.get()+ ".pdf")
            

        Button(frame,text="Generate PDF",command=pdf,width=20,font=("arial", 12),bg="blue",fg="white",relief='flat').grid(row=13, column=2, padx=5,pady=11)

if __name__ == "__main__":
    main()
