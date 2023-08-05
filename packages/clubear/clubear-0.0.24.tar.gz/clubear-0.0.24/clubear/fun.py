import pandas as pd
import numpy as np
import os

'''add dumy variable'''
def ady(df,varname,levels):
    '''ady is used to add dumy varialbes for varname according to levels.'''
    
    ncov=len(levels)
    strlevels=[str(each) for each in levels]
    strvalues=[str(each) for each in df[varname]]
    newname=[varname+'.'+str(each) for each in levels]
    for j in range(ncov): 
        dummys=[1.0*(each==strlevels[j]) for each in strvalues]
        df[newname[j]]=dummys
        
def ispump(pp):
    '''is pump is used to check whether the input is a pump'''
    
    out='YES'
    try:
        df=pp.go()
    except:
        return("ispump: The input pump is NOT a pump and has no GO!")
    if not isinstance(df, pd.DataFrame): return('ispump: The pump RUN output is not a DataFrame!')
    
    return out

def demo():
    '''demo is used to demonstrate the whole clubear class'''
    
    mylist=['manager','pump','check','plot','model']
    mylist=sorted(mylist)
    
    greeting='''
Welcome to CluBear!

This is a package designed for *Interactive* statistical analysis for massive 
datasets. The key idea used here is subsampling. The package is developed by 
CluBear Research Group. You are welcome to visit our official website at 
www.xiong99.com.cn. You are also welcome to follow us at our official WeChat 
account (ID: CluBear). Enjoy!
'''
    print(greeting)
    print('\n',mylist,'\n')
    
    return

