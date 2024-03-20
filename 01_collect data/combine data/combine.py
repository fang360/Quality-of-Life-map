# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 02:58:56 2023

@author: jigme
"""

#%%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

#%%
# POI data
shelter = pd.read_csv('shelter.csv', encoding='utf-8', header=None).set_index(0)
poi = pd.read_csv('pois.csv', encoding='utf-8')
poi['multiHospital'] = poi['ID'].str.count('\|')+1
poi['名稱'][poi['名稱'].isna()==False]=1
poi = poi.set_index(poi[['COUNTYNAME', 'TOWNNAME', 'VILLNAME']].apply(
    lambda x: "".join(x.astype(str)), axis=1)).fillna(0)
poi.index.rename('index', inplace=True)
poifront = poi.iloc[:,:-3].groupby(['index']).mean()
poiback = poi.iloc[:,-2:].groupby(['index']).max()
poi = poifront.join(poiback)
poi = poi.join(shelter).fillna(0).rename(columns={"名稱": "Hospital", 1: "Shelter"})

#%%
# normal datasets
col108 = ["縣市名稱","鄉鎮市區代碼", 	"鄉鎮市區名稱",	"村里代碼", "村里名稱","人口數", "性比例", "人口密度", "扶養比", "扶幼比", "扶老比", "老化指數", "0-14歲人口數", "15-64歲人口數", "65歲以上人口數", "15歲以上博士人口數", "15歲以上碩士人口數", "15歲以上大學院校人口數", "15歲以上專科人口數", "15歲以上高中職人口數", "15歲以上國中初職人口數", "15歲以上小學人口數", "15歲以上自修人口數", "15歲以上不識字人口數", "15歲以上未婚人口數", "15歲以上有偶(不同性別)人口數", "15歲以上有偶(相同性別)人口數", "15歲以上離婚(不同性別)人口數", "15歲以上離婚(相同性別)人口數", "自然增加人數", "社會增加人數", "總戶數", "綜合所得總額", "綜合所得平均數", "綜合所得中位數", "綜合所得第一分位數", "綜合所得第三分位數",  "各類所得金額合計(108年起)", "各類所得金額薪資所得(108年起)"]
col = ["縣市名稱","鄉鎮市區代碼", "鄉鎮市區名稱",	"村里代碼", "村里名稱", "人口數", "性比例", "人口密度", "扶養比", "扶幼比", "扶老比", "老化指數", "0-14歲人口數", "15-64歲人口數", "65歲以上人口數", "15歲以上博士人口數", "15歲以上碩士人口數", "15歲以上大學院校人口數", "15歲以上專科人口數", "15歲以上高中職人口數", "15歲以上國中初職人口數", "15歲以上小學人口數", "15歲以上自修人口數", "15歲以上不識字人口數", "15歲以上未婚人口數", "15歲以上有偶人口數", "15歲以上離婚人口數", "自然增加人數", "社會增加人數", "總戶數", "綜合所得總額", "綜合所得平均數", "綜合所得中位數", "綜合所得第一分位數", "綜合所得第三分位數", "綜合所得標準差", "各類所得金額合計", "各類所得金額薪資所得"]


for i in range(105,110):
    if i <108:
        column = col
    else:
        column = col108
        
    df1 = pd.read_csv(str(i)+'.csv', encoding = 'utf8')
    df1 = df1.loc[:,column]
    df1 = df1[df1['縣市名稱'].isin(['新北市', '臺北市'])]
    df1 = df1.set_index(df1[['縣市名稱', '鄉鎮市區名稱', '村里名稱']].apply(
        lambda x: "".join(x.astype(str)), axis=1))
    print(i)

    #house
    house = pd.read_csv(str(i)+'indicator.csv')
    df1 = df1.merge(house, left_on='鄉鎮市區代碼', right_on='鄉鎮市區代碼').drop(columns=['Unnamed: 0'])
    #air no2
    no = pd.read_csv(str(i)+'no2com.csv', encoding = 'utf8')
    no = no.set_index(no[['COUNTYNAME', 'TOWNNAME', 'VILLNAME']].apply(
        lambda x: "".join(x.astype(str)), axis=1))
    no.index.rename('index', inplace=True)
    no = no.groupby('index')['DN'].mean()
    df1 = df1.join(no).fillna(no.mean()).rename(columns={"DN": "NO2"})
    #air pm2.5
    pm = pd.read_csv(str(i)+'pm25com.csv', encoding = 'utf8')
    pm = pm.set_index(pm[['COUNTYNAME', 'TOWNNAME', 'VILLNAME']].apply(
        lambda x: "".join(x.astype(str)), axis=1))
    pm.index.rename('index', inplace=True)
    pm = pm.groupby('index')['DN'].mean()
    df1 = df1.join(pm).fillna(pm.mean()).rename(columns={"DN": "PM2.5"})   
    df1 = df1.set_index(df1[['縣市名稱', '鄉鎮市區名稱', '村里名稱']].apply(
        lambda x: "".join(x.astype(str)), axis=1))
    # Landsat data
    df2 = pd.read_csv('source3.csv', encoding = 'utf8')
    df2 = df2.fillna(0)
    df2 = df2.set_index(df2[['COUNTYNAME', 'TOWNNAME', 'VILLNAME']].apply(
        lambda x: "".join(x.astype(str)), axis=1))
    df2 = df2.filter(regex=(str(i)))
    df3  = df1.join(df2, how= "left")
    #poi
    df3 = df3.join(poi).fillna(0)
    df3.iloc[:,5:].to_csv('a'+str(i)+'dataset.csv')

#%%
df3.info()