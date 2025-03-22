def clean_dataframe(df):
    """
    Cleans a DataFrame by performing several preprocessing steps.

    The function removes duplicate rows, filters out rows with null values in the "id" column,
    converts the "id" column to integers, and trims whitespace from string columns.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to be cleaned.

    Returns
    -------
    pandas.DataFrame
        A cleaned DataFrame with duplicates removed, null "id" rows removed,
        "id" column converted to integers, and trimmed string columns.
    """

    df = df.drop_duplicates()
    df = df[df["id"].notnull()]
    df["id"] = df["id"].astype(int)
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].str.strip()
    return df


def transform_all(data_dict):
    """
    Transforms all dataframes in the given dictionary by cleaning them.

    This function iterates over each DataFrame in `data_dict`, applies the
    `clean_dataframe` function to clean the data, and returns a new dictionary
    with the cleaned DataFrames.

    Parameters
    ----------
    data_dict : dict
        A dictionary where each key is a string and each value is a pandas
        DataFrame that needs to be cleaned.

    Returns
    -------
    dict
        A dictionary with the same keys as `data_dict`, but with each DataFrame
        cleaned and transformed.
    """

    cleaned_data = {}
    for key, df in data_dict.items():
        cleaned_data[key] = clean_dataframe(df)
    return cleaned_data


if __name__ == "__main__":
    from farm.pipeline.extract import extract_all

    data_dict = extract_all()
    cleaned_data = transform_all(data_dict)
    for key, df in cleaned_data.items():
        print(f"{key} cleaned: {len(df)} records.")
