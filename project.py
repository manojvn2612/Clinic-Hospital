#-------------------------------------------------------------------------------importing modules-------------------------------------------------------------------------------------------#

import time
import tkinter.messagebox
import random as rd
import datetime 
import mysql.connector as sqltor
import os
import pyttsx3
import webbrowser
from tkinter import *
from tooltips import CreateToolTip

#---------------------------------creating directory------------------------------------#

filename = datetime.datetime.now()
directory = filename.strftime("%d %B %Y")
parent_dir = "History"
path = os.path.join(parent_dir, directory)
file_name=filename.strftime("%d %B %Y %H.%M.%S")
try:
	os.makedirs(path, exist_ok = True)
	print("Directory '%s' created successfully" % directory)
except OSError as error:
	print("Directory '%s' can not be created" % directory)
directory_photo = 'patients photo'
parent_dir = "Profile"
path = os.path.join(parent_dir, directory_photo)
try:
        os.makedirs(path, exist_ok = True)
        print("Directory '%s' created successfully" % directory_photo)
except OSError as error:
        print("Directory '%s' can not be created" % directory_photo)


#---------------------------making txt file for saving the history---------------------#

D = time.strftime("%D")
r = time.strftime("%r")
def create_file():
    # %d - date, %B - month, %Y - Year, %H - Hours, %M - Minutes, %S - Seconds
    with open('History/'+directory+'/'+file_name+".txt", "w") as file:
            file.write('hello\n')
            file.write("opened file on "+D+" at "+r+"\n")
create_file()

#-----------------------------main window-------------------------------#

root_main=Tk()
root_main.title('ALL IN ONE BY MANOJ')
frame=Frame(height=100,width=100)
frame.pack()

#---------------------------welcoming voice-------------------------#

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.runAndWait()
engine.say('Hello everyone!!')
pyttsx3.speak("Namaste!!")
pyttsx3.speak("Welcome if you are using for first time please read manual before use. it is the book icon. Please enjoy this app.")

#---------------------------program for medical emergency------------------------#

def medical(*args):
    root_medical=Toplevel(root_main)
    root_medical.title('medical')
    def medical_history():
            with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                    file.write(D+' '+r+':\tOpened medical tab from main application\n')
    medical_history()
    root_medical.wm_attributes('-toolwindow','True')

    #-------------------------program for hospital--------------------------#

    def hospital():
        con=sqltor.connect(host="localhost",user="root",password="panvel123")
        def hospital_history():
                with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                        file.write(D+' '+r+':\tOpened hospital/clinic application from main application\n')
        hospital_history()
        #-------------------------mysql connectivity------------------------#

        cur=con.cursor()
        cur = con.cursor(buffered=True) 
        cur.execute("use manoj")
        cur.execute("create table if not exists apt"
                  "("
                  "idno varchar(12) primary key,"
                  "name char(20),"
                  "age char(3),"
                  "gender char(1),"
                  "phone varchar(10),"
                  "bg varchar(3))")
        def connected():
                with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                        file.write(D+' '+r+':\tConnected to mqsql server\n')
        connected()    
        #---------------------------connected------------------------------------#
        def entry():

            #  Message for registration

            global e1,e2,e3,e4,e5,e6
            p1=e1.get()
            p2=e2.get()
            p3=e3.get()
            p4=e4.get()
            p5=e5.get()
            p6=e6.get()
            cur.execute('insert into apt values(%s,%s,%s,%s,%s,%s)',(p1,p2,p3,p4,p5,p6,))
            con.commit()
            tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN REGISTERED")
            def add_registration_details():
                with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                    file.write(D+' '+r+'\t'+"new records added\n")
                    file.write(D+' '+r+':\t'+f"{p1}\n"+D+' '+r+':\t'+f"{p2}\n"+D+' '+r+':\t'+f"{p3}\n"+D+' '+r+':\t'+f"{p4}\n"+D+' '+r+'\t'+f"{p5}\n"+D+' '+r+'\t'+f"{p6}\n")
            add_registration_details()
            if len(p1)==0:
                tkinter.messagebox.showwarning('ERROR','Please add info...')
            else:
                if len(p1)<10:
                    tkinter.messagebox.showwarning('ERROR','please add proper input')

        def register(*args):

            #  For registration
            
            global e1,e2,e3,e4,e5,e6
            root_registration=Toplevel(root_medical)
            root_registration.title('Registration')
            label=Label(root_registration,text="REGISTER YOURSELF",font='arial 25 bold')
            label.pack()
            frame=Frame(root_registration,height=500,width=200)
            frame.pack()
            root_registration.attributes('-topmost',True)
            root_registration.bind('<Return>',entry)
            l1=Label(root_registration,text="PATIENT ID")
            l1.place(x=10,y=130)
            e1=tkinter.Entry(root_registration)
            e1.place(x=100,y=130)
            e1.insert(0,'Please add your Patient Id')
            def patient_id_text(e):
                e1.delete(0,'end')
            e1.bind('<FocusIn>',patient_id_text)
            l2=Label(root_registration,text="NAME")
            l2.place(x=10,y=170)
            e2=tkinter.Entry(root_registration)
            e2.place(x=100,y=170)
            e2.insert(0,'Please add your Name')
            def name_text(e):
                e2.delete(0,'end')
            e2.bind('<FocusIn>',name_text)
            l3=Label(root_registration,text="AGE")
            l3.place(x=10,y=210)
            e3=tkinter.Entry(root_registration)
            e3.place(x=100,y=210)
            e3.insert(0,'Please add your Age')
            def age_text(e):
                e3.delete(0,'end')
            e3.bind('<FocusIn>',age_text)
            l4=Label(root_registration,text="GENDER M/F")
            l4.place(x=10,y=250)
            e4=tkinter.Entry(root_registration)
            e4.place(x=100,y=250)
            e4.insert(0,'Please add your Gender M/F')
            def gender_text(e):
                e4.delete(0,'end')
            e4.bind('<FocusIn>',gender_text)
            l5=Label(root_registration,text="PHONE")
            l5.place(x=10,y=290)
            e5=tkinter.Entry(root_registration)
            e5.place(x=100,y=290)
            e5.insert(0,'Please add your Phone No.')
            def patient_id_text(e):
                e5.delete(0,'end')
            e5.bind('<FocusIn>',patient_id_text)
            l6=Label(root_registration,text="BLOOD GROUP")
            l6.place(x=10,y=330)
            e6=tkinter.Entry(root_registration)
            e6.place(x=100,y=330)
            e6.insert(0,'Please add your Blood Group.')
            def bg_text(e):
                e6.delete(0,'end')
            e6.bind('<FocusIn>',bg_text)
            b_registration=Button(root_registration,text="SUBMIT",command=entry)
            b_registration.place(x=150,y=370)
            b_hospital_hospital_submit_tooltip = CreateToolTip(b_registration, "submit the form to our clinic and complete your registration")
            root_registration.resizable(False,False)
            root_registration.bind('<Return>',entry)
            root_registration.wm_attributes('-toolwindow','True')
            root_registration.mainloop()
        def apo_details():

            #  Message for appointment
            
            global x2
            p1=x2.get()    
            if int(p1)==1:
                i=("Dr. Manoj \nRoom no:- 201")
                j=("Dr. Shashank \nRoom no:- 202")
                q=(i,j)
                h=rd.choice(q) 
                u=(23,34,12,67,53,72)
                o=rd.choice(u)        
                det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=3),'\nAppointmnet no:-',o)
                tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
            elif int(p1)==2:
                i=("Dr. Shubham \nRoom no. 207")
                j=("Dr. Vinayak \nRoom no. 208")
                q=(i,j)
                h=rd.choice(q) 
                u=(23,34,12,67,53,72)
                o=rd.choice(u)        
                det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=5),'\nAppointmnet no:-',o)
                tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
            elif int(p1)==3:
                i=("Dr. Suraj \nRoom no. 203")
                j=("Dr. Ashwin \nRoom no. 204")
                q=(i,j)
                h=rd.choice(q) 
                u=(23,34,12,67,53,72)
                o=rd.choice(u)        
                det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=3),'\nAppointmnet no:-',o)
                tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
            elif int(p1)==4:
                i=("Dr. Ajay, \nRoom no. 209")
                j=("Dr. Ranveer \nRoom no. 200")
                q=(i,j)
                h=rd.choice(q) 
                u=(23,34,12,67,53,72)
                o=rd.choice(u)        
                det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=6),'\nAppointmnet no:-',o)
                tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
            elif int(p1)==5:
                i=("Dr. Swati \nRoom no. 205")
                j=("Dr. Shreya \nRoom no. 206")
                q=(i,j)
                h=rd.choice(q) 
                u=(23,34,12,67,53,72)
                o=rd.choice(u)        
                det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=4),'\nAppointmnet no:-',o)
                tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)   
            elif int(p1)==6:
                i=("Dr. Modi \nRoom no. 001")
                j=("Dr. Amit \nRoom no. 002")
                k=("Dr. Sanjay \nRoom no. 003")
                l=("Dr. Tejesvi \nRoom no. 004")
                q=(i,j,k,l)
                h=rd.choice(q)
                u=(23,34,12,67,53,72)
                o=rd.choice(u)
                det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=1),'\nAppointmnet no:-',o)
                tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
            else:
                tkinter.messagebox.showwarning('WRONG INPUT','PLEASE ENTER VALID VALUE')
            def add_appointment_details():
                with open('History/'+directory+'/'+file_name+".txt",'+a') as file:
                        file.write(D+' '+r+':\t'+'inserted '+f'{p1}'+' in the row\n'+D+' '+r+':\tclicked for appoinment and '+h+' is patients doctor and room no.')
            add_appointment_details()
        def get_apoint(*args):

            #  For appointment
            
            global x1,x2
            p1=x1.get()  
            cur.execute('select * from apt where idno=(%s)',(p1,))
            dat=cur.fetchall()
            a =[]
            for i in dat:
                a.append(i)
                if len(a)==0:
                    tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
                else:
                    root_appointment=Toplevel(root_medical)
                    root_appointment.title('Appointment')
                    label=Label(root_appointment,text="APPOINTMENT",font='arial 25 bold')
                    label.pack()
                    frame=Frame(root_appointment,height=500,width=300)
                    frame.pack()
                    root_appointment.attributes('-topmost',True)
                    if i[3]=='M' or i[3]=='m':
                        x="Mr."
                        name2=Label(root_appointment,text=i[1])
                        name2.place(x=140,y=80)
                    else:
                        x="Mrs\Ms."
                        name2=Label(root_appointment,text=i[1])
                        name2.place(x=170,y=80)
                    for i in dat:
                        name=Label(root_appointment,text='WELCOME')
                        name.place(x=50,y=80)
                        name1=Label(root_appointment,text=x)
                        name1.place(x=120,y=80)
                        age=Label(root_appointment,text='AGE:-')
                        age.place(x=50,y=100)
                        age1=Label(root_appointment,text=i[2])
                        age1.place(x=100,y=100)
                        phone=Label(root_appointment,text='PHONE:-')
                        phone.place(x=50,y=120)
                        phone1=Label(root_appointment,text=i[4])
                        phone1.place(x=100,y=120)
                        bg=Label(root_appointment,text='BLOOD GROUP:-')
                        bg.place(x=50,y=140)
                        bg1=Label(root_appointment,text=i[5])
                        bg1.place(x=150,y=140)
                        L=Label(root_appointment,text='DEPARTMENTS')
                        L.place(x=50,y=220)
                        L1=Label(root_appointment,text="1.Cardiologist ")
                        L1.place(x=50,y=250)
                        L2=Label(root_appointment,text='2.Rheumatologist')
                        L2.place(x=50,y=270)
                        L3=Label(root_appointment,text='3.Psychitrist')
                        L3.place(x=50,y=290)
                        L4=Label(root_appointment,text='4.Neurologist')
                        L4.place(x=50,y=310)
                        L5=Label(root_appointment,text='5.Otolaryngonologist')
                        L5.place(x=50,y=330)
                        L6=Label(root_appointment,text='6.MI Room')
                        L6.place(x=50,y=350)
                        L7=Label(root_appointment,text='Enter')
                        L7.place(x=100,y=370)
                        x2=tkinter.Entry(root_appointment)
                        x2.place(x=150,y=370)
                        B1=Button(master=root_appointment,text='Submit',command=apo_details)
                        B1.place(x=120,y=440)   
                        root_appointment.resizable(False,False)
                        root_appointment.wm_attributes('-toolwindow','True')
                        root_appointment.mainloop()
                        def add_appoinment_made_details():
                            with open('History/'+directory+'/'+file_name+".txt",'+a') as file:
                                file.write(D+' '+r+'\t'+f"{p1}"+" is patient id\n")
                        add_appoinment_made_details()

        def apoint():
            #  For Adhaar no.(patient id) input
            global x1
            root_prior_appointment=Toplevel(root_medical)
            root_prior_appointment.title('Appointment')
            label=Label(root_prior_appointment,text="APPOINTMENT",font='arial 25 bold')
            label.pack()
            frame=Frame(root_prior_appointment,height=200,width=200)
            frame.pack()
            l1=Label(root_prior_appointment,text="Patient Id")
            l1.place(x=10,y=130)
            x1=tkinter.Entry(root_prior_appointment)
            x1.place(x=100,y=130)
            b1=Button(root_prior_appointment,text='Submit',command=get_apoint)
            b1.place(x=100,y=160)
            root_prior_appointment.resizable(True,True)
            root_prior_appointment.wm_attributes('-toolwindow','True')
            root_prior_appointment.attributes('-topmost',True)                            
            root_prior_appointment.bind('<Return>',get_apoint)
            root_prior_appointment.mainloop()
        def lst_doc():

            #  List of doctors

            root_Doctors_list=Toplevel(root_medical)
            root_Doctors_list.title("Doctor's list")
            l=["Dr. Manoj","Dr. Shashank","Dr. Vinayak","Dr. Shubham","Dr. Modi","Dr. Suraj","Dr. Ashwin","Dr. Amit","Dr. Ajay","Dr. Ranveer",'Dr. Shreya','Dr. Swat','Dr. Sanjay','Dr. modi']
            m=["Cardiologist","Cardiologist","Psychatrist","Psychatrist","Otolaryngonologist","Otolaryngonologist","Rheumatologist","Rheumatologist","Neurologist","Neurologist",'MI room','MI room','MI room','MI room']
            n=[201, 202,203,204,205,206,207,208,209,200,401,402,403,404]
            frame=Frame(root_Doctors_list,height=500,width=500)
            frame.pack()
            root_Doctors_list.attributes('-toolwindow') 
            l1=Label(root_Doctors_list,text='NAME OF DOCTORS') 
            l1.place(x=20,y=10)
            count=20
            def list_doc():
                    with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                            file.write(D+' '+r+':\topened list of doctors\n')
            list_doc()
            for i in l:
                count=count+20
                l=Label(root_Doctors_list,text=i)
                l.place(x=20,y=count)
                l2=Label(root_Doctors_list,text='DEPARTMENT')
                l2.place(x=140,y=10)
                count1=20
            for i in m:
                count1=count1+20
                l3=Label(root_Doctors_list,text=i)
                l3.place(x=140,y=count1)
                l4=Label(root_Doctors_list,text='ROOM NO')
                l4.place(x=260,y=10)
                count2=20
            for i in n:
                count2=count2+20
                l5=Label(root_Doctors_list,text=i)
                l5.place(x=270,y=count2)
            root_Doctors_list.resizable(False,False)
            root_Doctors_list.mainloop()
        def ser_avail():
            root_Services_available=Tk()
            root_Services_available.title('Services Available')
            frame=Frame(root_Services_available,height=500,width=500)
            frame.pack()
            l1=Label(root_Services_available,text='SERVICES AVAILABLE')
            l1.place(x=20,y=10)
            texta=["X-Ray","MRI","CT Scan","Endoscopy","Dialysis","Ultrasound ","EEG","ENMG","ECG"]
            count1=20
            def service():
                    with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                            file.write(D+' '+r+'Opened services available tab\n')
            for name in texta:
                count1=count1+20
                l3=Label(root_Services_available,text=name)
                l3.place(x=20,y=count1)
                l2=Label(root_Services_available,text='ROOM NO.')
                l2.place(x=140,y=10)
                room=[101,102,103,104,105,301,302,303,304]
                count2=20
            for name in room:
                count2=count2+20
                l4=Label(root_Services_available,text=name)
                l4.place(x=140,y=count2)
                l5=Label(root_Services_available,text='To avail any of these please contact on our no.:- +91 9423912378')
                l5.place(x=20,y=240)
                root_Services_available.resizable(False,False)
                root_Services_available.mainloop()
        def mod_sub():
            global x3
            root_prior_modification=Toplevel(root_medical)
            root_prior_modification.title('Modification')
            label=Label(root_prior_modification,text="MODIFICATION",font='arial 25 bold')
            label.pack()
            frame=Frame(root_prior_modification,height=200,width=200)
            frame.pack()
            l1=Label(root_prior_modification,text="Patient Id")
            l1.place(x=10,y=130)
            x3=tkinter.Entry(root_prior_modification)
            x3.place(x=100,y=130)
            b1=Button(root_prior_modification,text='Submit',command=modify)
            b1.place(x=100,y=160)
            root_prior_modification.bind('<Return>',modify)
            root_prior_modification.resizable(False,False)
            root_prior_modification.mainloop()
        def modify(*args):
            global x3,x5
            p1=x3.get()
            cur.execute('select * from apt where idno=(%s)',(p1,))
            dat=cur.fetchall()
            with open('History/'+directory+'/'+file_name+'.txt','+a') as file:
                    file.write(D+' '+r+':\tverified and put id as '+f'{p1}\n')
            a=[]
            for i in dat:
                a.append(i)
                
                if len(a)==0:
                    tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
                else:
                    global x4
                    root_modification=Toplevel(root_medical)
                    root_modification.title('Modify')
                    frame=Frame(root_modification,height=1000,width=1000)
                    frame.pack()
                    l1=Label(root_modification,text='DATA MODIFICATION',font="arial 15 bold")
                    l1.place(x=75,y=10)
                    l2=Label(root_modification,text='WHAT YOU WANT TO CHANGE')
                    l2.place(x=50,y=200)
                    l3=Label(root_modification,text='1.NAME')
                    l3.place(x=50,y=220)
                    l4=Label(root_modification,text='2.AGE')
                    l4.place(x=50,y=240)
                    l5=Label(root_modification,text='3.GENDER')
                    l5.place(x=50,y=260)
                    l6=Label(root_modification,text='4.PHONE')
                    l6.place(x=50,y=280)
                    l7=Label(root_modification,text='5.BLOOD GROUP')
                    l7.place(x=50,y=300)
                    root_modification.wm_attributes('-toolwindow','True')
                   # root_modification.bind('<Return>',lambda:[modification_name(),modification_age(),modification_gender(),modification_phone(),modification_blood_group()])
            def pre_modified_details():
                with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                    file.write(D+' '+r+':\t'+' data modified\n')
                    file.write(D+' '+r+':\t'+'previous data is '+f'{dat}'+' i.e.(name,age,gender,phone,blood group) and new data is below\n')
            pre_modified_details()
            def modification_name(*args):
                global x5,x3
                sql_update="update apt set name=%s where idno=%s"
                p5=x5.get()
                inputs=(p5,p1)
                cur.execute(sql_update,inputs)
                con.commit()
                def modified_details_name():
                    with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                        file.write(D+' '+r+':\t'+f"{p5}"+" is entered name\n")
                modified_details_name()

            def modification_age(*args):
                global x6,x3
                sql_update="update apt set age=%s where idno=%s"
                p6=x6.get()
                inputs=(p6,p1)
                cur.execute(sql_update,inputs)
                con.commit()
                def modified_details_age():
                    with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                            file.write(D+' '+r+':\t'+f"{p6}"+" is entered age\n")
                modified_details_age()
            def modification_gender(*args):
                global x7,x3
                sql_update="update apt set gender=%s where idno=%s"
                p7=x7.get()
                inputs=(p7,p1)
                cur.execute(sql_update,inputs)
                con.commit()
                def modified_details_gender():
                        with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                                file.write(D+' '+r+':\t'+f"{p7}"+" is entered gender\n")
                modified_details_gender()
            def modification_phone(*args):
                global x8,x3
                sql_update="update apt set phone=%s where idno=%s"
                p8=x8.get()
                inputs=(p8,p1)
                cur.execute(sql_update,inputs)
                con.commit()
                def modified_details_phone():
                        with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                                file.write(D+' '+r+':\t'+f"{p8}"+" is entered phone\n")
                modified_details_phone()
            def modification_blood_group(*args):
                global x9,x3
                sql_update="update apt set bg=%s where idno=%s"
                p9=x9.get()
                inputs=(p9,p1)
                cur.execute(sql_update,inputs)
                con.commit()
                def modified_bg():
                        with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                                file.write(D+' '+r+':\t'+f"{p9}"+" is entered blood group\n")
                modified_bg()
            for i in dat:
                global x5,x6,x7,x8,x9
                name=Label(root_modification,text='NAME:-')
                name.place(x=50,y=80)
                name1=Label(root_modification,text=i[1])
                name1.place(x=150,y=80)
                age=Label(root_modification,text='AGE:-')
                age.place(x=50,y=100)
                age1=Label(root_modification,text=i[2])
                age1.place(x=150,y=100)
                gen=Label(root_modification,text='GENDER:-')
                gen.place(x=50,y=120)
                gen1=Label(root_modification,text=i[3])
                gen1.place(x=150,y=120)
                pho=Label(root_modification,text='PHONE:-')
                pho.place(x=50,y=140)
                pho1=Label(root_modification,text=i[4])
                pho1.place(x=150,y=140)
                bg=Label(root_modification,text='BLOOD GROUP:-')
                bg.place(x=50,y=160)
                bg1=Label(root_modification,text=i[5])
                bg1.place(x=150,y=160)
                L3=Label(root_modification,text='%s is your id'%p1)
                L3.place(x=50,y=510)
                L1=Label(root_modification,text='OLD DETAILS')
                L1.place(x=50,y=50)
                name_text=i[1]
                L2=Label(root_modification,text='ENTER NAME')
                L2.place(x=50,y=360)
                x5=tkinter.Entry(root_modification)
                x5.insert(0,f'{name_text}')
                x5.place(x=160,y=360)
                age_text=i[2]
                L3=Label(root_modification,text='ENTER AGE')
                L3.place(x=50,y=390)
                x6=tkinter.Entry(root_modification)
                x6.insert(0,f'{age_text}')
                x6.place(x=160,y=390)
                gen_text=i[3]
                L4=Label(root_modification,text='ENTER GENDER')
                L4.place(x=50,y=420)
                x7=tkinter.Entry(root_modification)
                x7.insert(0,f'{gen_text}')
                x7.place(x=160,y=420)
                phone_text=i[4]
                L5=Label(root_modification,text='ENTER PHONE')
                L5.place(x=50,y=450)
                x8=tkinter.Entry(root_modification)
                x8.insert(0,f'{phone_text}')
                x8.place(x=160,y=450)
                bg_text=i[5]
                L6=Label(root_modification,text='ENTER BLOOD GROUP')
                L6.place(x=40,y=480)
                x9=tkinter.Entry(root_modification)
                x9.insert(0,f'{bg_text}')
                x9.place(x=160,y=480)
                def messagebox_modify():
                        tkinter.messagebox.showinfo('Modified Your Data','Thank You')
                b=Button(root_modification,text='Submit',command=lambda:[modification_name(),modification_age(),modification_gender(),modification_phone(),modification_blood_group(),messagebox_modify()])
                b.place(x=50,y=540)
                root_modification.resizable(False,False)
                root_modification.wm_attributes('-toolwindow','True')
                root_modification.mainloop()

        #-----------------------------------------main window for hospital-------------------------------------------------#  

        root_hospital=Toplevel(root_medical)
        root_hospital.title('Clinic')
        bg = PhotoImage(master=root_hospital,file = "images/background.png")
        label1=Label(master=root_hospital, image=bg)
        label1.place(x=750,y=300)
        photo4 = PhotoImage(master=root_hospital, file = r"images/hospital.png")
        photoimage4 = photo4.subsample(3, 3)
        label=Label(master=root_hospital,text="NAYAK CLINIC",font="arial 40 bold",bg='blue',image=photoimage4,compound=LEFT)
        photo = PhotoImage(master=root_hospital, file = r"images/registration.png")
        photoimage = photo.subsample(3, 3)
        photo1 = PhotoImage(master=root_hospital, file = r"images/appointment.png")
        photoimage1 = photo1.subsample(3, 3)
        photo2 = PhotoImage(master=root_hospital, file = r"images/doctor.png")
        photoimage2 = photo2.subsample(8, 8)
        photo3 = PhotoImage(master=root_hospital, file = r"images/sad.png")
        photoimage3 = photo3.subsample(3, 3)

        #------------------------------------------------------------------------buttons-----------------------------------------------------------------------------#

        b_registration=Button(master=root_hospital, text="Registration",font="arial 20 bold",bg='cyan',command=register,image=photoimage,compound=LEFT,cursor='hand2')
        b_appointment=Button(master=root_hospital, text="Appointment",font="arial 20 bold",bg='cyan',command=apoint,compound=LEFT,image=photoimage1,cursor='hand2')
        b_list=Button(master=root_hospital,text="List of Doctors",font="arial 20 bold",bg='cyan',command=lst_doc,compound=LEFT,image=photoimage2,cursor='hand2')
        b_services=Button(master=root_hospital,text="Services available",font='arial 20 bold',bg='cyan',command=ser_avail,cursor='hand2')
        b_modification=Button(master=root_hospital,text="Modify data",font='arial 20 bold',bg='cyan',command=mod_sub,cursor='hand2')
        b_exit=Button(master=root_hospital,text="Exit",font='arial 20 bold',command=root_hospital.destroy,bg='yellow',image=photoimage3,compound=LEFT,cursor='hand2')
        label.pack()
        b_registration.pack(side=LEFT,padx=10)
        b_hospital_registration_tooltip = CreateToolTip(b_registration, "For registration of patient")
        b_appointment.pack(side=LEFT,padx=10)
        b_hospital_appointment_tooltip = CreateToolTip(b_appointment, "For appoinment")
        b_list.pack(side=LEFT,padx=10)
        b_hospital_list_tooltip = CreateToolTip(b_list, "Doctors list")
        b_services.pack(side=LEFT,padx=10)
        b_modification.pack(side=LEFT,padx=10)
        b_exit.pack(side=LEFT,padx=10)
        b_hospital_exit_tooltip = CreateToolTip(b_exit, "press for exit!!!!")
        p = PhotoImage(file = 'images/health1.png')
        root_hospital.iconphoto(False, p)
        frame=Frame(root_hospital,height=1000,width=100)
        frame.pack()
        root_hospital.resizable(True,True)
        root_hospital.mainloop()

        #to keep it working

    b_hospital=Button(root_medical,text='hospital',font='arial 20',command=hospital)
    b_hospital.pack(side=LEFT,padx=50,pady=10)
    b_hospital_tooltip = CreateToolTip(b_hospital, "click for medical")
    root_medical.mainloop()
b_medical=Button(text='medical',command=medical)
b_medical.pack(side=LEFT,padx=10)
b_medical_tooltip = CreateToolTip(b_medical, "for clinic bills and management")
root_main.resizable(True,True)

#-------------------------------------------------------------uploading picture------------------------------------------------------------#

def profile():
    import tkinter as tk
    from tkinter import filedialog
    def upload_file():
        from PIL import ImageTk,Image
        x = openfilename()
        img = Image.open(x)
        img1=img.convert("RGB")
        img1.save('Profile/patients photo/profile_uploaded.png')
        img.resize((250,250),Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img)
        panel=Label(my_w,image=img)
        panel.image=img
        panel.grid(row=2)
        def save_file():
                with open('History/'+directory+'/'+file_name+".txt",'+a') as file:
                        file.write(D+' '+r+':\timage saved in folder proifle/patients photo,please check for verification\n')
        save_file()
    def openfilename():
        filename=filedialog.askopenfilename(title='image upload',filetypes=[('All Files','*'),('Jpg Files', '.jpg'),('Png Files','.png')])
        return filename
    my_w = Toplevel(root_main)
    my_w.geometry('400x300') # Size of the window
    my_w.title('profile')
    my_font1=('times', 18, 'bold')
    l1 = tk.Label(my_w,text='your data',width=30,font=my_font1)  
    l1.grid(row=1,column=1)
    b1 = tk.Button(my_w, text='Upload File', 
    width=20,command = upload_file)
    b1.grid(row=2,column=1)
    photo_upload=PhotoImage(file='images/upload.png')
    my_w.iconphoto(True,photo_upload)
    my_w.mainloop()
button_profile=Button(text='reference photo',font='arial 10',command=profile)
button_profile.pack(side=LEFT,padx=10)
def entertainment(*args):
    root_entertainment=Toplevel(root_main)
    root_entertainment.title('entertainment')
    entertainment_icon=PhotoImage(file='images/entertainment.png')
    root_entertainment.iconphoto(False,entertainment_icon)
    def open_entertainment():
            with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                    file.write(D+' '+r+':\topened entertainement tab\n')
    open_entertainment()
    def game():
        root_game=Toplevel(root_entertainment)
        root_game.title('games')
        game_icon=PhotoImage(file='images/game.png')
        root_game.iconphoto(False,game_icon)
        def open_games():
            with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                    file.write(D+' '+r+':\topened games tab\n')
        open_games()
        def snake_game():

                import turtle
                import time
                import random

                delay = 0.1
                score = 0

                # Score

                high_score = 0
                wn = turtle.Screen()

                # Set up the screen

                wn.title("Snake Game by Manoj v Nayak")
                wn.bgcolor("blue")
                wn.setup(width=600, height=600)
                wn.tracer(0)

                # Turns off the screen updates

                head = turtle.Turtle()

                # Snake head

                head.speed(0)
                head.shape("square")
                head.color("black")
                head.penup()
                head.goto(0,1)
                head.direction = "stop"
                food = turtle.Turtle()
                food.speed(0)

                # Snake food

                food.shape("circle")
                food.color("red")
                food.penup()
                food.goto(0,100)
                segments = []
                pen = turtle.Turtle()

                # Pen

                pen.speed(0)
                pen.shape("square")
                pen.color("white")
                pen.penup()
                pen.hideturtle()
                pen.goto(0, 260)
                pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

                # Functions

                def go_up():
                    if head.direction != "down":
                        head.direction = "up"
                def go_down():
                    if head.direction != "up":
                        head.direction = "down"
                def go_left():
                    if head.direction != "right":
                        head.direction = "left"
                def go_right():
                    if head.direction != "left":
                        head.direction = "right"
                def move():
                    if head.direction == "up":
                        y = head.ycor()
                        head.sety(y + 20)
                    if head.direction == "down":
                        y = head.ycor()
                        head.sety(y - 20)
                    if head.direction == "left":
                        x = head.xcor()
                        head.setx(x - 20)
                    if head.direction == "right":
                        x = head.xcor()
                        head.setx(x + 20)
                wn.listen()

                # Keyboard bindings

                wn.onkeypress(go_up, "8")
                wn.onkeypress(go_down, "2")
                wn.onkeypress(go_left, "4")
                wn.onkeypress(go_right, "6")
                while True:

                    # Main game loop

                    wn.update()
                    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:

                        # Check for a collision with the border

                        time.sleep(1)
                        head.goto(0,0)
                        head.direction = "stop"
                        for segment in segments:

                            # Hide the segments

                            segment.goto(1000, 1000)
                        segments.clear()

                        # Clear the segments list

                        score = 0

                        # Reset the score

                        delay = 0.1

                        # Reset the delay

                        pen.clear()
                        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
                    if head.distance(food) < 20:

                        # Check for a collision with the food

                        x = random.randint(-290, 290)

                        # Move the food to a random spot

                        y = random.randint(-290, 290)
                        food.goto(x,y)
                        new_segment = turtle.Turtle()

                        # Add a segment

                        new_segment.speed(0)
                        new_segment.shape("square")
                        new_segment.color("grey")
                        new_segment.penup()
                        segments.append(new_segment)
                        delay -= 0.001

                        # Shorten the delay

                        score += 10

                        # Increase the score

                        if score > high_score:
                            high_score = score
                        pen.clear()
                        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
                    for index in range(len(segments)-1, 0, -1):

                        # Move the end segments first in reverse order

                        x = segments[index-1].xcor()
                        y = segments[index-1].ycor()
                        segments[index].goto(x, y)
                    if len(segments) > 0:

                        # Move segment 0 to where the head is

                        x = head.xcor()
                        y = head.ycor()
                        segments[0].goto(x,y)
                    move()    
                    for segment in segments:

                        # Check for head collision with the body segments

                        if segment.distance(head) < 20:
                            time.sleep(9)
                            head.goto(0,0)
                            head.direction = "stop"
                            for segment in segments:

                                # Hide the segments

                                segment.goto(1000, 1000)
                            segments.clear()

                            # Clear the segments list

                            score = 0

                            # Reset the score

                            delay = 0.1

                            # Reset the delay

                            pen.clear()

                            # Update the score display

                            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
                    time.sleep(delay)
                    def open_snake_game():
                        with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                            file.write(D+' '+r+':\topened snake games tab\n')
                            file.write(D+' '+r+':\tscore is '+f'{score}'+f'{high_score}'+'\n')
                    open_snake_game()

            #wn.mainloop()

        #---------------------------------opening more games which is miniclip.com----------------------------------#

        def more_games():
            more_game='www.miniclip.com'
            webbrowser.open_new_tab(more_game)
            def open_more_game():
                    with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
                            file.write(D+' '+r+':\topened more games tab and went to browser and opened miniclip.com\n')
            open_more_game()
        #--------------------------------------------opened more games--------------------------------------#
        b_snake_game=Button(root_game,text='snake game',font='arial 10',command=snake_game,bg='green')
        b_snake_game.pack(side=LEFT,padx=10)
        b_snake_game_tooltip=CreateToolTip(b_snake_game,"snake game")
        b_more_games=Button(root_game,text='more games',command=more_games,font='arial 10')
        b_more_games.pack(side=LEFT,padx=10)
        b_more_games_tooltip=CreateToolTip(b_more_games,"more games")
    b_game=Button(root_entertainment,text='game',font='arial 10',command=game)
    b_game.pack(side=LEFT,padx=10)
    root_entertainment.mainloop()

#----------------------------------manual----------------------------------------#

def open_html():
    from manual import manual
    from manual import Home
    filename = 'file:///'+os.getcwd()+'/'+'manual.html'
    filename1= 'file:///'+os.getcwd()+'/'+'Home.html'
    webbrowser.open_new_tab(filename)
    webbrowser.open_new_tab(filename1)
def manual_remove():
    os.remove('manual.html')
    os.remove('news.html')
    os.remove('Home.html')

#--------------------------close of manual part and making buttons for main window-----------------------------#

b_entertainment=Button(text="Entertainment",font='arial 10',command=entertainment)
b_entertainment.pack(side=LEFT,padx=10)
b_entertainment_tooltip = CreateToolTip(b_entertainment, "for games and movies")
def quiting(*args):
    root_main.destroy()
root_main.bind('<Escape>',quiting)
def exiting():
    with open('History/'+directory+'/'+filename.strftime("%d %B %Y %H.%M.%S")+".txt",'+a') as file:
        file.write(D+' '+r+':\texited\n')
b_main=Button(text="exit",font='arial 10',bg='red',command=lambda:[root_main.destroy(),manual_remove(),exiting(),quiting()])
b_main.pack(side=LEFT,padx=10)
b_main_tooltip = CreateToolTip(b_main, "press for exit...")
photo_manual=PhotoImage(file='images/manual.png')
phoimage_manual=photo_manual.subsample(15,15)
b_manual=Button(command=open_html,relief=FLAT,image=phoimage_manual)
b_manual.place(x=10,y=20)
main_icon=PhotoImage(file='images/icon.png')
root_main.iconphoto(False,main_icon)
root_main.bind('<Control-m>',medical)
root_main.bind('<Control-e>',entertainment)
root_main.mainloop()
pyttsx3.speak("exiting.Hope you enjoyed this app.provide us the feedback via phone number or email id.we are on our way of creating our feedback tab.so please co operate with us.thank you.")
