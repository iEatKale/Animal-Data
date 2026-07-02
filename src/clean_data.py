def clean_data(df):
    # clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")

    # remove duplicate records
    df = df.drop_duplicates()

    # drop useless columns
    df = df.drop(columns=["animal_code", "animal_name"])

    # clean animal type symbols
    df["animal_type"] = df["animal_type"].str.replace("™" & "?", "", regex=False).str.strip()

    # clean country names
    df.loc[df["country"] == "PL", "country"] = "Poland"
    df.loc[df["country"] == "HU", "country"] = "Hungary"
    
    return df