
#--------Reading Libraries--------------#

import pandas as pd
import numpy as np

#-------Reading dataset-----------------#

def dropping_variables(X,thresold):
    for i in X.columns:
       if (X[i].isnull().sum()/len(X[i]))>thresold:
           X.drop(i,axis=1)
    return X

     