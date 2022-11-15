import json
from flask import Flask, request, jsonify, render_template
import config
from utils import BrainStroke


app = Flask(__name__)

@app.route("/")
def get_home():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict_stroke():
    input_data = request.form
    gender            = input_data["gender"]   #
    age               = int(input_data["age"]) #
    hypertension      = (input_data["hypertension"])
    heart_disease     = (input_data["heart_disease"])
    ever_married      = (input_data["ever_married"])
    Residence_type    = (input_data["Residence_type"])
    avg_glucose_level = eval(input_data["avg_glucose_level"])  #
    bmi               = eval(input_data["bmi"])                #
    smoking_status    = (input_data["smoking_status"])
    work_type        = (input_data["work_type"])

    stroke = BrainStroke(gender, age,  hypertension, heart_disease, ever_married, Residence_type, avg_glucose_level, bmi, smoking_status, work_type)
    prediction = stroke.Predict_brain_stroke()
    if prediction == 1:
        result = "This is Brain Stroke"
    else:
        result = "This is Not a Brain Stroke"
    return render_template("index2.html", ans=result)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT_NUM1)