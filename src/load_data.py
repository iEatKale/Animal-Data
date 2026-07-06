import pandas as pd;

def load_file(file_path, separator = ","):
    df = pd.read_csv(file_path, sep = separator)
    return df

