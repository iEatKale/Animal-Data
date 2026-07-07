### Regression Task

The second machine learning task focused on regression. Unlike classification, regression predicts a numerical value rather than a category.

The goal of this task was to predict the `body_length_cm` column using selected features from the cleaned dataset.

The target variable was:

```text
body_length_cm
```

The features used for prediction were:

```text
animal_type
country
weight_kg
gender
latitude
longitude
```

The `body_length_cm` column was not used as an input feature because it was the value the model was trying to predict.

### Model Used

A `RandomForestRegressor` was used for the regression task.

The model was created using:

```python
RandomForestRegressor(n_estimators=100, random_state=42)
```

A Random Forest Regressor works by building multiple decision trees. Each tree predicts a numerical value, and the final prediction is based on the average prediction across all trees.

This model was chosen because the relationship between animal type, weight, and body length may not be perfectly linear. A Random Forest can capture more complex patterns than a simple linear regression model.

### Preprocessing

The dataset contained both numerical and categorical features.

Numerical features were passed directly into the model:

```text
weight_kg
latitude
longitude
```

Categorical features were encoded using `OneHotEncoder`:

```text
animal_type
country
gender
```

One-hot encoding converts text categories into numerical columns so that the model can process them.

A machine learning pipeline was used to combine preprocessing and model training into one workflow.

### Train/Test Split

The cleaned dataset was split into training and testing sets using an 80/20 split.

The model was trained on the training set and evaluated on the test set. This allowed the model to be tested on records it had not seen during training.

### Evaluation Metrics

Regression models are evaluated differently from classification models. Since the model predicts a numerical value, there is no confusion matrix.

Instead, the following metrics were used:

```text
Mean Absolute Error
Root Mean Squared Error
R2 Score
```

#### Mean Absolute Error

Mean Absolute Error, or MAE, shows the average prediction error.

For this task, it shows how many centimetres away the model's predicted body length was from the actual body length on average.

For example, an MAE of `2.5` would mean the model was wrong by around 2.5 cm on average.

#### Root Mean Squared Error

Root Mean Squared Error, or RMSE, is another error metric. It gives more weight to larger errors, so it is useful for identifying whether the model made some large mistakes.

#### R2 Score

The R2 score shows how much of the variation in the target value is explained by the model.

A score close to `1.0` means the model explains most of the variation in body length.  
A score close to `0.0` means the model is not much better than predicting the average body length.  
A negative score means the model is performing poorly.

### Feature Importance

Feature importance was used to identify which features contributed most to the model's body length predictions.

The most important features were expected to be:

```text
animal_type
weight_kg
```

This is because different animal types have different typical body length ranges, and weight is usually related to animal size.

### Interpretation

This regression task tests whether the cleaned dataset can be used to estimate an animal's body length from its physical, categorical, and location-based features.

The Random Forest Regressor was suitable because the relationship between weight and body length may vary between animal types. For example, the relationship between weight and length for a European Bison is very different from that of a Red Squirrel or Hedgehog.

### Output

The regression results are saved to:

```text
data/output/ml/regression_report.txt
```

This file contains the regression metrics and feature importance results.