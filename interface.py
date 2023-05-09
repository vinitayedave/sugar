from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from project_app.utils import Diabetes
app = Flask(__name__)

########################################################################

@app.route('/') 
def man():
    return render_template('home.html')
#########################################################################


@app.route('/predict',methods = ['POST'])
def get_predicted():

    data = request.form

    Glucose = eval(data['Glucose'])
    BloodPressure = eval(data['BloodPressure'])
    SkinThickness = eval(data['SkinThickness'])
    Insulin = eval(data['Insulin'])
    BMI = eval(data['BMI'])
    DiabetesPedigreeFunction = eval(data['DiabetesPedigreeFunction'])
    Age = eval(data['Age'])
    
    
    
    dib = Diabetes(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    result = dib.get_predicted()
    
    #return jsonify({"Result":f"Predict Patient having Diabetes : {result}"})
    #return render_template({"Result":f"Predict Patient having Diabetes : {result}"})
    return render_template('after.html',data = result)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)