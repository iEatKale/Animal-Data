# Anymal-Data

Anymal-Data is a Python data pipeline project for cleaning, processing, and analysing animal observation data.

The project takes a raw animal dataset, performs data cleaning and standardisation, saves the cleaned data in CSV and Excel formats, and then applies machine learning techniques to explore the cleaned dataset.

The machine learning section currently includes:

- classification
- regression
- clustering

## Project Overview

The project is split into two main parts:

```text
Data Engineering
```

This part focuses on loading, inspecting, cleaning, and saving the dataset.

```text
Machine Learning
```

This part applies machine learning models to the cleaned dataset.

The current ML tasks are:

```text
Classification → predict animal_type
Regression     → predict body_length_cm
Clustering     → group animals based on physical measurements
```

## Folder Structure

```text
Anymal-Data/
│
├── data/
│   ├── input/
│   │   └── animal_data.csv
│   │
│   └── output/
│       ├── csv/
│       │   └── cleaned_animal_data.csv
│       │
│       ├── excel/
│       │   └── cleaned_animal_data.xlsx
│       │
│       └── ml/
│           ├── classification_report.txt
│           ├── regression_report.txt
│           └── clustering_report.txt
│
├── docs/
│   ├── cleaning_log.md
│   ├── classification_log.md
│   ├── regression_log.md
│   └── clustering_log.md
│
├── src/
│   ├── data_engineering/
│   │   ├── __init__.py
│   │   ├── clean_data.py
│   │   ├── inspect_data.py
│   │   ├── load_data.py
│   │   └── save_data.py
│   │
│   └── ml/
│       ├── __init__.py
│       ├── ml_preprocessing.py
│       ├── ml_classification.py
│       ├── ml_regression.py
│       └── ml_clustering.py
│
├── main.py
├── README.md
└── requirements.txt
```

## Dataset

The raw dataset is stored in:

```text
data/input/animal_data.csv
```

The dataset contains animal observation records with fields such as:

```text
animal type
country
weight
body length
gender
latitude
longitude
observation date
data compiler
```

The raw dataset includes issues such as:

- missing values
- duplicate records
- inconsistent animal names
- inconsistent country names
- invalid or unusual numeric values
- unnecessary columns
- inconsistent column formatting

## Data Cleaning

The cleaning pipeline performs several steps, including:

- standardising column names
- removing duplicate records
- removing unnecessary columns
- correcting inconsistent animal type values
- correcting inconsistent country values
- removing rows with missing key values
- removing invalid weight and body length values
- converting observation dates into a consistent format
- saving the cleaned dataset

The cleaned dataset is saved as:

```text
data/output/csv/cleaned_animal_data.csv
data/output/excel/cleaned_animal_data.xlsx
```

More detail about the cleaning process is documented in:

```text
docs/cleaning_log.md
```

## Machine Learning

After cleaning, the project applies machine learning to the cleaned dataset.

### Classification

The classification task predicts:

```text
animal_type
```

using features such as:

```text
country
weight_kg
body_length_cm
gender
latitude
longitude
```

A `RandomForestClassifier` was used for this task.

The classification model achieved:

```text
Accuracy: 1.0000
```

The full classification documentation is available in:

```text
docs/ml_classification.md
```

The classification report is saved to:

```text
data/output/ml/classification_report.txt
```

### Regression

The regression task predicts:

```text
body_length_cm
```

using features such as:

```text
animal_type
country
weight_kg
gender
latitude
longitude
```

A `RandomForestRegressor` was used for this task.

The regression model is evaluated using:

```text
Mean Absolute Error
Root Mean Squared Error
R2 Score
```

The full regression documentation is available in:

```text
docs/regression_log.md
```

The regression report is saved to:

```text
data/output/ml/regression_report.txt
```

### Clustering

The clustering task groups animals without using a target label.

KMeans clustering was used with:

```text
weight_kg
body_length_cm
```

The model was set to four clusters because the dataset contains four known animal types:

```text
European Bison
Hedgehog
Lynx
Red Squirrel
```

The final clustering model achieved:

```text
Silhouette Score: 0.8848
```

The full clustering documentation is available in:

```text
docs/clustering_log.md
```

The clustering report is saved to:

```text
data/output/ml/clustering_report.txt
```

## Installation

Clone the repository and move into the project folder:

```bash
git clone <repository-url>
cd Anymal-Data
```

Create a virtual environment:

```bash
python -m venv env
```

Activate the virtual environment.

On Windows PowerShell:

```bash
.\env\Scripts\Activate.ps1
```

On Windows Command Prompt:

```bash
env\Scripts\activate
```

On macOS/Linux:

```bash
source env/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Requirements

The project uses:

```text
pandas
openpyxl
scikit-learn
numpy
```

These should be listed in `requirements.txt`.

## Running the Project

The project can be run from `main.py`.

The script supports three modes:

```bash
python main.py clean
python main.py ml
python main.py all
```

### Run the Cleaning Pipeline Only

```bash
python main.py clean
```

This loads the raw dataset, cleans it, inspects the results, and saves the cleaned files.

Outputs:

```text
data/output/csv/cleaned_animal_data.csv
data/output/excel/cleaned_animal_data.xlsx
```

### Run the Machine Learning Pipeline Only

```bash
python main.py ml
```

This loads the already cleaned CSV file and runs the machine learning models.

Outputs:

```text
data/output/ml/classification_report.txt
data/output/ml/regression_report.txt
data/output/ml/clustering_report.txt
```

This command does not regenerate the cleaned CSV or Excel files.

### Run Everything

```bash
python main.py all
```

This runs both the cleaning pipeline and the machine learning pipeline.

It performs the full process:

```text
raw data → cleaned data → machine learning reports
```

## Recommended Workflow

If running the project for the first time:

```bash
python main.py clean
python main.py ml
```

Or run everything at once:

```bash
python main.py all
```

If the cleaned dataset already exists and only the ML models need to be rerun:

```bash
python main.py ml
```

## Output Files

### Cleaned Data

```text
data/output/csv/cleaned_animal_data.csv
data/output/excel/cleaned_animal_data.xlsx
```

### Machine Learning Reports

```text
data/output/ml/classification_report.txt
data/output/ml/regression_report.txt
data/output/ml/clustering_report.txt
```

### Documentation

```text
docs/cleaning_log.md
docs/classification_log.md
docs/regression_log.md
docs/clustering_log.md
```

## Summary

This project demonstrates a complete data workflow:

```text
1. Load raw animal observation data
2. Inspect the dataset
3. Clean and standardise the data
4. Save cleaned outputs
5. Apply classification, regression, and clustering models
6. Save machine learning reports
7. Document the full process
```

The project shows how raw data can be transformed into a clean, machine-learning-ready dataset and then used for different types of analysis.