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

### Model Deployment



### Model Inference

In order to use your model to predict the results of upcoming fixtures, you're going to need some data. I've provided some [sample inference data](resources/group_b.json) to predict the outcome of matches in Group B but you could also create your own for the matches that you want to predict. I used the following sources to gather the data required:

* [fifa.com](https://www.fifa.com/fifa-world-ranking) to get the latest world rankings and fifa points
* [Fifa Index](https://www.fifaindex.com/) to get the latest FIFA 23 player stats
* For the form and the goal related features you could either use the latest values for each team from the training data, update them manually based on the most recent fixtures or (this is what I did) start with a clean slate and have everyone going into the tournament with 0s for calendar form, goals for, goals against etc. The reason I chose this route is that in many ways the world cup is a clean slate, and just because you've been amazing in friendlies played in your local region, doesn't mean that form is representative of the teams you're going to face in the world cup. As such, for the [sample inference data](resources/group_b.json) I started out with all teams having form and goal related values of 0. After the first round of predictions, I fed the results into the second. So if you won the first game you had a form of 3 and a goals for of 2 for the second. You get the idea, lets get predicting...

1. Highlight and copy the [sample inference data](resources/group_b.json)
2. Switch to Databricks [Machine Learning](https://www.databricks.com/product/machine-learning) / Models
3. Find the model that you deployed above
4. Select Serving (Preview)
5. Under Call the model find the Request text box and paste the data copied above
6. Select Send Request

All being well, you should see something like this:

You can also navigate to the [inference notebook](notebooks/inference.py) in your checked out repo, enter the model URL and your Databricks username (again used the locate the [sample inference data](resources/group_b.json)) in the widgets provided and run the notebook

As you can see, for Group B we're predicting the following outcomes:

* England v IR Iran: **England Win**
* USA v Wales: **USA Win**
* Wales v IR Iran: **Wales Win**
* England v USA: **England Win**
* IR Iran v USA: **USA Win**
* Wales v England: **England Win**

Based on the above, the final table for Group B should look something like this:


| Team        | Points      |
| ----------- | ----------- |
| England     | 9           |
| USA         | 6           |
| Wales       | 3           |
| Iran        | 0           |

Here's hoping! :crossed_fingers:
