# Data governance

## Task

Using Data Version Control (DVC), it is necessary to set the dataset (Iris) on remote storage (S3), so that it can be downloaded with the command "dvc pull data/Iris.csv". I created 3 python files named basic_cleaning, scaling and outlier_detection that contain different preprocessing techniques. There is also a train file for training the model and creating a .json file for metrics. Using dvc.yaml, I have created 4 different stages that will be started in a specific order with the command "dvc repro". Finally, it is possible to view the results of the metrics with the command "dvc metrics show".

## How to run it?

The project is started with the command:
```
docker build -t dvc_image .
```
This command will create a docker image using dockerfile. After that, it is necessary to start the container in which all the previously mentioned commands will be started automatically:
```
docker run \
    -e AWS_ACCESS_KEY_ID=your_aws_access_key_id \
    -e AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key \
    -e AWS_DEFAULT_REGION=your_aws_region \
    dvc_image
```
Please change values with real credentials and region. The metrics and pipeline execution order can be seen in the console.
If you want to see pylint rates for python files in this project, please open new terminal and use command:
```
docker ps
```
It is necessary to copy the ID of the container that is active and then paste it into the command instead of <container_id> :
```
docker exec -it <container_id> /bin/sh
```
Then navigate to the directory in project with:
```
cd /app
```
and check rate for the python file you want with the command:
```
pylint name_of_the_file.py
```
where name_of_the_file is the actual name of the python file

