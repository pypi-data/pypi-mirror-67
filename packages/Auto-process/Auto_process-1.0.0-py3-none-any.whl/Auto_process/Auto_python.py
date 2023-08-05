# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 02:31:13 2020

@author: Roshan
"""

#--------Reading Libraries--------------#

import pandas as pd
import numpy as np

#-------Reading dataset-----------------#

def dropping_variables(X,thresold):
    for i in X.columns:
       if (X[i].isnull().sum()/len(X[i]))>thresold:
           X.drop(i,axis=1)
    return X

def main():
    X1 = X
    X1 = dropping_variables(X1,thresold=0.20)
    

if __name__ == "__main__":
    main()            