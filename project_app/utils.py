from operator import index
import pickle
import json
import numpy as np
import config 

class Diabetes():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age
        
        

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)
            
    def get_predicted(self):
        self.load_model()
        
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.Glucose
        test_array[1] = self.BloodPressure
        test_array[2] = self.SkinThickness
        test_array[3] = self.Insulin
        test_array[4] = self.BMI
        test_array[5] = self.DiabetesPedigreeFunction
        test_array[6] = self.Age
        
        predicted = self.model.predict([test_array])
        return predicted
          
        
if __name__ == "__main__":
    
    Glucose = 150
    BloodPressure = 66
    SkinThickness = 23
    Insulin = 94
    BMI = 28.1
    DiabetesPedigreeFunction = 0.167
    Age = 21

    dib = Diabetes(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    dib.get_predicted()
    
                    