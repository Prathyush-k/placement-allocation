from tkinter import *
from tkinter import filedialog
import numpy as np
import pandas as pd

tkin=Tk()
company_Path=[]
final={}

def func1(event):
	tkin.fileName=filedialog.askopenfilename( filetypes = (("excel files","*.xlsx"),("all files","*.*")))
	company_Path.append(tkin.fileName)
	button1.configure(fg='green')

def func2(event):
    tkin.fileName=filedialog.askopenfilename( filetypes = (("excel files","*.xlsx"),("all files","*.*")))
    company_Path.append(tkin.fileName)
    button2.configure(fg='green')

def func3(event):
    tkin.fileName=filedialog.askopenfilename( filetypes = (("excel files","*.xlsx"),("all files","*.*")))
    company_Path.append(tkin.fileName)
    button3.configure(fg='green')

def func4(event):
    tkin.fileName=filedialog.askopenfilename( filetypes = (("excel files","*.xlsx"),("all files","*.*")))
    company_Path.append(tkin.fileName)
    button4.configure(fg='green')

def func5(event):
    tkin.fileName=filedialog.askopenfilename( filetypes = (("excel files","*.xlsx"),("all files","*.*")))
    company_Path.append(tkin.fileName)
    button5.configure(fg='green')
	
def submit(event):
	print(company_Path,final)
	tkin.quit()
company_list=['Infosys','Capgemini','Cognizant']
var1=StringVar(tkin)
var1.set(company_list[0])

var2=StringVar(tkin)
var2.set(company_list[1])

var3=StringVar(tkin)
var3.set(company_list[2])

option1=OptionMenu(tkin,var1,*company_list)
option2=OptionMenu(tkin,var2,*company_list)
option3=OptionMenu(tkin,var3,*company_list)

button1=Button(tkin,text='Choose File',fg='blue')
button2=Button(tkin,text='Choose File',fg='blue')
button3=Button(tkin,text='Choose File',fg='blue')
button4=Button(tkin,text='Choose File',fg='blue')
button5=Button(tkin,text='Choose File',fg='blue')
buttons=Button(tkin,text='Submit',fg='blue')

lab1=Label(tkin,text='Master File')
lab2=Label(tkin,text='Preference File')

button1.bind("<Button-1>",func1)
button2.bind("<Button-1>",func2)
button3.bind("<Button-1>",func3)
button4.bind("<Button-1>",func4)
button5.bind("<Button-1>",func5)
buttons.bind("<Button-1>",submit)

lab1.grid(row=0)
lab2.grid(row=1)
button1.grid(row=0,column=2)
button2.grid(row=1,column=2)
button3.grid(row=2,column=2)
button4.grid(row=3,column=2)
button5.grid(row=4,column=2)
buttons.grid(row=6,column=1)
option1.grid(row=2)
option2.grid(row=3)
option3.grid(row=4)

tkin.mainloop()

# coding: utf-8

# In[1]:





# In[2]:


cap=pd.read_excel(company_Path[3])
cts=pd.read_excel(company_Path[4])
infy=pd.read_excel(company_Path[2])
preference=pd.read_excel(company_Path[1])
student_info=pd.read_excel(company_Path[0])


# In[3]:


cap.set_index(cap.columns[1],inplace=True)
cts.set_index(cts.columns[0],inplace=True)
infy.set_index(infy.columns[0],inplace=True)
preference.set_index(preference.columns[1],inplace=True)
student_info.set_index(student_info.columns[1],inplace=True)


# In[4]:


a=['Infosys','Capgemini','Cognizant']


# In[5]:


all3=[]
inf_cts=[]
cts_cap=[]
cap_inf=[]
oinf=[]
ocap=[]
octs=[]
for roll in preference.index:
        if roll in infy.index.values :
            if roll in cts.index.values:
                if roll in cap.index.values:
                    all3.append(roll)
                else:
                    inf_cts.append(roll)
        if roll in infy.index.values :
            if roll in cap.index.values:
                if roll in cts.index.values:
                    pass
                else:
                    cap_inf.append(roll)
        if roll in cap.index.values :
            if roll in cts.index.values:
                if roll in infy.index.values:
                    pass
                else:
                    cts_cap.append(roll)
        if roll in infy.index.values :
            if roll not in cts.index.values:
                if roll not in cap.index.values:
                    oinf.append(roll)
        if roll in cts.index.values :
            if roll not in infy.index.values:
                if roll not in cap.index.values:
                    octs.append(roll)
        if roll in cap.index.values :
            if roll not in cts.index.values:
                if roll not in infy.index.values:
                    ocap.append(roll)
        
print(len(all3),
len(inf_cts),
len(cts_cap),
len(cap_inf),
len(oinf),
len(ocap),
len(octs)) 


# In[6]:


Infosys=oinf
Capgemini=ocap
Cognizant=octs

for roll in all3:
    if preference.loc[roll]['Preference-1']==a[0]:
        Infosys.append(roll)
    elif preference.loc[roll]['Preference-1']==a[1]:
        Capgemini.append(roll)
    elif preference.loc[roll]['Preference-1']==a[2]:
        Cognizant.append(roll)
for roll in inf_cts:
    if preference.loc[roll]['Preference-1']==a[0]:
        Infosys.append(roll)
    elif preference.loc[roll]['Preference-1']==a[2]:
        Cognizant.append(roll)
    elif preference.loc[roll]['Preference-2']==a[0]:
        Infosys.append(roll)
    elif preference.loc[roll]['Preference-2']==a[2]:
        Cognizant.append(roll)
for roll in cts_cap:
    if preference.loc[roll]['Preference-1']==a[2]:
        Cognizant.append(roll)
    elif preference.loc[roll]['Preference-1']==a[1]:
        Capgemini.append(roll)
    elif preference.loc[roll]['Preference-2']==a[2]:
        Cognizant.append(roll)
    elif preference.loc[roll]['Preference-2']==a[1]:
        Capgemini.append(roll)
for roll in cap_inf:
    if preference.loc[roll]['Preference-1']==a[0]:
        Infosys.append(roll)
    elif preference.loc[roll]['Preference-1']==a[1]:
        Capgemini.append(roll)
    elif preference.loc[roll]['Preference-2']==a[0]:
        Infosys.append(roll)
    elif preference.loc[roll]['Preference-2']==a[1]:
        Capgemini.append(roll)
print(len(Capgemini),len(Infosys),len(Cognizant))


# In[7]:


student_info


# In[8]:


for roll in student_info.index.values:
    if type(roll)== str and '-' in roll:
        roll_split=roll.split('-')
        modified_roll=''
        for i in roll_split:
            modified_roll+=i
        modified_roll=int(modified_roll)
        student_info=student_info.rename({roll: modified_roll})


# In[9]:


columns=[
    'Full Name','Branch','Email ID','Mobile No.','BE Gpa'
]
Infosys_final=pd.DataFrame(columns=columns,index=Infosys)
for roll in Infosys_final.index:
    if roll in student_info.index:
        name=student_info.loc[roll][1]
        branch=student_info.loc[roll][2]
        email=student_info.loc[roll][2]
        mob=student_info.loc[roll][4]
        gpa=student_info.loc[roll][8]
        Infosys_final.loc[roll]=[name,branch,email,mob,gpa]
Cognizant_final=pd.DataFrame(columns=columns,index=Cognizant)
for roll in Cognizant_final.index:
    if roll in student_info.index:
        name=student_info.loc[roll][1]
        branch=student_info.loc[roll][2]
        email=student_info.loc[roll][2]
        mob=student_info.loc[roll][4]
        gpa=student_info.loc[roll][8]
        Cognizant_final.loc[roll]=[name,branch,email,mob,gpa]
Capgemini_final=pd.DataFrame(columns=columns,index=Capgemini)
for roll in Capgemini_final.index:
    if roll in student_info.index:
        name=student_info.loc[roll][1]
        branch=student_info.loc[roll][2]
        email=student_info.loc[roll][2]
        mob=student_info.loc[roll][4]
        gpa=student_info.loc[roll][8]
        Capgemini_final.loc[roll]=[name,branch,email,mob,gpa]


# In[10]:


#company wise xlsx files..
#Capgemini_final.to_excel()
#Infosys_final.to_excel()
#Cognizant_final.to_excel() 


# In[11]:


inf_add=[]
cap_add=[]
cog_add=[]
for i in Infosys_final.index:
    inf_add.append("Infosys")
for i in Capgemini_final.index:
    cap_add.append("Capgemini")
for i in Cognizant_final.index:
    cog_add.append("Cognizant")


# In[12]:


Infosys_f=Infosys_final
Capgemini_f=Capgemini_final
Cognizant_f=Cognizant_final
Infosys_f['Company']=pd.Series(inf_add,index=Infosys_f.index)
Capgemini_f['Company']=pd.Series(cap_add,index=Capgemini_f.index)
Cognizant_f['Company']=pd.Series(cog_add,index=Cognizant_f.index)
Placed_student_list=pd.DataFrame()
Placed_student_list=Placed_student_list.append(Infosys_f)
Placed_student_list=Placed_student_list.append(Capgemini_f)
Placed_student_list=Placed_student_list.append(Cognizant_f)


# In[13]:


#Placed Students list...
Placed_student_list.to_csv("placement_final.csv")

