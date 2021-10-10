import pandas as pd
from sklearn.metrics import accuracy_score
import pickle


def process_input(x):
    enc = pickle.load(open("enc.pk", "rb"))
    columns = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
               'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']
    x = pd.DataFrame(x, columns=columns)
    for each in columns:
        x[each] = enc.fit_transform(x[each])
    return x


def process(gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status):
    sv = pickle.load(open("svm.pk", "rb"))
    x = [[gender, age, hypertension, heart_disease, ever_married, work_type,
          residence_type, avg_glucose_level, bmi, smoking_status]]
    x = process_input(x)
    y = sv.predict_proba(x)
    return y[0]
