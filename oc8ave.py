from tkinter import *
import tkinter as tk
import pandas as pd
from saver_function import Saver_1

#functions
def Saver_1():
    
    induction_days=3
    applicant_seats=20
    a = honesty_variable.get()
    d = Experience_Variable.get()
    g = collaborative_variable.get()
    c = culture_fit_variable.get()
    b = curiosity_variable.get()
    e = adaptive_Variable.get()
    f = self_motivated_Variable.get()
    h = growth_variable.get()
    z = e1.get()
    x = e2.get()
    l = e3.get()
    v = e4.get()
    m = e5.get()
    c1 = comment.get()

    formula_value = ((a+b+c+d+e+f+g+h))/(applicant_seats)*(induction_days)
    formula_value = formula_value.__round__(3) #to round values to 3 sf
    #also look into the save button, it needs to be destroyed after first click and then update button would appear
    #below code works
    data = {'First Name':z,'Last Name':x,'Faculty':l,'Degree':v,'Preferred Portfolio':m,'Honesty':a,'Experience':d,'Collaboration':g,'Culture-Fit':c,'Curiosity':b,'Adaptiveness':e,'Self-Motivated':f,'Growth':h,'Credibility Score':formula_value,'Comments':c1}
    df = pd.DataFrame(data, index = [0])
    df.to_excel('Candidates.xlsx',index=False)













main_window = tk.Tk()

main_window.title('OCTAVE') #changing name

main_window.iconphoto(False,tk.PhotoImage(file='C:/Users/LENOVO/Desktop/OCTAVE/logo.png')) #adding logo
main_window.resizable(False,False)

w = tk.Canvas(main_window,width=1080,height=900,borderwidth=0) #making window
w.grid() #needs to be added as it messes shit up

'''widgets are added here'''
Label(w, text='First Name',font="Sans",padx=10).grid(row=0,column=0,pady=15)
Label(w, text='Last Name',font="Sans",padx=10).grid(row=1,column=0,pady=15)
Label(w, text='Faculty',font="Sans",padx=10).grid(row=2,column=0,pady=15)
Label(w, text='Degree',font="Sans",padx=10).grid(row=3,column=0,pady=15)
Label(w, text='Preferred Portolio',font="Sans",padx=10).grid(row=4,column=0,pady=15)
Label(w, text='Comments',font='Sans',padx=10).grid(row=5,column=0,pady=15)

e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
comment = StringVar()

e1_entry = Entry(w,textvariable=e1,width=25,font="Sans",borderwidth=3)
e2_entry = Entry(w,textvariable=e2,width=25,font="Sans",borderwidth=3)
e3_entry = Entry(w,textvariable=e3,width=25,font="Sans",borderwidth=3)
e4_entry = Entry(w,textvariable=e4,width=25,font="Sans",borderwidth=3)
e5_entry = Entry(w,textvariable=e5,width=25,font="Sans",borderwidth=3)
comment_entry = Entry(w,textvariable=comment,width=25,font='Sans',borderwidth=3)

e1_entry.grid(row=0,column=1)
e2_entry.grid(row=1,column=1)
e3_entry.grid(row=2,column=1)
e4_entry.grid(row=3,column=1)
e5_entry.grid(row=4,column=1)
comment_entry.grid(row=5,column=1)

"""lists of ratings here"""
honesty_variable = IntVar(w) #a #mapping to letters for function saver_1
honesty_variable.trace_add("write",Saver_1)
curiosity_variable = IntVar(w) #b
curiosity_variable.trace_add("write",Saver_1)
culture_fit_variable = IntVar(w) #c
culture_fit_variable.trace_add("write",Saver_1)
Experience_Variable = IntVar(w) #d
Experience_Variable.trace_add("write",Saver_1)
adaptive_Variable = IntVar(w) #e
adaptive_Variable.trace_add('write',Saver_1)
self_motivated_Variable = IntVar(w) #f
self_motivated_Variable.trace_add('write',Saver_1)
collaborative_variable = IntVar(w) #g
collaborative_variable.trace_add('write',Saver_1)
growth_variable = IntVar(w) #h'''
growth_variable.trace_add('write',Saver_1)

#honesty button
Label(w,text='Honesty',font="Sans",borderwidth=3,padx=10,justify='right').grid(row=0,column=3,pady=20)
Radiobutton(w,text='0',value=0,variable=honesty_variable).grid(row=0,column=4)
Radiobutton(w,text='1',value=1,variable=honesty_variable).grid(row=0,column=5)

#curiosity button
Label(w,text='Curiosity',font="Sans",borderwidth=3,padx=10).grid(row=1,column=3,pady=20)
Radiobutton(w,text='0',value=0,variable=curiosity_variable).grid(row=1,column=4)
Radiobutton(w,text='1',value=1,variable = curiosity_variable).grid(row=1,column=5)

#Culture-Fit button
Label(w,text='Culture-Fit',font="Sans",borderwidth=3,padx=10).grid(row=2,column=3,pady=20)
Radiobutton(w,text='0',value=0,variable=culture_fit_variable).grid(row=2,column=4)
Radiobutton(w,text='1',variable=culture_fit_variable,value=1).grid(row=2,column=5)

#Experience button
Label(w,text='Experience',font="Sans",borderwidth=3,padx=10).grid(row=3,column=3,pady=20)
Radiobutton(w,text='0',value=0,variable=Experience_Variable).grid(row=3,column=4)
Radiobutton(w,text='1',value=1,variable=Experience_Variable).grid(row=3,column=5)
Radiobutton(w,text='2',value=2,variable=Experience_Variable).grid(row=3,column=6)

#adaptive button
Label(w,text='Adaptiveness',font="Sans",borderwidth=3,padx=10).grid(row=4,column=3,pady=20)
Radiobutton(w,text='0',value=0,variable = adaptive_Variable).grid(row=4,column=4)
Radiobutton(w,text='1',value=1,variable = adaptive_Variable).grid(row=4,column=5)

#self-motivated button
Label(w,text='Self-Motivation',font="Sans",borderwidth=3,padx=10).grid(row=5,column=3,pady=20)
Radiobutton(w,text='0',value=0,variable=self_motivated_Variable).grid(row=5,column=4)
Radiobutton(w,text='1',value=1,variable=self_motivated_Variable).grid(row=5,column=5)
Radiobutton(w,text='2',value=2,variable=self_motivated_Variable).grid(row=5,column=6)

#collaboration button
Label(w,text='Collaborative',font="Sans",borderwidth=3,padx=10).grid(row=6,column=3,pady=20)
Radiobutton(w,text='0',value=0,variable=collaborative_variable).grid(row=6,column=4)
Radiobutton(w,text='1',value=1,variable=collaborative_variable).grid(row=6,column=5)
Radiobutton(w,text='2',value=2,variable=collaborative_variable).grid(row=6,column=6)

#growth button
Label(w,text='Growth-Mindset',font="Sans",borderwidth=3,padx=10).grid(row=7,column=3,pady=20)
Radiobutton(w,text='0',value=0,variable=growth_variable).grid(row=7,column=4)
Radiobutton(w,text='1',value=1,variable=growth_variable).grid(row=7,column=5)

entry_dict = {'entry1':e1,'entry2':e2,'entry3':e3,'entry4':e4,'entry5':e5,'comments':comment} #to be used in function
dictionary_variables = {'honesty':honesty_variable,'curiosity':curiosity_variable,'culture-fit':culture_fit_variable,'Experience':Experience_Variable,'Adaptive':adaptive_Variable,'self-motivated':self_motivated_Variable,'collaboration':collaborative_variable,'growth':growth_variable}

#button to save data
normal_button_1 = Button(w,text='Submit',borderwidth=3,command=Saver_1(),font="Sans",bg='grey',fg='black').grid(sticky='SW')




main_window.mainloop()