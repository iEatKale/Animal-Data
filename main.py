from src.load_data import load_file
from src.inspect_data import inspect_data

def main():
    file_path = "data/input/animal_data.csv"

    df = load_file(file_path)
    inspect_data(df)

if __name__ == "__main__":
    main()