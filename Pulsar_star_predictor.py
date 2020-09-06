# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:09:07 2020

@author: anirudhrvs
"""
# import
import pandas as pd

#reading the dataset
df= pd.read_csv('pulsar_stars.csv')

# taking independant variables into x and dependant variable into y
x= df.drop(columns='target_class')
y= df['target_class']

# train test split
from sklearn import model_selection
x_train ,x_test , y_train, y_test = model_selection.train_test_split(x,y, test_size = 0.3)

# random forest
from sklearn.ensemble import RandomForestRegressor
ran_state= 123
model= RandomForestRegressor(verbose=2, random_state= ran_state, oob_score= True, warm_start=True) #, ccp_alpha= non-negative float

# model fitting
model.fit(x_train, y_train)

# taking inputs for all input field attributes
a1= float(input('Enter Mean of the integrated profile:- '))
a2= float(input('Enter Standard deviation of the integrated profile:- '))
a3= float(input('Enter Excess kurtosis of the integrated profile:- '))
a4= float(input('Enter Skewness of the integrated profile:- '))
a5= float(input('Enter Mean of the DM-SNR curve:- '))
a6= float(input('Enter Standard deviation of the DM-SNR curve:- '))
a7= float(input('Enter Excess kurtosis of the DM-SNR curve:- '))
a8= float(input('Enter Skewness of the DM-SNR curve:- '))

# arranging in the order of input attributes 
data=[(a1, a2, a3, a4, a5, a6, a7, a8)]

# defining a prediction dataframe 
x_pred= pd.DataFrame(data,
                     columns= [' Mean of the integrated profile',
                               ' Standard deviation of the integrated profile',
                               ' Excess kurtosis of the integrated profile',
                               ' Skewness of the integrated profile',
                               ' Mean of the DM-SNR curve',
                               ' Standard deviation of the DM-SNR curve',
                               ' Excess kurtosis of the DM-SNR curve',
                               ' Skewness of the DM-SNR curve'])
# predicting the target class
y_pred= model.predict(x_pred)

# fetching the target class
array_length = len(y_pred)
star_class = y_pred[array_length - 1]
print('Target class:- ', round(star_class))