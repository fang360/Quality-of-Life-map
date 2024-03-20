# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 20:04:02 2023

@author: jigme
"""
#%%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

#%%
# air quality
       
folder = '北部空品區_'
point = pd.read_csv('points.csv', encoding='utf-8').set_index('SiteName')
for i in range(2016,2018):
    val = []
    allFileList = os.listdir('./'+folder+str(i)+"/")
    for file in allFileList:
        print('now at:', file)
        df = pd.read_csv('./'+folder+str(i)+"/"+file, encoding = 'unicode_escape')
        df = df.iloc[1:,:].replace('#|x|\*','', regex=True).dropna()
        dfpm = df[df.iloc[:,2]=='PM2.5']
        dfno = df[df.iloc[:,2]=='NO2']
        a = dfno.iloc[:,3:].astype('float').stack().mean()
        b= dfpm.iloc[:,3:].astype('float').stack().mean()
        val.append([a,b])
    #     break
    # break

    dfall = pd.DataFrame(val, index=[i.split('_', 1)[0] for i in allFileList])
     
    final = dfall.join(point)
    final.to_csv(str(i)+'air.csv')
#%%
# air quality 108-110
folder = '北部空品區_'
point = pd.read_csv('points.csv', encoding='utf-8').set_index('SiteName')
for i in range(2020,2022):
    val = []
    allFileList = os.listdir('./'+folder+str(i)+"/")
    for file in allFileList:
        print('now at:', file)
        df = pd.read_csv('./'+folder+str(i)+"/"+file, encoding = 'unicode_escape')
        df = df.iloc[1:,:].replace('',None, regex=True).replace('#|x|\*|A',None, regex=True).dropna()
        dfpm = df[df.iloc[:,2]==df.iloc[8,2]]
        dfno = df[df.iloc[:,2]==df.iloc[5,2]]
        a = dfno.iloc[:,3:].astype('float').stack().mean()
        b= dfpm.iloc[:,3:].astype('float').stack().mean()
        val.append([a,b])

    dfall = pd.DataFrame(val, index=[i.split('_', 1)[0] for i in allFileList])
     
    final = dfall.join(point)
    final.to_csv(str(i)+'air.csv')
#%%

shape = pd.read_csv('105airshape.csv', encoding='utf-8')
SHAPE = shape[["DN", "VILLAGE", "COUNTY", "TOWN"]].groupby(["COUNTY", "TOWN", "VILLAGE"]).mean()
SHAPE.to_csv(str(105)+'air.csv')
