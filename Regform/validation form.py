from tkinter import * 
from tkinter.ttk import * 
from tkcalendar import Calendar, DateEntry 
# For connenction on mysql database in python 
import pymysql 
import tkinter.messagebox as tm 
# For regular expression 
import re 
# For processing date and time variable 
from datetime import datetime 
 
# Saving student form data 
def saveStudent(): 
     
    # Checking last input for validating , if not validated , shows error message 
    if (len(landline.get()) == 8 and landline.get().isdigit()) == False: 
        tm.showinfo("Save" , "Not Validated!") 
        return 
     
    try: 
        # processing for three date variables : Birth Date , Start Date , End Date 
        birthDateObj = datetime.strptime(yearBirth.get() + "-" + monthBirth.get() + "-" + dayBirth.get(), '%Y-%m-%d') 
        startDateObj = datetime.strptime(startDate.get(), '%d/%m/%Y') 
        endDateObj = datetime.strptime(endDate.get(), '%d/%m/%Y') 
        conn = pymysql.connect(user="root", password="", host="localhost", database="studentdata") 
        cur = conn.cursor() 
        # Excuting insert query  
        cur.execute("""insert into details(RegistrationNumber,name,address, email,mobileno,landlineno,dob,startdate,enddate,gender) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" , (reg_number.get(),cand_name.get(),address.get(),email.get(),mobile.get(),landline.get(), birthDateObj.strftime("%Y-%m-%d"),startDateObj.strftime("%Y-%m-%d"),endDateObj.strftime("%Y-%m-%d"),genderValue.get())) 
        conn.close() 
        # Show message for successing 
        tm.showinfo("Save" , "Success!") 
        # Initializing for each input. 
        candNameEntry.config(state='disabled') 
        addressEntry.config(state='disabled') 
        emailEntry.config(state='disabled') 
        mobileEntry.config(state='disabled') 
        landlineEntry.config(state='disabled') 
    except Exception as e: 
        print(e) 
        # If error on saving , shows error message. 
        tm.showerror("Save" ,"Failed to save!") 
# When clicking cancel button , application will be closed. 
def cancel(): 
    
    reg_number.set("") 
    cand_name.set("") 
    address.set("")  
    email.set("") 
    mobile.set("") 
    landline.set("") 
 
    yearBirth.set("2019") 
    monthBirth.set("1") 
    dayBirth.set("1") 
    root.quit() 
# Checking if email is correct format 
def is_valid_email(email): 
    if email.replace('.', '', 1).isdigit():
        return True
    else:
        return False
        
    '''
    if len(email) > 7: 
        return bool(re.match("[-+]?([0-5]*\. [0-5]+|[0-5]+)", email)) 
    return False''' 
# Validating for each input 
def validate(event , input): 
    if( input == "Registration number"):
        
        reg_num = reg_number.get() 
        if (len(reg_num) < 5 or len(reg_num) > 30): 
            tm.showerror("Invalidate!" ,"Registration number has to alphanumeric  having length between 5 and 20.") 
            regNumEntry.focus_set() 
        else: 
            candNameEntry.focus_set() 
            candNameEntry.config(state='normal') 
    elif( input == "Candidate name"): 
        if all(x.isalpha() or x.isspace() for x in cand_name.get()) and (len(cand_name.get()) > 0):
            addressEntry.focus_set() 
            addressEntry.config(state='normal') 
        else: 
            tm.showerror("Invalidate!" ,"Candidate name cannot contain digits or special characters . Spaces are allowed. ") 
            candNameEntry.focus_set() 
    elif( input == "address"): 
        if address.get().isalnum():
            
            emailEntry.focus_set() 
            emailEntry.config(state='normal') 
        else: 
            tm.showerror("Invalidate!" ,"Address: alphanumeric. ") 
            addressEntry.focus_set() 
    elif( input == "email"): 
        if is_valid_email(email.get()): 
            mobileEntry.focus_set() 
            mobileEntry.config(state='normal') 
        else: 
            tm.showerror("Invalidate!" ,"Incorrect email formats. ") 
            emailEntry.focus_set() 
    elif( input == "mobile"): 
        if len(mobile.get()) == 10 and mobile.get().isdigit(): 
            landlineEntry.focus_set() 
            landlineEntry.config(state='normal') 
        else: 
            tm.showerror("Invalidate!" ,"Mobile number: digits only,strictly 10 digits. ") 
            mobileEntry.focus_set()   
    elif( input == "landline"): 
        if len(landline.get()) == 8 and landline.get().isdigit(): 
            birthFrame.focus_set() 
        else: 
            tm.showerror("Invalidate!" ,"Landline number: digits only. Strictly 8 digits. ") 
            landlineEntry.focus_set()     
 
# Creating main window and setting with width and height             
root = Tk() 
root.title("Student Data") 
root.geometry('{}x{}'.format(600, 500)) 
mainframe = Frame(root) 
mainframe.pack() 
 
# Setting string variable for 6 input 
reg_number = StringVar() 
cand_name = StringVar() 
address = StringVar() 
email = StringVar() 
mobile = StringVar() 
landline = StringVar() 
# Input for Registration number 
regNumEntry = Entry(mainframe, width=20, textvariable=reg_number) 
regNumEntry.grid(row=0, column=1 ,padx=5, pady=5) 
regNumEntry.bind("<Return>", lambda event: validate(event, "Registration number")) 
regNumEntry.bind("<Tab>", lambda event: validate(event, "Registration number")) 

candNameEntry = Entry(mainframe, width=20, textvariable=cand_name) 
candNameEntry.grid(row=1, column=1 ,padx=5, pady=5) 
candNameEntry.bind("<Return>", lambda event: validate(event, "Candidate name")) 
candNameEntry.bind("<Tab>", lambda event: validate(event, "Candidate name")) 
# Input for address 
addressEntry = Entry(mainframe, width=20, textvariable=address) 
addressEntry.grid(row=2, column=1 ,padx=5, pady=5) 
addressEntry.bind("<Return>", lambda event: validate(event, "address")) 
addressEntry.bind("<Tab>", lambda event: validate(event, "address")) 
# Input for email 
emailEntry = Entry(mainframe, width=20, textvariable=email) 
emailEntry.grid(row=3, column=1 ,padx=5, pady=5) 
emailEntry.bind("<Return>", lambda event: validate(event, "email")) 
emailEntry.bind("<Tab>", lambda event: validate(event, "email")) 
# Input for mobile 
mobileEntry = Entry(mainframe, width=20, textvariable=mobile) 
mobileEntry.grid(row=4, column=1 ,padx=5, pady=5) 
mobileEntry.bind("<Return>", lambda event: validate(event, "mobile")) 
mobileEntry.bind("<Tab>", lambda event: validate(event, "mobile")) 
# Input for landline 
landlineEntry = Entry(mainframe, width=20, textvariable=landline) 
landlineEntry.grid(row=5, column=1 ,padx=5, pady=5) 
landlineEntry.bind("<Return>", lambda event: validate(event, "landline")) 
landlineEntry.bind("<Tab>", lambda event: validate(event, "landline")) 
candNameEntry.config(state='disabled') 
addressEntry.config(state='disabled') 
emailEntry.config(state='disabled') 
mobileEntry.config(state='disabled') 
landlineEntry.config(state='disabled') 
 
# Three combobox for birth date 
birthFrame = Frame(mainframe) 
yearBirth = StringVar() 
choices = list(range(1950,2020)) 
Combobox(birthFrame , width=5, values = choices ,textvariable = yearBirth  ).grid(row=0, column=1, padx=5, pady=5) 
monthBirth = StringVar() 
choices = list(range(1,13)) 
Combobox(birthFrame , width=5, values = choices ,textvariable = monthBirth  ).grid(row=0, column=2, padx=5, pady=5) 
dayBirth = StringVar() 
choices = list(range(1,32)) 
Combobox(birthFrame , width=5, values = choices ,textvariable = dayBirth  ).grid(row=0, column=3, padx=5, pady=5) 
birthFrame.grid(row=6, column=1, padx=5, pady=5) 
# Birth Date initializing as 2019-1-1 
yearBirth.set("2019") 
monthBirth.set("1") 
dayBirth.set("1") 
# Date picker for start date ,  end date 
startDate = StringVar() 
endDate = StringVar() 
DateEntry(mainframe , textvariable = startDate , date_pattern='dd/mm/y' ).grid(row=7, column=1, padx=5, pady=5) 
DateEntry(mainframe , textvariable = endDate , date_pattern='dd/mm/y' ).grid(row=8, column=1, padx=5, pady=5) 
# Radio option for selecting gender , as default , Male 
genderValue = StringVar() 
genderFrame = Frame(mainframe) 
Radiobutton(genderFrame, text="Male" ,variable=genderValue, value="Male"  ).grid(row=0, column=1, padx=5, pady=5) 
Radiobutton(genderFrame, text="Female" ,variable=genderValue, value="Female").grid(row=0, column=2, padx=5, pady=5) 
genderFrame.grid(row=9, column=1, padx=5, pady=5) 
genderValue.set("Male") 
 
# Setting labels for each input 
Label(mainframe, text='Registration Number:*', anchor='w').grid(row=0, column=0 ,padx=5, pady=5, sticky="w") 
Label(mainframe, text='Candidate Name:*', anchor='w').grid(row=1, column=0 ,padx=5, pady=5, sticky="w") 
Label(mainframe, text='Address:*', anchor='w').grid(row=2, column=0 ,padx=5, pady=5, sticky="w") 
Label(mainframe, text='Email:*', anchor='w').grid(row=3, column=0 ,padx=5, pady=5, sticky="w") 
Label(mainframe, text='Mobile Number:', anchor='w').grid(row=4, column=0 ,padx=5, pady=5, sticky="w") 
Label(mainframe, text='Landline Number:', anchor='w').grid(row=5, column=0 ,padx=5, pady=5, sticky="w") 
 
Label(mainframe, text='Date of Birth:', anchor='w').grid(row=6, column=0 ,padx=5, pady=5, sticky="w") 
Label(mainframe, text='Start Date:*', anchor='w').grid(row=7, column=0 ,padx=5, pady=5, sticky="w") 
Label(mainframe, text='End Date:*', anchor='w').grid(row=8, column=0 ,padx=5, pady=5, sticky="w") 
Label(mainframe, text='Gender:*', anchor='w').grid(row=9, column=0 ,padx=5, pady=5, sticky="w") 
# Buttons for submit and cancel  
btnFrame = Frame(mainframe) 
Button(btnFrame, text="Submit", command=saveStudent).grid(row=0, column=1, padx=5, pady=5) 
Button(btnFrame, text="Cancel", command=cancel).grid(row=0, column=2, padx=5, pady=5) 
btnFrame.grid(row=10, column=1, padx=5, pady=5) 
root.mainloop() 