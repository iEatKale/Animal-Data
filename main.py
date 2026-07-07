import sys

from src.data_engineering.load_data import load_file
from src.data_engineering.inspect_data import inspect_data
from src.data_engineering.clean_data import clean_data
from src.data_engineering.save_data import save_to_csv, save_to_excel
from src.machine_learning.ml_classification import train_classification_model
from src.machine_learning.ml_regression import train_regression_model
from src.machine_learning.ml_clustering import run_clustering_model

def run_cleaning_pipeline():
    file_path = "data/input/animal_data.csv"
    csv_output_path = "data/output//csv/cleaned_animal_data.csv"
    excel_output_path = "data/output/excel/cleaned_animal_data.xlsx"

    df = load_file(file_path, separator = ";")

    print ("Data before cleaning:")
    inspect_data(df)

    df = clean_data(df)
    print ("Data after cleaning:")
    inspect_data(df)

    save_to_csv(df, csv_output_path)
    save_to_excel(df, excel_output_path)

    print (f"\nCleaned CSV saved to: {csv_output_path}")
    print (f"Cleaned Excel saved to: {excel_output_path}")

def run_ml_pipeline():
    cleaned_file_path = "data/output/csv/cleaned_animal_data.csv"
    df = load_file(cleaned_file_path, separator = ",")

    print("Columns in loaded cleaned dataset:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())

    print("Running animal_type classification model...")
    train_classification_model(df)

    print("\nRunning body_length_cm regression model...")
    train_regression_model(df)

    print("\nRunning animal clustering model...")
    run_clustering_model(df)

def main():
    if len(sys.argv) < 2:
        print("Please choose what to run:")
        print("python main.py clean - Run the data cleaning pipeline")
        print("python main.py ml - Run the ML classification pipeline")
        print("python main.py all - Run everything")
        return
    
    command = sys.argv[1].lower()

    if command == "clean":
        run_cleaning_pipeline()
    elif command == "ml":
        run_ml_pipeline()
    elif command == "all":
        run_cleaning_pipeline()
        run_ml_pipeline()

if __name__ == "__main__":
    main()