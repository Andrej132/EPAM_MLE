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

![image](https://github.com/Andrej132/EPAM_MLE/assets/93214115/ed56311d-0060-4313-ba03-7f41aa3665ab)

### 3. Create the SageMaker Model, Endpoint Configuration and Endpoint
Create a SageMaker model pointing to the Docker image in ECR.
Create an endpoint configuration specifying instance type and other parameters.
Create an endpoint using the configuration.

![model](https://github.com/Andrej132/EPAM_MLE/assets/93214115/c70e320d-bbec-412a-a2e6-e4005713be84)

![endpoint_configuration](https://github.com/Andrej132/EPAM_MLE/assets/93214115/2525db05-8dcf-41ea-990d-0b0cd65afeab)

![endpoint](https://github.com/Andrej132/EPAM_MLE/assets/93214115/736e5e4b-7efc-4a7f-a8d7-7f2547d561de)

### 4. Create Lambda function and API Gateway
Write a Lambda function in Python to call the SageMaker endpoint.
Deploy the Lambda function on AWS.
Create a new REST API in API Gateway.
Create a resource and a POST method.

![function](https://github.com/Andrej132/EPAM_MLE/assets/93214115/b9d81a25-f6df-4143-9f2e-6b431f238d8c)

![post_method](https://github.com/Andrej132/EPAM_MLE/assets/93214115/719ac4e2-7659-4932-8cb2-ad0ec40c9d9d)

### 5. Test the Deployed Endpoint
Use an HTTP client (e.g., Postman or curl) to send requests to the API Gateway endpoint.

![test](https://github.com/Andrej132/EPAM_MLE/assets/93214115/9d118a09-2574-40e8-a13d-764eb5c1d177)

Endpoint can be invoked by using terminal. Open the terminal in project folder and create a docker image and run the the container. 
Docker image:
```
docker build -t image .
```
Run the container on port 8080:
```
docker run -p 8080:8080 image
```
If the application is running, open new terminal and enter the command:
```
curl -X POST http://localhost:8080/invocations -H "Content-Type: application/json" -d '{"input": {"sepal_length": 5.1,"sepal_width": 3.5,"petal_length": 1.4,"petal_width": 0.2}}'
``` 



