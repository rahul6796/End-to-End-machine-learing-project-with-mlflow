# End-to-End-machine-learing-project-with-mlflow

## Workflow

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update entity 
5. update the configuration manager in src config
6. update the components 
7. update the pipeline
8. update the main.py
9. update the dvc.yaml

# How to run?
### STEPS:

Clone the repository
https://dagshub.com/rahul6796/End-to-End-machine-learing-project-with-mlflow.mlflow
```bash

```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/rahul6796/End-to-End-machine-learing-project-with-mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=rahul6796 \
MLFLOW_TRACKING_PASSWORD=e5c188b020f645e002579b732ea0ff563e982b38 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/rahul6796/End-to-End-machine-learing-project-with-mlflow.mlflow

export MLFLOW_TRACKING_USERNAME=rahul6796  

export MLFLOW_TRACKING_PASSWORD=e5c188b020f645e002579b732ea0ff563e982b38

```
.