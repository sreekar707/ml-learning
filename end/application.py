import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from flask import Flask,jsonify,render_template,request

application= Flask(__name__)
app=application

# ### import ridge regressor and standard scaler
ridge_model=pickle.load(open('end/models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('end/models/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        temperature = float(request.form.get('temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        
        
        new_data_scaled=standard_scaler.transform([[temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)
        
        return render_template('home.html',results=result[0])
    
    else:
        return render_template('home.html')
    
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)