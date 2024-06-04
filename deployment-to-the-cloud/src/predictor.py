import os
import json
import boto3
import joblib
import flask
import logging

#Define the path
prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')
logging.info("Model Path" + str(model_path))

# Load the model components
model = joblib.load(os.path.join(model_path, 'model.pkl'))
logging.info("Model" + str(model))

flower_names = {
    0: 'Setosa',
    1: 'Versicolor',
    2: 'Virginica'
}

# The flask app for serving predictions
app = flask.Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    # Check if the model was loaded correctly
    try:
        status = 200
        logging.info("Status : 200")
    except:
        status = 400
    return flask.Response(response=json.dumps(' '), status=status, mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def transformation():
    # Get input JSON data and convert it to a DataFrame
    input_json = flask.request.get_json()

    # Extract features for the Iris dataset
    sepal_length = input_json['input']['sepal_length']
    sepal_width = input_json['input']['sepal_width']
    petal_length = input_json['input']['petal_length']
    petal_width = input_json['input']['petal_width']

    # Create a feature array
    features = [[sepal_length, sepal_width, petal_length, petal_width]]

    # Make a prediction using the model
    predictions = model.predict(features)
    predicted_class = int(predictions[0])

    predicted_flower = flower_names.get(predicted_class, 'Unknown')

    # Transform prediction to JSON
    result = {
        'output': predicted_flower
    }

    result_json = json.dumps(result)

    """
    This code will delete the endpoint after use. This code is commented out because I didn't write the code to 
    create the endpoint, but I created it manually, so this code will delete the endpoint every time but will not 
    create it again.
    sagemaker_client = boto3.client('sagemaker', region_name="eu-north-1")
    sagemaker_client.delete_endpoint(EndpointName="iris-endpoint")
    """
    return flask.Response(response=result_json, status=200, mimetype='application/json')
