# Model deployment

## Task

Train the model on the Iris dataset in two modes: online using the Flask framework and batch with the scheduler. It is necessary to test the entire training using the pytest library. The entire project should be packaged in a python package.

## How to run?

The command to build a new docker image that installs the required libraries is:
```
docker compose build
```
After that, it's necessary to start all containers from docker-compose file:
```
docker compose up
```

Three containers are started: first for training, second for api and third for tests.Metrics and test results can be viewed in the terminal.You can see the html page on link:
```
http://127.0.0.1:5000
```
You can open another terminal and use a command:
```
curl -X POST -F "file=@batch.csv" http://127.0.0.1:5000/batch_predict -o batch_with_predictions.csv
```
This command will start batch mode and you can see the prediction results in the new batch_with_predictions.csv file.
