# Pipelines

## Task

Using the Iris dataset, it is necessary to train a machine learning model and create a DAG (Directed Acyclic Graph) with separate tasks. A task should represent a process in training.

## How to run?

I used the apache/airflow docker compose file along with the apache/airflow docker image. I added the installation of the necessary libraries from requrements.txt.

The command to build a new docker image that installs the required libraries is:
```
docker compose build
```
After that, it's necessary to start all containers from docker-compose file:
```
docker compose up
```
Wait for all the containers to start and you can access the link:
```
http://localhost:8080
```
You need to log in with username: airflow and password: airflow. Find dag named "decision-tree-training".
