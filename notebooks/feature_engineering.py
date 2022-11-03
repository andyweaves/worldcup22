# Databricks notebook source
import pandas as pd

pdf = pd.read_csv("/Workspace/Repos/andrew.weaver@databricks.com/worldcup22/resources/international_matches.csv")
display(pdf)

# COMMAND ----------

len(df)
