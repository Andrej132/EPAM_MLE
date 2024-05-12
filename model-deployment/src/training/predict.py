from utils import load_model,load_and_split_data
from sklearn.metrics import accuracy_score, recall_score, precision_score

X_train, X_test, y_train, y_test = load_and_split_data()
model = load_model()
predictions = model.predict(X_test)
with open('predicts.txt', 'w') as f:
    f.write("Accuracy: {}\n".format(accuracy_score(y_test, predictions)))
    f.write("Precision: {}\n".format(precision_score(y_test, predictions, average='macro')))
    f.write("Recall: {}\n".format(recall_score(y_test, predictions, average='macro')))
    for i in range(len(predictions)):
        f.write("{} {}\n".format(predictions[i], y_test[i]))