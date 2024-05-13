from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score
import pickle
from utils import load_and_split_data

X_train, X_test, y_train, y_test = load_and_split_data()
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
pickle.dump(model, open('/app/src/training/model.pkl', 'wb'))
print("Accuracy: ", accuracy_score(y_test, predictions))
print("Precision: ", precision_score(y_test, predictions, average='macro'))
print("Recall: ", recall_score(y_test, predictions, average='macro'))
