### classifier

import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import time



def classifier(features):
    model = pickle.load(open('decision_tree.p','rb'))
    scaler = StandardScaler()
    #X = scaler.fit_transform(features)
    start_time = time.time()
    predict = model.predict(features)
    print("--- %s seconds ---" % (time.time() - start_time))
    return predict
