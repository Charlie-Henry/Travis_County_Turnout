# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:51:32 2020

@author: charlie.henry
"""

import pandas as pd
import numpy as np

file_name="24hr Report - G20 In Person 10-15.csv"


data = pd.read_csv(file_name)

data=data.rename(columns=data.iloc[2])
data.drop(data.index[2])

data_columns = data.columns

a=["1","IP","F/A","F/B","F/C"]

data.drop(data[~data[data_columns[0]].isin(a)].index, inplace = True) 


pct_results = data.groupby(['PCT']).count()


pct_results.to_csv(file_name[:-4] +' PCT Results.csv')