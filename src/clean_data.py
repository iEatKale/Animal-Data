import pandas as pd

def clean_data(df):
    # clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")

    # remove duplicate records
    df = df.drop_duplicates()

    # drop useless columns
    df = df.drop(columns=["animal_code", "animal_name"])

    # clean animal type symbols
    df["animal_type"] = df["animal_type"].str.replace("™", "", regex=False).str.strip().str.lower()
    df["animal_type"] = df["animal_type"].str.replace("?", "", regex=False).str.strip().str.lower()

    # clean animal type names
    animal_type_map = {
        "red squirrell": "red squirrel",
        "red squirel": "red squirrel",
        "european bisson": "european bison",
        "european buster": "european bison",
        "european bison": "european bison",
        "lynx": "lynx",
        "hedgehog": "hedgehog",
        "ledgehod": "hedgehog",
        "wedgehod": "hedgehog",
        "red squirrel": "red squirrel"
    }

    df["animal_type"] = df["animal_type"].replace(animal_type_map)
    df["animal_type"] = df["animal_type"].str.title()

    # remove rows where animal_type is missing
    df = df.dropna(subset=["animal_type"])

    # fill length and weight with median values for each animal type
    df.loc[df["weight_kg"] <= 0, "weight_kg"] = pd.NA
    df.loc[df["body_length_cm"] <= 0, "body_length_cm"] = pd.NA

    # fill missing weight and body length using median value per animal type
    df["weight_kg"] = df.groupby("animal_type")["weight_kg"].transform(
        lambda x: x.fillna(x.median())
    )

    df["body_length_cm"] = df.groupby("animal_type")["body_length_cm"].transform(
        lambda x: x.fillna(x.median())
    )

    # remove negative lattude rows, but keep missing values 
    df = df[(df["latitude"] >= 0) | (df["latitude"].isna())]

    # clean country names
    df["country"] = df["country"].str.strip()

    country_map = {
    "PL": "Poland",
    "HU": "Hungary",
    "Hungry": "Hungary",
    "CZ": "Czech Republic",
    "DE": "Germany",
    "Czech": "Czech Republic",
    "Australia": "Austria",
    "CC": "Czech Republic"
    }

    df["country"] = df["country"].replace(country_map)

    # Fill missing gender values
    df["gender"] = df["gender"].fillna("not determined")

    # Convert observation_date to datetime
    original_dates = df["observation_date"].astype(str).str.strip()

    # parse main format
    df["observation_date"] = pd.to_datetime(
        original_dates,
        format="%d.%m.%Y",
        errors="coerce"
    )
    # parse text dates
    failed_dates = df["observation_date"].isna()

    df.loc[failed_dates, "observation_date"] = pd.to_datetime(
        original_dates[failed_dates],
        format="%d %B %Y",
        errors="coerce",
    )

    # backup format: month.day.year
    failed_dates = df["observation_date"].isna()

    df.loc[failed_dates, "observation_date"] = pd.to_datetime(
        original_dates[failed_dates],
        format="%m.%d.%Y",
        errors="coerce"
    )

    # Remove time from date
    df["observation_date"] = df["observation_date"].dt.date

    print("\nUnconverted dates:")
    print(original_dates[df["observation_date"].isna()].value_counts())

    return df
