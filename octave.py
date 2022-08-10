from multiprocessing.sharedctypes import Value
from tkinter import *
import tkinter as tk
from turtle import width
from openpyxl import Workbook,load_workbook

##clear all entries after submission#############
def clear():
    first_name_input.delete(0,'end')
    last_name_input.delete(0,'end')
    faculty_input.delete(0,'end')
    degree_input.delete(0,'end')
    pref_por_name_input.delete(0,'end')
    comments_input.delete(0,'end')
    


#functions
def Saver_1():
    
    induction_days=3
    applicant_seats=20

    a = honesty_variable.get()
    b = curiosity_variable.get()
    c = culture_fit_variable.get()
    d = Experience_Variable.get()
    e = adaptive_Variable.get()
    f = self_motivated_Variable.get()
    g = collaborative_variable.get()
    h = growth_variable.get()

    z = e1.get().upper()
    x = e2.get().upper()
    l = e3.get().upper()
    v = e4.get().upper()
    m = e5.get().upper()
    c1 = comment.get().upper()

    credibilty = ((a+b+c+d+e+f+g+h))/(applicant_seats)*(induction_days)
    credibilty = credibilty.__round__(3) #to round values to 3 sf
    #also look into the save button, it needs to be destroyed after first click and then update button would appear
    #below code works
    # print(a,d,b,c,d,e,f,h,z,x,l,v,m,c1,credibilty)

    data = [z,x,l,v,m,c1,a,b,c,d,e,f,g,h,credibilty]
    
    wb = load_workbook("Candidates.xlsx") # creates a workbook object.
    ws = wb.active # creates a worksheet object.
    ws.append(data)
    wb.save(filename="Candidates.xlsx")
    clear()



root = Tk()
root.title('OCTAVE') #changing name
root.iconphoto(False,tk.PhotoImage(file='logo.png')) #adding logo
root.resizable(False,False)

'''widgets are added here'''
Label(root, text='First Name',font="Sans",padx=10).grid(row=0,column=0,pady=15)
Label(root, text='Last Name',font="Sans",padx=10).grid(row=1,column=0,pady=15)
Label(root, text='Faculty',font="Sans",padx=10).grid(row=2,column=0,pady=15)
Label(root, text='Degree',font="Sans",padx=10).grid(row=3,column=0,pady=15)
Label(root, text='Preferred Portolio',font="Sans",padx=10).grid(row=4,column=0,pady=15)
Label(root, text='Comments',font='Sans',padx=10).grid(row=5,column=0,pady=15)

##INPUTS############################################
e1 = StringVar(root)
e2 = StringVar(root)
e3 = StringVar(root)
e4 = StringVar(root)
e5 = StringVar(root)
comment = StringVar(root)

first_name_input = Entry(root,textvariable=e1,width=25,font="Sans",borderwidth=3)
last_name_input = Entry(root,textvariable=e2,width=25,font="Sans",borderwidth=3)
faculty_input = Entry(root,textvariable=e3,width=25,font="Sans",borderwidth=3)
degree_input = Entry(root,textvariable=e4,width=25,font="Sans",borderwidth=3)
pref_por_name_input = Entry(root,textvariable=e5,width=25,font="Sans",borderwidth=3)
comments_input = Entry(root,textvariable=comment,width=25,font="Sans",borderwidth=3)

first_name_input.grid(row=0,column=1)
last_name_input.grid(row=1,column=1)
faculty_input.grid(row=2,column=1)
degree_input.grid(row=3,column=1)
pref_por_name_input.grid(row=4,column=1)
comments_input.grid(row=5,column=1)


##Radio Buttons###################################
"""lists of ratings here"""
honesty_variable = IntVar(root) #a #mapping to letters for function saver_1
curiosity_variable = IntVar(root) #b
culture_fit_variable = IntVar(root) #c
Experience_Variable = IntVar(root) #d
adaptive_Variable = IntVar(root) #e
self_motivated_Variable = IntVar(root) #f
collaborative_variable = IntVar(root) #g
growth_variable = IntVar(root) #h'''

#honesty button
Label(root,text='Honesty',font="Sans",borderwidth=3,padx=10,justify='right').grid(row=0,column=3,pady=20)
Radiobutton(root,text='0',value=0,variable=honesty_variable).grid(row=0,column=4)
Radiobutton(root,text='1',value=1,variable=honesty_variable).grid(row=0,column=5)
Radiobutton(root,text='2',value=2,variable=honesty_variable).grid(row=0,column=6)
Radiobutton(root,text='3',value=3,variable=honesty_variable).grid(row=0,column=7)
Radiobutton(root,text='4',value=4,variable=honesty_variable).grid(row=0,column=8)
Radiobutton(root,text='5',value=5,variable=honesty_variable).grid(row=0,column=9)

#curiosity button
Label(root,text='Curiosity',font="Sans",borderwidth=3,padx=10).grid(row=1,column=3,pady=20)
Radiobutton(root,text='0',value=0,variable=curiosity_variable).grid(row=1,column=4)
Radiobutton(root,text='1',value=1,variable = curiosity_variable).grid(row=1,column=5)
Radiobutton(root,text='2',value=2,variable = curiosity_variable).grid(row=1,column=6)
Radiobutton(root,text='3',value=3,variable = curiosity_variable).grid(row=1,column=7)
Radiobutton(root,text='4',value=4,variable = curiosity_variable).grid(row=1,column=8)
Radiobutton(root,text='5',value=5,variable = curiosity_variable).grid(row=1,column=9)

#Culture-Fit button
Label(root,text='Culture-Fit',font="Sans",borderwidth=3,padx=10).grid(row=2,column=3,pady=20)
Radiobutton(root,text='0',variable=culture_fit_variable,value=0).grid(row=2,column=4)
Radiobutton(root,text='1',variable=culture_fit_variable,value=1).grid(row=2,column=5)
Radiobutton(root,text='2',variable=culture_fit_variable,value=2).grid(row=2,column=6)
Radiobutton(root,text='3',variable=culture_fit_variable,value=3).grid(row=2,column=7)
Radiobutton(root,text='4',variable=culture_fit_variable,value=4).grid(row=2,column=8)
Radiobutton(root,text='5',variable=culture_fit_variable,value=5).grid(row=2,column=9)

#Experience button
Label(root,text='Experience',font="Sans",borderwidth=3,padx=10).grid(row=3,column=3,pady=20)
Radiobutton(root,text='0',value=0,variable=Experience_Variable).grid(row=3,column=4)
Radiobutton(root,text='1',value=1,variable=Experience_Variable).grid(row=3,column=5)
Radiobutton(root,text='2',value=2,variable=Experience_Variable).grid(row=3,column=6)
Radiobutton(root,text='3',value=3,variable=Experience_Variable).grid(row=3,column=7)
Radiobutton(root,text='4',value=4,variable=Experience_Variable).grid(row=3,column=8)
Radiobutton(root,text='5',value=5,variable=Experience_Variable).grid(row=3,column=9)

#adaptive button
Label(root,text='Adaptiveness',font="Sans",borderwidth=3,padx=10).grid(row=4,column=3,pady=20)
Radiobutton(root,text='0',value=0,variable = adaptive_Variable).grid(row=4,column=4)
Radiobutton(root,text='1',value=1,variable = adaptive_Variable).grid(row=4,column=5)
Radiobutton(root,text='2',value=2,variable = adaptive_Variable).grid(row=4,column=6)
Radiobutton(root,text='3',value=3,variable = adaptive_Variable).grid(row=4,column=7)
Radiobutton(root,text='4',value=4,variable = adaptive_Variable).grid(row=4,column=8)
Radiobutton(root,text='5',value=5,variable = adaptive_Variable).grid(row=4,column=9)

#self-motivated button
Label(root,text='Self-Motivation',font="Sans",borderwidth=3,padx=10).grid(row=5,column=3,pady=20)
Radiobutton(root,text='0',value=0,variable=self_motivated_Variable).grid(row=5,column=4)
Radiobutton(root,text='1',value=1,variable=self_motivated_Variable).grid(row=5,column=5)
Radiobutton(root,text='2',value=2,variable=self_motivated_Variable).grid(row=5,column=6)
Radiobutton(root,text='3',value=3,variable=self_motivated_Variable).grid(row=5,column=7)
Radiobutton(root,text='4',value=4,variable=self_motivated_Variable).grid(row=5,column=8)
Radiobutton(root,text='5',value=5,variable=self_motivated_Variable).grid(row=5,column=9)

#collaboration button
Label(root,text='Collaborative',font="Sans",borderwidth=3,padx=10).grid(row=6,column=3,pady=20)
Radiobutton(root,text='0',value=0,variable=collaborative_variable).grid(row=6,column=4)
Radiobutton(root,text='1',value=1,variable=collaborative_variable).grid(row=6,column=5)
Radiobutton(root,text='2',value=2,variable=collaborative_variable).grid(row=6,column=6)
Radiobutton(root,text='3',value=3,variable=collaborative_variable).grid(row=6,column=7)
Radiobutton(root,text='4',value=4,variable=collaborative_variable).grid(row=6,column=8)
Radiobutton(root,text='5',value=5,variable=collaborative_variable).grid(row=6,column=9)

#growth button
Label(root,text='Growth-Mindset',font="Sans",borderwidth=3,padx=10).grid(row=7,column=3,pady=20)
Radiobutton(root,text='0',value=0,variable=growth_variable).grid(row=7,column=4)
Radiobutton(root,text='1',value=1,variable=growth_variable).grid(row=7,column=5)
Radiobutton(root,text='2',value=2,variable=growth_variable).grid(row=7,column=6)
Radiobutton(root,text='3',value=3,variable=growth_variable).grid(row=7,column=7)
Radiobutton(root,text='4',value=4,variable=growth_variable).grid(row=7,column=8)
Radiobutton(root,text='5',value=5,variable=growth_variable).grid(row=7,column=9)




normal_button_1 = Button(root,text='Submit',borderwidth=3,command=Saver_1,font="Sans",bg='grey',fg='black').grid(sticky='SW')


root.geometry("800x800")
root.mainloop()