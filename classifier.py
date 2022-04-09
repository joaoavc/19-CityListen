### classifier

import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression



def classifier(features):
    model = pickle.load(open('model.p','rb'))
    scaler = StandardScaler()
    X = scaler.fit_transform(features)
    predict = model.predict(X)
    return predict
