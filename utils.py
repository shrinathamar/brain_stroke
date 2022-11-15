import numpy as np
import config
import pickle
import json

class BrainStroke():

    def __init__(self, gender, age,  hypertension, heart_disease, ever_married, Residence_type, avg_glucose_level, bmi, smoking_status, work_type):
        self.gender   = gender
        self.age      = age
        self.hypertension      = hypertension
        self.heart_desease     = heart_disease
        self.ever_married      = ever_married
        self.Residence_type    = Residence_type
        self.avg_glucose_level = avg_glucose_level
        self.bmi            = bmi
        self.smoking_status = smoking_status
        self.work_type      = "work_type_"+ work_type

    def load_model(self):
        
        with open(config.MODEL_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_PATH, "r") as f:
            self.json_data = json.load(f)

    def Predict_brain_stroke(self):
        self.load_model()

        test_array = np.zeros(14)

        test_array[0]  = self.json_data["select_gender"][self.gender]
        test_array[1]  = self.age
        test_array[2]  = self.json_data["hypertension_select"][self.hypertension]
        test_array[3]  = self.json_data["heart_disease_select"][self.heart_desease]
        test_array[4]  = self.json_data["ever_married_select"][self.ever_married]
        test_array[5]  = self.json_data["Residence_type"][self.Residence_type]
        test_array[6]  = self.avg_glucose_level
        test_array[7]  = self.bmi
        test_array[8]  = self.json_data["smoker_select"][self.smoking_status]

        job = self.work_type
        idx = np.where(self.json_data["work_type"] == job)
        test_array[idx]  = 1 

        prediction = self.model.predict([test_array])[0]
        return prediction













# ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
#        'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status',
#        'work_type_Govt_job', 'work_type_Never_worked', 'work_type_Private',
#        'work_type_Self-employed', 'work_type_children'],

#     age               = 76
# avg_glucose_level = 194.3
# bmi               = 30
 
# gender            = "Male"

# hypertension      = "Yes"
# heart_disease     = "No"
# ever_married     = "Yes"

# Residence         = "Urban"
# smoker = "formerly smoked"
# work_type         = "Self-employed"