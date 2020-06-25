# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:38:49 2020

@author: maria
"""
import requests
import json
import pandas as pd
import numpy as np

url = 'http://127.0.0.1:5000/'

emo= pd.read_csv("Data/emotions.csv")

entrada = emo.iloc[1:2, 0:2548]
entrada2=np.array(entrada)
entrada3= entrada2.tolist()[0]

diccionario_input={"input": entrada3}

j_data = json.dumps(diccionario_input)
print(type(entrada3),diccionario_input)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)