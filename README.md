## Predicting the 2022 World Cup with [No-code data science and machine learning](https://www.databricks.com/product/no-code-ml)

Using the [FIFA World Cup 2022 ⚽️🏆](https://www.kaggle.com/datasets/brenda89/fifa-world-cup-2022) dataset from Kaggle

### Feature Engineering

1. Check out this repo into your Databricks workspace using [Databricks Repos](https://www.databricks.com/product/repos)
2. Navigate to the [feature_engineering notebook](notebooks/feature_engineering.py) in your checked out repo
3. Enter your Databricks username in the username widget (NB - this is used to find the location of the [training data](resources/international_matches.csv) in your checked out repo. If you haven't checked it out to your home location you may need to change this part. You can also use the [download_data notebook](notebooks/download_data.py) to download the dataset directly from Kaggle
4. Run the notebook on a cluster running the latest version of the [Machine Learning Runtime](https://www.databricks.com/product/machine-learning-runtime)
5. The notebook will create a table called ```football.international_results``` which is what we're going to train our model on

### Model Training


### Model Inference


