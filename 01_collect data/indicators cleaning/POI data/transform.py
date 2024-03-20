# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 17:44:49 2023

@author: jigme
"""
#%%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

#%%
allFileList = os.listdir('./')
for file in allFileList:
    if file != 'transform.py':
        df = pd.read_csv(file, encoding = 'utf8')
        newName = file.split('- ')[1]
        df = df.dropna(axis='columns', how='all')
        df['WKT'] = df['WKT'].str.strip('POINT( )')
        df[['lon', 'lat']] = df['WKT'].str.split(' ', expand = True)
        df.iloc[:,1:].to_csv(newName)
        
  
#%%
# normal datasets
col108 = ["縣市名稱","鄉鎮市區代碼", 	"鄉鎮市區名稱",	"村里代碼", "村里名稱","人口數", "性比例", "人口密度", "扶養比", "扶幼比", "扶老比", "老化指數", "0-14歲人口數", "15-64歲人口數", "65歲以上人口數", "15歲以上博士人口數", "15歲以上碩士人口數", "15歲以上大學院校人口數", "15歲以上專科人口數", "15歲以上高中職人口數", "15歲以上國中初職人口數", "15歲以上小學人口數", "15歲以上自修人口數", "15歲以上不識字人口數", "15歲以上未婚人口數", "15歲以上有偶(不同性別)人口數", "15歲以上有偶(相同性別)人口數", "15歲以上離婚(不同性別)人口數", "15歲以上離婚(相同性別)人口數", "自然增加人數", "社會增加人數", "總戶數", "綜合所得總額", "綜合所得平均數", "綜合所得中位數", "綜合所得第一分位數", "綜合所得第三分位數", "各類所得金額薪資所得", "各類所得金額合計(108年起)", "各類所得金額薪資所得(108年起)"]
col = ["縣市名稱","鄉鎮市區代碼", "鄉鎮市區名稱",	"村里代碼", "村里名稱", "人口數", "性比例", "人口密度", "扶養比", "扶幼比", "扶老比", "老化指數", "0-14歲人口數", "15-64歲人口數", "65歲以上人口數", "15歲以上博士人口數", "15歲以上碩士人口數", "15歲以上大學院校人口數", "15歲以上專科人口數", "15歲以上高中職人口數", "15歲以上國中初職人口數", "15歲以上小學人口數", "15歲以上自修人口數", "15歲以上不識字人口數", "15歲以上未婚人口數", "15歲以上有偶人口數", "15歲以上離婚人口數", "自然增加人數", "社會增加人數", "總戶數", "綜合所得總額", "綜合所得平均數", "綜合所得中位數", "綜合所得第一分位數", "綜合所得第三分位數", "綜合所得標準差", "各類所得金額合計", "各類所得金額薪資所得"]
df1 = pd.read_csv('105.csv', encoding = 'utf8')
df1 = df1.loc[:,col]
df1 = df1[df1['縣市名稱'].isin(['新北市', '臺北市'])]
df1 = df1.set_index(df1[['縣市名稱', '鄉鎮市區名稱', '村里名稱']].apply(
    lambda x: "".join(x.astype(str)), axis=1))

#%%


#%%
# POI data
df2 = pd.read_csv('source3.csv', encoding = 'utf8')
df2 = df2.fillna(0)
df2 = df2.set_index(df2[['COUNTYNAME', 'TOWNNAME', 'VILLNAME']].apply(
    lambda x: "".join(x.astype(str)), axis=1))

#%%

df3 = df2.filter(regex=("105|[^0-9]"))
df3  = df1.join(df3, how= "left")

#%%
df3.info()