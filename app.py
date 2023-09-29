# Library
import uvicorn 
from fastapi import FastAPI
from features import feature
import numpy as np
import pandas as pd 
import pickle

# Create the app object
app = FastAPI()

# Model load
pickleIn = open('model.pkl','rb')
classifier = pickle.load(pickleIn)

# Create a index page 
@app.get('/')
def index():
    return {'message':'Hello World!'}


# HTTP POST request is made to the "/predict" endpoint.
@app.post('/predict')

# This function handles the POST request to the "/predict" endpoint. It accepts data of type "feature" and assigns it to a variable named "data."
def predictDiabetes(data:feature):

    # Converts the incoming data into a Python dictionary. This makes it easier to work with the data later.
    data = data.dict()

    # Assign the data from the dictionary to relevant variables.
    Pregnancies=data['Pregnancies']
    Glucose=data['Glucose']
    BMI=data['BMI']
    DiabetesPedigreeFunction=data['DiabetesPedigreeFunction']


    # Stores the prediction result in a variable.
    prediction = classifier.predict([[Pregnancies,Glucose,BMI,DiabetesPedigreeFunction]])

    # If the prediction is 1, it is diabetes and if the prediction is 0, it is not diabetes. 
    if(prediction[0]==1):
        prediction="Diabetes"
    else:
        prediction="Not-Diabetes"
    return {
        'prediction': prediction
    }

# Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    