from flask import Flask, request, render_template, send_file
import numpy as np
import src.training.utils
import pandas as pd

app = Flask(__name__)
pred_dict = {0: "setosa", 1: "versicolor", 2: "virginica"}


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
    if 'file' not in request.files:
        return "There is no key 'file' in the request", 400

    file = request.files['file']

    if file.filename == '':
        return "File is not selected", 400

    file_path = "batch.csv"
    file.save(file_path)
    iris = pd.read_csv(file_path)
    model = src.training.utils.load_model()
    predictions = model.predict(iris)
    iris['predictions'] = [pred_dict[prediction] for prediction in predictions]
    iris.to_csv(file_path, index=False)
    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
