import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

DBNAME = "kilimodata"

DATABASE_URI = (
    f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}'
    f'@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
)


def load_to_postgres(df, table_name):
    """
    Loads a Pandas DataFrame into a PostgreSQL database

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame to be loaded
    table_name : str
        Name of the PostgreSQL table to load into
    """
    engine = create_engine(DATABASE_URI)
    df.to_sql(table_name, engine, if_exists="append", index=False)
    print(f"{table_name} loaded successfully!")


if __name__ == "__main__":
    from extract import extract_all
    from transform import transform_all

    data_dict = extract_all()
    cleaned_data = transform_all(data_dict)

    for table, df in cleaned_data.items():
        load_to_postgres(df, table)
