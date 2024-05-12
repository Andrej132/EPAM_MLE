from typing import Any
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, recall_score, precision_score
import pandas as pd
from sklearn.utils import shuffle
import mlflow
from mlflow.models.signature import infer_signature
from mlflow.data.pandas_dataset import PandasDataset


def create_mlflow_experiment(experiment_name: str, artifact_location: str, tags: dict[str, Any]) -> str:
    try:
        experiment_id = mlflow.create_experiment(
            name=experiment_name, artifact_location=artifact_location, tags=tags
        )

    except:
        print(f"Experiment {experiment_name} already exists.")
        experiment_id = mlflow.get_experiment_by_name(experiment_name).experiment_id
    
    mlflow.set_experiment(experiment_name=experiment_name)
 
    return experiment_id


def get_mlflow_experiment(experiment_id: str = None, experiment_name: str = None) -> mlflow.entities.Experiment:
    if experiment_id is not None:
        experiment = mlflow.get_experiment(experiment_id)
    elif experiment_name is not None:
        experiment = mlflow.get_experiment_by_name(experiment_name)
    else:
        raise ValueError("Either experiment_id or experiment_name must be provided.")
    return experiment


def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return shuffle(df, random_state=42)


def train_model(model, X_train, y_train, param_grid):
    grid_search = GridSearchCV(model, param_grid, cv=5)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_, grid_search.best_params_


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')
    metrics = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall
    }
    return metrics


def perform_experiment(models, feature_subsets, data, experiment_id):
    for model in models:
        with mlflow.start_run(run_name="Run with {} model".format(model), experiment_id=experiment_id):
            for subset in feature_subsets:
                with mlflow.start_run(run_name="Features {}".format(subset), experiment_id=experiment_id, nested=True):
                    X = data[subset]
                    y = data['target']

                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                    param_grid = {}

                    if type(model) == type(LogisticRegression()):
                        param_grid = {'C': [0.1, 1, 10], 'max_iter': [150, 200]}
                    elif type(model) == type(SVC()):
                        param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
                    elif type(model) == type(KNeighborsClassifier()):
                        param_grid = {'n_neighbors': [3, 5, 7]}

                    best_model, best_params = train_model(model, X_train, y_train, param_grid)
                    metrics = evaluate_model(best_model, X_test, y_test)
                    model_signature = infer_signature(X_train, y_train, params=best_params)

                    dataset: PandasDataset = mlflow.data.from_pandas(data)
                    mlflow.log_input(dataset, context="whole dataset")
                    mlflow.log_params(best_params)
                    mlflow.log_metrics(metrics)		    		  	 
                    mlflow.sklearn.log_model(sk_model=best_model,artifact_path="models",signature=model_signature,registered_model_name=f"{model} model")


dataset = load_data()
feature_subsets=[dataset.columns[[0,1]].tolist(),dataset.columns[[2,3]].tolist(),
dataset.columns[[0,3]].tolist(),dataset.columns[[1,2]].tolist(),dataset.columns[[0,2,3]].tolist()]

logreg = LogisticRegression()
svm = SVC()
knn = KNeighborsClassifier()
models = [logreg, svm, knn]

experiment_id = create_mlflow_experiment(
    experiment_name="Iris classification using MLFlow",
    artifact_location="iris_artifact",
    tags={"env": "dev", "version": "1.0.0"},
)

experiment = get_mlflow_experiment(experiment_id=experiment_id)

perform_experiment(models, feature_subsets, dataset, experiment_id)
print("Training is completed")




