# Containerization

I have a train.py file where I created a neural network using pytorch. The problem I was solving was the Iris dataset, where I have a multiclass classification with four features. In addition, I have a requirements.txt file that contains the required libraries with certain versions and a dockerfile that contains commands for creating a docker image.

My task was to setup environment so that anyone can run model training and get predictions using docker. In addition, it was necessary to observe as many common docker practices as possible.

How to run?

1. Open terminl in "Containerization" directory.

2. Write next command in terminal:
``` 
docker build -t image . 
```
3. When it's completed, you can run the container with mounted volume
```
docker run -v $(pwd):/app/test_results image
```
4. We can see training process in terminal and when it's completed, we will get accuracy and predictions.txt file with class predictions.

Docker image name can be changed. In this case, image name is "image".

