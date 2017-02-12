# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:57:31 2017

@author: a1849
"""
import numpy as np
def processLALAlgo(seq):
    countone=1
    tmpresult=""
    loopcounter=0
    result=""
    lasti=""
    #print ("process",len(seq))
    strarr = list(seq)
    for i  in strarr:        
        if lasti==i and len(seq)==(loopcounter+1):
            countone = countone +1
            result = tmpresult + str(countone)+i
        elif lasti==i:
            countone = countone +1
            result = tmpresult +str(countone)+i            
        else:
            if len(seq)==1:
                 result = tmpresult +str(countone)+i
            else:
                countone = 1
                tmpresult = result
                result = tmpresult +str(countone)+i
                #print("inner result ",result)
                lasti = i
        loopcounter = loopcounter +1
            
    return result




if __name__ =='__main__':
    print ("Look and see Algo....")
    result="1"

    #a=a+a
    print("anser",result)
    for i in range(19):        
        result = processLALAlgo(result)
        print("anser",result)
       

