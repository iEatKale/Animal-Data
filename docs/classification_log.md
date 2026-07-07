## Machine Learning

After cleaning the dataset, a machine learning classification model was trained to predict the `animal_type` column.

### Classification Task

The first machine learning task focused on classification. The goal was to predict the type of animal based on selected features from the cleaned dataset.

The target variable was:

```text
animal_type
```

The features used for prediction were:

```text
country
weight_kg
body_length_cm
gender
latitude
longitude
```

The columns `observation_date` and `data_compiled_by` were not used in this initial model. This kept the classification task focused on animal characteristics and location-based information.

### Model Used

A `RandomForestClassifier` was used for the classification task.

Random Forest was chosen because it combines multiple decision trees and makes predictions using majority voting. This makes it more stable than a single decision tree and suitable for classification problems involving both numerical and categorical features.

The model was created using:

```python
RandomForestClassifier(n_estimators=100, random_state=42)
```

In this model:

- `n_estimators=100` means the forest uses 100 decision trees.
- `random_state=42` makes the results reproducible each time the code is run.

### Preprocessing

The dataset contained both numerical and categorical features.

Numerical features were passed directly into the model:

```text
weight_kg
body_length_cm
latitude
longitude
```

Categorical features were encoded using `OneHotEncoder`:

```text
country
gender
```

One-hot encoding converts text categories into numerical columns so that the model can process them. For example, countries such as `Poland`, `Germany`, and `Austria` are converted into separate binary columns.

A machine learning pipeline was used to combine preprocessing and model training into one workflow.

### Train/Test Split

The cleaned dataset was split into training and testing sets using an 80/20 split.

Stratified splitting was used so that each animal type kept a similar proportion in both the training and test sets.

The model was tested on 150 records.

### Classification Results

The Random Forest classifier achieved the following result:

```text
Accuracy: 1.0000
```

This means the model correctly classified all 150 test records.

The classification report showed perfect precision, recall, and F1-score values for all animal classes:

```text
                precision    recall  f1-score   support

European Bison       1.00      1.00      1.00        12
      Hedgehog       1.00      1.00      1.00        56
          Lynx       1.00      1.00      1.00        14
  Red Squirrel       1.00      1.00      1.00        68

      accuracy                           1.00       150
     macro avg       1.00      1.00      1.00       150
  weighted avg       1.00      1.00      1.00       150
```

### Confusion Matrix

The confusion matrix was:

```text
[[12  0  0  0]
 [ 0 56  0  0]
 [ 0  0 14  0]
 [ 0  0  0 68]]
```

The diagonal values show the correct predictions. Since all values are on the diagonal and all other values are zero, the model made no incorrect predictions.

This means:

```text
European Bison: 12 correctly classified
Hedgehog:       56 correctly classified
Lynx:           14 correctly classified
Red Squirrel:   68 correctly classified
```

### Feature Importance

Feature importance was used to understand which features contributed most to the model's predictions.

The results were:

```text
Feature                   Importance
weight_kg                  0.593476
body_length_cm             0.205676
longitude                  0.086454
latitude                   0.077332
country_Poland             0.016618
country_Germany            0.004675
country_Czech Republic     0.004158
gender_male                0.002875
country_Hungary            0.002480
country_Slovakia           0.002407
gender_female              0.002191
country_Austria            0.001105
gender_not determined      0.000554
```

The most important feature was `weight_kg`, followed by `body_length_cm`.

Together, these two features accounted for approximately 80% of the model's feature importance. This suggests that the model relied mainly on the physical size of the animals when making predictions.

### Interpretation

The model achieved 100% accuracy because the animal classes in the dataset have clearly distinct physical characteristics.

The feature importance results support this interpretation, as `weight_kg` and `body_length_cm` were by far the most influential features.

### Output

The classification results are saved to:

```text
data/output/ml/classification_report.txt
```

This file contains the model accuracy, classification report, confusion matrix, and feature importance results.