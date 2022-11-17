## Predicting the 2022 World Cup with [No-code data science and machine learning](https://www.databricks.com/product/no-code-ml)

Using the [FIFA World Cup 2022 ⚽️🏆](https://www.kaggle.com/datasets/brenda89/fifa-world-cup-2022) dataset from Kaggle

### Feature Engineering

1. Check out this repo into your Databricks workspace using [Databricks Repos](https://www.databricks.com/product/repos)
2. Navigate to the [feature_engineering notebook](notebooks/feature_engineering.py) in your checked out repo
3. Enter your Databricks username in the username widget (NB - this is used to find the location of the [training data](resources/international_matches.csv) in your checked out repo. If you haven't checked it out to your home location you may need to change this part. You can also use the [download_data notebook](notebooks/download_data.py) to download the dataset directly from Kaggle
4. Run the notebook on a cluster running the latest version of the [Machine Learning Runtime](https://www.databricks.com/product/machine-learning-runtime)
5. The notebook will create a table called ```football.international_results``` which is what we're going to train our model on

### Model Training

1. Switch to Databricks [Machine Learning](https://www.databricks.com/product/machine-learning) / Experiments and Create [AutoML](https://www.databricks.com/product/automl) Experiment
2. Under Cluster select the [Machine Learning Runtime](https://www.databricks.com/product/machine-learning-runtime) cluster used above
3. Under Dataset select Browse and then select ```football.international_results```
4. Under Prediction target select ```result```
5. Under Schema you can select the features that will go into your model. De-select ```home_team_score``` and ```away_team_score``` (unless you want a model that is 100% accurate but needs you to provide the final score in order to predict the result!)
6. Expand Advanced Configuration (optional) and under Time column for training/validation/testing split select ```date```

All being well, you should see something like this:

![image](https://user-images.githubusercontent.com/43955924/202459203-3820c3b8-cbd4-4721-9af6-f10500375302.png)

Select Start AutoML to begin training your model!

### Model Inference


