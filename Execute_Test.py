# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 08:34:22 2021

@author: KIT
"""

import shutil
import os
import sys


#A = 0
#B = 0
#SUM = 0

def Execute_Test():
    #Insert code of Execute Test here
    A = Set_A(1)
    B = Set_B(2
    SUM = SUM_A_B(A, B)

    
    if os.path.exists("result.txt"):
        os.remove("result.txt")
        f = open("result.txt", "w")
        f.close()
    else:
        f = open("result.txt", "w")
        f.close()
      
      
    with open(os.path.join('result.txt'), 'a') as the_file:
        the_file.write(str(A)+'\n')
        the_file.write(str(B)+'\n')
        the_file.write(str(SUM))

def Set_A(value):
    A = value
    return A

def Set_B(value):
    B = value
    return B
    
def SUM_A_B(value_A, value_B):
    SUM = value_A + value_B
    return SUM

if __name__ == "__main__":
    #Call function here
    Execute_Test()