def inspect_data(df):
    print ("First 5 rows:")
    print (df.head())

    print ("Data shape:")
    print (df.shape)

    print ("Column information:")
    print (df.info())

    print ("Missing values:")
    print (df.isnull().sum())

    print ("Duplicate records:")
    print (df.duplicated().sum())

    print ("Numeric summary:")
    print (df.describe())

    print ("Text column value counts:")
    text_columns = df.select_dtypes(include=["object", "string"]).columns
    for col in text_columns:
        print (f"Value counts for column '{col}':")
        print (df[col].value_counts())
    