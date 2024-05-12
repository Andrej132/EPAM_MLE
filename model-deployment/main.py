from flask import Flask, request, render_template
import numpy as np
import src.training.utils

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
