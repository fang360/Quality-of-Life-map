# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 22:35:08 2023

@author: jigme
"""

#%%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

#%%
#col = ["縣市代碼","縣市名稱","鄉鎮市區名稱","不含車位_各建物型態合計棟數","不含車位_公寓棟數","不含車位_透天厝棟數","不含車位_店面(店舖)棟數","不含車位_辦公商業大樓棟數","不含車位_住宅大樓棟數","不含車位_華廈棟數","不含車位_套房棟數","不含車位_工廠棟數","不含車位_廠辦棟數","不含車位_農舍棟數","不含車位_倉庫棟數","不含車位_其他建物型態棟數","不含車位_各建物型態合計面積","不含車位_公寓面積","不含車位_透天厝面積","不含車位_店面(店舖)面積","不含車位_辦公商業大樓面積","不含車位_住宅大樓面積","不含車位_華廈面積","不含車位_套房面積","不含車位_工廠面積","不含車位_廠辦面積","不含車位_農舍面積","不含車位_倉庫面積","不含車位_其他建物型態面積","不含車位_各建物型態整體中位數房價","不含車位_公寓中位數房價","不含車位_透天厝中位數房價","不含車位_店面(店舖)中位數房價","不含車位_辦公商業大樓中位數房價","不含車位_住宅大樓中位數房價","不含車位_華廈中位數房價","不含車位_套房中位數房價","不含車位_工廠中位數房價","不含車位_廠辦中位數房價","不含車位_農舍中位數房價","不含車位_倉庫中位數房價","不含車位_其他建物型態中位數房價","含車位_各建物型態合計棟數","含車位_公寓棟數","含車位_透天厝棟數","含車位_店面(店舖)棟數","含車位_辦公商業大樓棟數","含車位_住宅大樓棟數","含車位_華廈棟數","含車位_套房棟數","含車位_工廠棟數","含車位_廠辦棟數","含車位_農舍棟數","含車位_倉庫棟數","含車位_其他建物型態棟數","含車位_各建物型態合計面積","含車位_公寓面積","含車位_透天厝面積","含車位_店面(店舖)面積","含車位_辦公商業大樓面積","含車位_住宅大樓面積","含車位_華廈面積","含車位_套房面積","含車位_工廠面積","含車位_廠辦面積","含車位_農舍面積","含車位_倉庫面積","含車位_其他建物型態面積","含車位_各建物型態整體中位數房價","含車位_公寓中位數房價","含車位_透天厝中位數房價","含車位_辦公商業大樓中位數房價","含車位_住宅大樓中位數房價","含車位_華廈中位數房價","含車位_套房中位數房價","含車位_其他建物型態中位數房價"]
for i in range(2016,2022):  
    df = pd.read_csv("./"+str(i)+"_housing/"+str(i-1911)+'_housing.csv', encoding = 'utf-8')
    df = df[df['縣市名稱'].isin(['新北市','臺北市'])].loc[:,["鄉鎮市區代碼",'含車位_各建物型態整體中位數房價', '不含車位_各建物型態整體中位數房價']]
    df['含車位_各建物型態整體中位數房價'] = df['含車位_各建物型態整體中位數房價'].fillna(df['含車位_各建物型態整體中位數房價'].nsmallest(5).mean())
    df['不含車位_各建物型態整體中位數房價'] = df['不含車位_各建物型態整體中位數房價'].fillna(df['不含車位_各建物型態整體中位數房價'].nsmallest(5).mean())
    df.info()
    df.to_csv(str(i-1911)+'indicator.csv')
