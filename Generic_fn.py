
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from xlrd import open_workbook


# In[2]:


file = [] 

stud = open_workbook('C:/IT project/Students.xlsx', 'rb')
sheets0 = stud.sheet_names()
pref = open_workbook('C:/IT project/Preferences.xlsx', 'rb')
sheets1 = pref.sheet_names()
inf = open_workbook('C:/IT project/Infosys.xlsx', 'rb')
sheets2 = inf.sheet_names()
cts = open_workbook('C:/IT project/CTS.xlsx', 'rb')
sheets3 = cts.sheet_names()
cap = open_workbook('C:/IT project/Capgemini.xlsx', 'rb')
sheets4 = cap.sheet_names()

sheets2


# In[3]:


def func(stud, sheet, row):
    data = []
    df = pd.DataFrame()
#     x = 1
#     for sheet_name in sheet:
#         if x == 2:
#             pass
#         else:
#             ++x
    print (sheet)
    sh = stud.sheet_by_name(sheet[0])
    for rownum in range(sh.nrows):
        row_values = sh.row_values(rownum)
        dat =[]
        for i in range(0,len(row)):
            dat.append((row_values[row[i]]))
        data.append(dat) 
        df = pd.DataFrame(data)
        df.drop(df.index[0], axis = 0, inplace = True)

                
    return df


# In[6]:


# df_stud = pd.DataFrame()
# df_stud = pd.DataFrame(func(stud, sheets0, (1,2,3,4,5)))

# df_pref = pd.DataFrame()
# df_pref = pd.DataFrame(func(pref, sheets1, (1,3,4,5)))

df_inf = pd.DataFrame()
df_inf = pd.DataFrame(func(inf, sheets2, (0,1,2)))

df_cts = pd.DataFrame()
df_cts = pd.DataFrame(func(cts, sheets3, (0,1,2)))

df_cap = pd.DataFrame()
df_cap = pd.DataFrame(func(cap, sheets3, (0,1,2)))


df_cts


# In[ ]:


if pref[]

