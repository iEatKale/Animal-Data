from src.load_data import load_file
from src.inspect_data import inspect_data
from src.clean_data import clean_data
from src.save_data import save_to_csv, save_to_excel

def main():
    file_path = "data/input/animal_data.csv"
    csv_output_path = "data/output//csv/cleaned_animal_data.csv"
    excel_output_path = "data/output/excel/cleaned_animal_data.xlsx"

    df = load_file(file_path)

    print ("Data before cleaning:")
    inspect_data(df)

    df = clean_data(df)
    print ("Data after cleaning:")
    inspect_data(df)

    save_to_csv(df, csv_output_path)
    save_to_excel(df, excel_output_path)

    print (f"\nCleaned CSV saved to: {csv_output_path}")
    print (f"Cleaned Excel saved to: {excel_output_path}")


if __name__ == "__main__":
    main()