# Databricks notebook source
dbutils.widgets.text(name="model_url", defaultValue="", label="model_url")
dbutils.widgets.text(name="username", defaultValue="", label="username")
dbutils.widgets.text(name="pat_secret_scope", defaultValue="", label="pat_secret_scope")
dbutils.widgets.text(name="pat_secret_key", defaultValue="", label="pat_secret_key")

username = dbutils.widgets.get("username")
model_url = dbutils.widgets.get("model_url")
pat_secret_scope = dbutils.widgets.get("pat_secret_scope")
pat_secret_key = dbutils.widgets.get("pat_secret_key")

# COMMAND ----------

import json
import pandas as pd

with open(f"/Workspace/Repos/{username}/worldcup22/resources/group_b.json") as f:
    data = json.load(f)

data = pd.json_normalize(data, record_path =["dataframe_records"])  
display(data)

# COMMAND ----------

import requests

def score_model(model_url, data):
  
  databricks_token = dbutils.secrets.get(scope=pat_secret_scope, key=pat_secret_key)
  
  headers = {
    "Authorization": f"Bearer {databricks_token}",
    "Content-Type": "application/json",
  }
  
  data_json = {"dataframe_records": data.to_dict(orient='records')}
  response = requests.request(method='POST', headers=headers, url=model_url, json=data_json)
  if response.status_code != 200:
      raise Exception(f"Request failed with status {response.status_code}, {response.text}")
  return response.json()

# COMMAND ----------

data_json = {"dataframe_records": data.to_dict(orient='records')}

# COMMAND ----------

score_model(model_url, data)
