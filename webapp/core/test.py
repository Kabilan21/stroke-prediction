import pandas as pd
from sklearn.metrics import accuracy_score
import pickle

from webapp.settings import CLASSIFIER_PATH, ENCODER_PATH, SCALER_PATH


def age_group(x):
    if x < 13:
        return "Child"
    elif 13 < x < 20:
        return "Teenager"
    elif 20 < x <= 60:
        return "Adult"
    else:
        return "Elder"


def bmi_group(x):
    if x < 18.5:
        return "UnderWeight"
    elif 18.5 < x < 25:
        return "Healthy"
    elif 25 < x < 30:
        return "OverWeight"
    else:
        return "Obese"


categorical_features = ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type',
                        'Residence_type', 'smoking_status', "age_group", "bmi_group"]


def process_input(x):
    encoders = pickle.load(open(ENCODER_PATH, "rb"))
    std = pickle.load(open(SCALER_PATH, "rb"))
    columns = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
               'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status', ]
    x = pd.DataFrame(x, columns=columns)
    x["bmi_group"] = x.bmi.apply(bmi_group)
    x["age_group"] = x.age.apply(age_group)
    for each in categorical_features:
        x[each] = encoders[each].transform(x[each])
    x = std.transform(x)
    return x


def process(gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status):
    sv = pickle.load(open(CLASSIFIER_PATH, "rb"))

    x = [[gender, age, hypertension, heart_disease, ever_married, work_type,
          residence_type, avg_glucose_level, bmi, smoking_status]]
    x = process_input(x)
    y = sv.predict(x)
    return y[0]
