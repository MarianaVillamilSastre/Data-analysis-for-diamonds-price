# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:05:32 2020

@author: maria
"""

import numpy as np
from flask import Flask, request, jsonify
import pickle
import json

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    print('hola')
    data = request.get_json(force=True)
    if(not data):
        print('No llego nada')
    else:
        return funcion(data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    

def funcion(variable):
    
    data=json.loads(variable)
    
    
    prediction = model.predict([[np.array(data['input'])]])
    output = prediction[0]   
    cleanup_rules = ({'NEUTRAL': 0, 'POSITIVE': 1, 'NEGATIVE': 2} )
    output=cleanup_rules[output]
    diccionario_output={"output": output}
    

    
    return jsonify(diccionario_output)










