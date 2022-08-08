import pandas as pd
from pandas import *

def Saver_1():

    induction_days=3
    applicant_seats=20
    formula_value = ((a+b+c+d+e+f+g+h))/(applicant_seats)*(induction_days)
    #also look into the save button, it needs to be destroyed after first click and then update button would appear
    
    data = {'First Name':z,'Last Name':x,'Faculty':l,'Degree':v,'Preferred Portfolio':m,'Honesty':a,'Experience':d,'Collaboration':g,'Culture-Fit':c,'Curiosity':b,'Adaptiveness':e,'Self-Motivated':f,'Growth':h,'Credibility Score':formula_value,'Comments':c1}
    df = pd.DataFrame(data, index = [0])
    df.to_excel('Candidates.xlsx',index=False)

#2 issues remain
#entry and radio button data not storing to excel
#update if excel file exists
