def generate_sample_data(df, yColumn="grav"):
    
    if(df[yColumn].isnull().any()):
        raise ValueError("missing values in column '" + yColumn + "'")
    y = df[yColumn].to_list()
    
    # getting all the columns
    new_cols = set(df.columns)
    # removing the desired column
    new_cols.remove(yColumn)
    new_cols = list(new_cols)
    X = df[new_cols]
    return X.to_numpy(), y