#!/bin/sh

dvc init --no-scm
dvc remote add -d myremote s3://bucket-data-governance/data
dvc pull data/Iris.csv
dvc repro
dvc metrics show

tail -f /dev/null


