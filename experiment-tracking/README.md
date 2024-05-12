# Experiment tracking

## Task

Choose one problem related to machine learning and perform several different experiments to find out which is the best model, hyperparameters, metrics.. Use the MLflow library to observe various changes during experimentation. After the completed experiment, it is necessary to create two docker containers, where the first one will have the pipeline of the trainin, while the second one will run the MLflow server. The best model needs to be stored in AWS S3.

## How to run?

There are two docker files and docker-compose file, Dockerfile_pipeline and Dockerfile_mlflow, with train.py file and requirements.txt. Use the terminal to navigate to the directory and first you need to build images for both docker files with the command:
```
docker-compose build
```
When it's completed, you need to run both containers the command:
```
docker-compose up
```
when containers are started, you can see all experiments for all models on port http://0.0.0.0:5000

## Conclusions

Iris-dataset, which I used for classification, contains 4 features: Sepal Length, Sepal Width, Petal Length and Petal Width. Experimented with different combinations of features and I concluded that all combinations give similar and quite high results except for the combination: Sepal Length and Sepal Width, which gives lower accuracy. That makes sense because It's hard to tell which flower it is based on the sepals. I tested 3 different models, Logistic regression, Support vector machine and K-nearest neighbors. All models performed well on this problem, so I chose K-nearest neighbors as the model to store. If we talk about metrics, the dataset is completely balanced so that accuracy can give reliable results, while precision and recall were similar.

## Model storage

I used AWS S3 to store the model, and you can use the following link to copy-paste it into the browser and download the model will begin:
```
https://iris-classification-bucekt.s3.eu-north-1.amazonaws.com/iris_classifier_model.pkl
```


