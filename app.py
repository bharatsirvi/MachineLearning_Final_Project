import numpy as np
import pandas as pd
from flask import Flask,render_template,request,redirect,session
import pickle
model =pickle.load(open('heart-disease.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',result="Please Fill This Form For Prediction")

@app.route('/reset',methods=['POST'])
def reset():
    return redirect('/')

@app.route('/predict',methods=['POST'])
def predict_health_insurance_cost():
    age_input = request.form.get('age')
    age = int(age_input) if age_input else 0
    sex=int(request.form.get('sex'))
    cp= int(request.form.get('cp') )
    trestbps_input = request.form.get('trestbps')
    trestbps = int(trestbps_input) if trestbps_input else 0
    chol_input = request.form.get('chol')
    chol = int(chol_input) if chol_input else 0
    fbs = int(request.form.get('fbs'))
    restecg = int(request.form.get('restecg'))
    thalach_input = request.form.get('thalach')
    thalach = int(thalach_input) if thalach_input else 0
    exang = int(request.form.get('exang'))
    oldpeak_input = request.form.get('oldpeak')
    oldpeak = float(oldpeak_input) if oldpeak_input else 0.0
    slope = int(request.form.get('slope'))
    ca = int(request.form.get('ca'))
    thal = int(request.form.get('thal'))

    if age==0 or sex==-1 or cp==-1 or trestbps==0 or chol==0 or fbs==-1 or restecg==-1 or thalach==0 or exang==-1 or oldpeak==0.0 or slope==-1 or ca==-1 or thal==-1:
        return render_template('index.html', result="All entries are mandatory ! Please provide Complete Information")
    else:
        query = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal],dtype=object).reshape(1, 13)
        result= model.predict(query)
        if result[0]==0:
            return render_template('index.html', result="NO Heart Disease")
        else:
            return render_template('index.html', result="Heart Disease")

if __name__ == '__main__':
    app.run(debug=True)


