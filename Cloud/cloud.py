
import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
from joblib import dump

def getData():
    """ loads, shuffles, categorizes and splits data

    Returns:
        [type] [description]
        X_train [np.ndarray]: attribute values of train data
        X_test [np.ndarray]: attribute values of test data
        y_train [np.ndarray]: class labels of train data
        y_test [np.ndarray]: class labels of test data
    """

    # read data
    with open("Cloud/storage/data/data.csv", "r") as file_object:
        raw_data = file_object.read().split('\n')

    # remove empty string
    raw_data = [x for x in raw_data if x]

    # split each row from ','
    splitted_data = []
    for i in raw_data:
        splitted_data += [ list(map(int, i.split(',')))]

    random.shuffle(splitted_data)

    # categorize attributes
    for i in range(len(splitted_data)):
        if splitted_data[i][1] <= 100:
            splitted_data[i][1] = 0
        else:
            splitted_data[i][1] = 1

        if splitted_data[i][2] <= 10:
            splitted_data[i][2] = 0
        else:
            splitted_data[i][2] = 1

    data = np.array(splitted_data)

    X_train, X_test, y_train, y_test = train_test_split(list(data[:,0:4]), list(data[:,4]), test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    """ start point of the Clout System,
        creates model, trains it and stores it in the Clout storage

    """
    # get cleaned and splitted data
    X_train, X_test, y_train, y_test = getData()

    # create a decision tree model
    model = tree.DecisionTreeClassifier()

    # train the model
    model.fit(X_train, y_train)

    # test the model
    y_pred = model.predict(X_test)
    print(accuracy_score(y_test, y_pred))

    # store model in the clout storage
    dump(model, 'Cloud/storage/model.joblib')