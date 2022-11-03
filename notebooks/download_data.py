# Databricks notebook source
dbutils.widgets.text("kaggle_username", "")
dbutils.widgets.text("kaggle_api_key", "")
dbutils.widgets.text("kaggle_dataset", "brenda89/fifa-world-cup-2022")
dbutils.widgets.text("download_dir", "/dbfs/world_cup_2022/")

# COMMAND ----------

# MAGIC %pip install kaggle

# COMMAND ----------

import os, json, subprocess

def create_kaggle_conf(username, api_key):
  
  kaggle_dir = os.path.join(os.path.expandvars("$HOME"), ".kaggle")
  os.makedirs(kaggle_dir, exist_ok = True)
  conf = {"username": username, "key": api_key}
  with open(f"{kaggle_dir}/kaggle.json", "w", encoding='utf-8') as f:
    json.dump(conf, f)

# COMMAND ----------

import kaggle

def init_kaggle(username, api_key):
  
  create_kaggle_conf(username, api_key)
  return kaggle.api

# COMMAND ----------

def download_dataset(username, api_key, dataset, path):
  
  os.makedirs(path, exist_ok = True)
  kaggle = init_kaggle(username, api_key)
  kaggle.dataset_download_files(dataset, path=path, unzip=True)

# COMMAND ----------

download_dataset(dbutils.widgets.get("kaggle_username"), dbutils.widgets.get("kaggle_api_key"), dbutils.widgets.get("kaggle_dataset"), dbutils.widgets.get("download_dir"))

# COMMAND ----------

dbutils.fs.ls("dbfs:/world_cup_2022/")
