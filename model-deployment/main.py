from flask import Flask, request, render_template, send_file
import numpy as np
import src.training.utils
import pandas as pd
from sklearn.datasets import load_iris

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    feature_values = [float(x) for x in request.form.values()]
    model = src.training.utils.load_model()
    feature_array = np.array(feature_values)
    prediction = model.predict(feature_array.reshape(1, -1)).tolist()
    output = ['setosa', 'versicolor', 'virginica'][prediction[0]]
    return render_template('index.html', prediction_text='The Flower is {}'.format(output))


@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    iris = load_iris()
    iris_data = iris.data
    model = src.training.utils.load_model()
    predictions = model.predict(iris_data)
    predictions_df = pd.DataFrame(iris_data, columns=iris.feature_names)
    predictions_df['predictions'] = predictions
    file_path = '/app/src/training/iris_with_predictions.csv'
    predictions_df.to_csv(file_path, index=False)
    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
