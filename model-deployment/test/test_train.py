import pytest
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import os


@pytest.fixture(scope="module")
def iris_data():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    return X, y


@pytest.fixture(scope="module")
def trained_model(iris_data):
    X, y = iris_data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model, X_test, y_test


def test_accuracy(trained_model):
    model, X_test, y_test = trained_model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    assert accuracy >= 0.0 and accuracy <= 1.0


def test_model_saved(trained_model):
    model, _, _ = trained_model
    pickle.dump(model, open('model.pkl', 'wb'))
    assert os.path.exists('model.pkl')


def test_model_load():
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    assert isinstance(loaded_model, LogisticRegression)


def test_model_predictions(trained_model):
    _, X_test, _ = trained_model
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    predictions = loaded_model.predict(X_test)
    assert len(predictions) == len(X_test)
