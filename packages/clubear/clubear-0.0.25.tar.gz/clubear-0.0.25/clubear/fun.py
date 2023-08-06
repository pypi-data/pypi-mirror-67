import pandas as pd
import numpy as np
import os

        
def ispump(pp):
    '''is pump is used to check whether the input is a pump'''

    try:
        df=pp.go()
    except:
        return False
    if not isinstance(df, pd.DataFrame): return False
    if df.shape[0]==0: return False
    
    return True

def demo():
    '''demo is used to demonstrate the whole clubear class'''
    
    mylist=['manager','pump','check','plot','model','tank']
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

def auc(x,y):
    '''auc is used to computed auc for x and binary y'''
    
    if not isinstance(x,list): print('auc: the input x should be a list.'); return
    if not isinstance(y,list): print('auc: the input y should be a list.'); return
    if len(x)!=len(y): print('auc: the input x and y should have same length.'); return
    
    pos=np.argsort(x)
    x=[x[each] for each in pos]
    y=[y[each] for each in pos]
    
    ss=len(y);positive=np.sum(y);negative=ss-positive
    totalwin=0;losers=0
    for i in range(ss): 
        if y[i]==0: losers=losers+1
        if y[i]==1: totalwin=totalwin+losers
    auc=totalwin/(positive*negative)
    return auc

