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
    