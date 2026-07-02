def save_to_csv(df, csv_output_path):
    df.to_csv(csv_output_path, index=False)

def save_to_excel(df, excel_output_path):
    df.to_excel(excel_output_path, index=False)