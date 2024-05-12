from sklearn import datasets
from sklearn.model_selection import train_test_split
import pickle


def load_and_split_data():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


def load_model():
    model = pickle.load(open('model.pkl', 'rb'))
    return model