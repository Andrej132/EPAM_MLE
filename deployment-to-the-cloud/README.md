# Deployment to the Cloud

## Task

The goal of this task is to deploy a pre-trained machine learning model as an endpoint using AWS SageMaker. The endpoint will serve predictions in response to HTTP requests with features for inference. This task involves creating a Docker container for inference, uploading it to AWS ECR, and setting up an endpoint in SageMaker.

## Steps to complete the task:

### 1. Create a Docker Container for Inference
Prepare a dockerfile defining the environment and dependencies.
Implement the inference logic in a server (Flask).
Build and test the Docker container locally to ensure it responds to HTTP requests correctly.

### 2. Upload the Container to AWS ECR
Create a repository in ECR.
Authenticate Docker to the ECR registry.
Tag and push the Docker image to the ECR repository.

### 3. Create the SageMaker Model, Endpoint Configuration and Endpoint
Create a SageMaker model pointing to the Docker image in ECR.
Create an endpoint configuration specifying instance type and other parameters.
Create an endpoint using the configuration.

### 4. Create Lambda function and API Gateway
Write a Lambda function in Python to call the SageMaker endpoint.
Deploy the Lambda function on AWS.
Create a new REST API in API Gateway.
Create a resource and a POST method.

### 5. Test the Deployed Endpoint
Use an HTTP client (e.g., Postman or curl) to send requests to the API Gateway endpoint.


