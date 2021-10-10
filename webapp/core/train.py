from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pickle

data = pd.read_csv("data/data.csv")
data['bmi'].fillna(data['bmi'].mean(), inplace=True,)
data.drop('id', inplace=True, axis=1)
categorical_features = ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type',
                        'Residence_type', 'smoking_status']
enc = LabelEncoder()

for each in categorical_features:
    data[each] = enc.fit_transform(data[each])

X = data.drop('stroke', axis=1)
y = data['stroke']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

sv = SVC(probability=True)
sv.fit(x_train, y_train)

y_pred = sv.predict(x_test)
ac_rf = accuracy_score(y_test, y_pred)

pickle_sv = open("svm.pk", 'wb')
pickle.dump(sv, pickle_sv)
pickle_sv.close()

pickle_en = open("enc.pk", 'wb')
pickle.dump(enc, pickle_en)
pickle_en.close()
