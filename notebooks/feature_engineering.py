# Databricks notebook source
# MAGIC %pip install bamboolib --quiet

# COMMAND ----------

dbutils.widgets.text(name="username", defaultValue="", label="username")
username = dbutils.widgets.get("username")

# COMMAND ----------

import pandas as pd
import bamboolib as bam

bam
pdf = pd.read_csv(f"/Workspace/Repos/{username}/worldcup22/resources/international_matches.csv", parse_dates=["date"])
pdf

# COMMAND ----------

import pyspark.pandas as ps

df = ps.from_pandas(pdf)
df["result"] = df["home_team_result"].apply(lambda x: 0 if x == "Win" else 1 if x == "Draw" else 2 if x == "Lose" else -1)
df["fifa_rank_difference"] = df["home_team_fifa_rank"] - df["away_team_fifa_rank"]
df["fifa_points_difference"] = df["home_team_total_fifa_points"] - df["away_team_total_fifa_points"]
df["year"] = df["date"].dt.year
display(df)

# COMMAND ----------

def get_form(df, home_or_away):

  values, other = ([3, 0, 1], "away") if home_or_away == "home" else ([0, 3, 1], "home") if home_or_away == "away" else (None, None)

  df.sort_values(by=["date"], ascending=True)
  df[f"{home_or_away}_calendar_gf"] = df[f"{home_or_away}_team_score"].cumsum()
  df[f"{home_or_away}_calendar_ga"] = df[f"{other}_team_score"].cumsum()
  df[f"{home_or_away}_calendar_gd"] = df[f"{home_or_away}_calendar_gf"] - df[f"{home_or_away}_calendar_ga"]
  df[f"{home_or_away}_team_pts"] = df["home_team_result"].replace(to_replace=["Win", "Lose", "Draw"], value=values)
  df[f"{home_or_away}_form"] = df[f"{home_or_away}_team_pts"].rolling(6, min_periods=1).sum()
  df[f"{home_or_away}_calendar_pts"] = df[f"{home_or_away}_team_pts"].cumsum()
  
  return df[["date", "year", "home_team", "away_team", f"{home_or_away}_form", f"{home_or_away}_calendar_pts", f"{home_or_away}_calendar_gf", f"{home_or_away}_calendar_ga", f"{home_or_away}_calendar_gd"]]

# COMMAND ----------

home = df.groupby(["home_team", "year"]).apply(get_form, "home")
away = df.groupby(["away_team", "year"]).apply(get_form, "away")

# COMMAND ----------

results = df.merge(home, on=["date", "year", "home_team", "away_team"], how="left").merge(away, on=["date", "year", "home_team", "away_team"], how="left").drop(columns=["city", "shoot_out", "home_team_result"])
results.to_table("football.international_results", format="delta", mode="overwrite")

# COMMAND ----------

display(ps.read_table("football.international_results"))
