### classifier

import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression



def classifier(features):
    model = pickle.load(open('lr.p','rb'))
    scaler = StandardScaler()
    #X = scaler.fit_transform(features)
    predict = model.predict(features)
    return predict
