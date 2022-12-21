import pickle
import json
from flask import Flask, request
import pandas as pd
import numpy as np


model = pickle.load(open("laboratorio-machine-learning/models/version2.0/model.pk", "rb"))
scaler = pickle.load(open("laboratorio-machine-learning/models/version2.0/scaler.pk", "rb"))

# create the Flask app
app = Flask(__name__)

def country_to_numeric(country):
    countries={'France': [1, 0, 0], 'Germany': [0, 1, 0], 'Spain': [0, 0, 1]}
    return countries[country]

def convert_numerical(features):
    output = []
    geography = []

    for i, feat in enumerate(features):
        if i == 1:
            geography=country_to_numeric(feat)
        else:
            try:
                output.append(pd.to_numeric(feat))
            except:
                gender_to_numeric = lambda feat: 1 if feat=='Female' else 0
                output.append(gender_to_numeric(feat))
    output+=geography
    return output

@app.route('/query')
def query_example():
    features = convert_numerical(request.args.get('feats').split(','))
    response = {
        'response': [int(x) for x in model.predict([scaler.transform(np.array(features).reshape(1, -1))[0]])]
    }
    return json.dumps(response)

if __name__ == '__main__':
    # run app in debug mode on port 3001
    app.run(debug=True, port=3001)

