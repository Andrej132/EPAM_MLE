from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,recall_score,precision_score
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import joblib


def load_data(**context):
    data = pd.read_csv("/opt/airflow/dags/Iris.csv")
    context['ti'].xcom_push(key='dataset', value=data)


def clean_data(**context):
    dataset = context['ti'].xcom_pull(key='transformed_dataset')
    dataset.drop(['Id'], axis=1, inplace=True)
    dataset.drop_duplicates(inplace=True)
    dataset.fillna(dataset.mean(numeric_only=True))
    z_scores = (dataset.iloc[:, :-1] - dataset.iloc[:, :-1].mean()) / dataset.iloc[:, :-1].std()
    dataset = dataset[(z_scores < 3).all(axis=1)]
    context['ti'].xcom_push(key='cleaned_dataset', value=dataset)


def split_data(**context):
    dataset = context['ti'].xcom_pull(key='cleaned_dataset')
    X = dataset.drop(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], axis=1)
    y = dataset[['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    context['ti'].xcom_push(key='X_train', value=X_train)
    context['ti'].xcom_push(key='X_test', value=X_test)
    context['ti'].xcom_push(key='y_train', value=y_train)
    context['ti'].xcom_push(key='y_test', value=y_test)


def unsupervised_transformations(**context):
    dataset = context['ti'].xcom_pull(key='dataset')
    X = dataset.drop('Species', axis=1)
    scaler = MinMaxScaler()
    X_normalized = scaler.fit_transform(X)
    dummies = pd.get_dummies(dataset['Species'])
    dataset_with_dummies = pd.concat([pd.DataFrame(X_normalized, columns=X.columns), dummies], axis=1)
    context['ti'].xcom_push(key='transformed_dataset', value=dataset_with_dummies)


def training(**context):
    X_train = context['ti'].xcom_pull(key='X_train')
    y_train = context['ti'].xcom_pull(key='y_train')
    clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=3, min_samples_split=3)
    clf.fit(X_train, y_train)
    model_file = '/opt/airflow/dags/decision_tree_model.joblib'
    joblib.dump(clf, model_file)
    context['ti'].xcom_push(key='model_file', value=model_file)


def predicting(**context):
    X_test = context['ti'].xcom_pull(key='X_test')
    y_test = context['ti'].xcom_pull(key='y_test')
    model_file = context['ti'].xcom_pull(key='model_file')
    model = joblib.load(model_file)
    y_predictions = model.predict(X_test)
    accuracy = accuracy_score(y_predictions, y_test)
    recall = recall_score(y_predictions,y_test,average="macro")
    precision = precision_score(y_predictions,y_test,average="macro")
    context['ti'].xcom_push(key='accuracy', value=accuracy)
    context['ti'].xcom_push(key='recall', value=recall)
    context['ti'].xcom_push(key='precision', value=precision)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
        'decision-tree-training',
        default_args=default_args,
        description='Training using DAG',
        schedule=timedelta(days=1),
        start_date=datetime(2024, 4, 25),
        catchup=False,
        tags=['example'],

) as dag:
    load_dataset = PythonOperator(
        task_id='loading',
        python_callable=load_data
    )
    transformations = PythonOperator(
        task_id='transformations',
        python_callable=unsupervised_transformations
    )
    clean_dataset = PythonOperator(
        task_id='cleaning',
        python_callable=clean_data
    )
    split_dataset = PythonOperator(
        task_id='splitting',
        python_callable=split_data
    )
    train = PythonOperator(
        task_id='training',
        python_callable=training
    )

    predict = PythonOperator(
        task_id='predicting',
        python_callable=predicting
    )

    load_dataset >> transformations >> clean_dataset >> split_dataset >> train >> predict




