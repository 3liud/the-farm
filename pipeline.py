from dagster import Definitions, ScheduleDefinition, asset, define_asset_job

from extract import extract_all
from load import load_to_postgres
from transform import transform_all


# Define assets
@asset
def extracted_data():
    """
    Extracts data from all predefined APIs and returns it as a dictionary of DataFrames.

    This function serves as a Dagster asset that executes the data extraction
    process by calling the `extract_all` function.

    Returns
    -------
    dict
        A dictionary of DataFrames containing the extracted data from various sources.
    """

    return extract_all()


@asset
def transformed_data(extracted_data):
    """
    Transforms the extracted data by applying data cleaning and transformation steps.

    This function serves as a Dagster asset that executes the data transformation
    process by calling the `transform_all` function.

    Parameters
    ----------
    extracted_data : dict
        A dictionary of DataFrames containing the extracted data from various sources.

    Returns
    -------
    dict
        A dictionary of DataFrames containing the transformed data.
    """
    return transform_all(extracted_data)


@asset
def load_data_to_db(transformed_data):
    """
    Loads transformed data into a PostgreSQL database.

    This function serves as a Dagster asset that executes the data loading
    process by calling the `load_to_postgres` function.

    Parameters
    ----------
    transformed_data : dict
        A dictionary of DataFrames containing the transformed data from various sources.

    Returns
    -------
    None
    """

    for table, df in transformed_data.items():
        load_to_postgres(df, table)


# Define a job explicitly
etl_job = define_asset_job(name="daily_etl_job")

# Schedule referencing the explicit job
daily_schedule = ScheduleDefinition(
    job=etl_job,
    cron_schedule="0 0 * * *",  # Runs every midnight
)

# Properly initialize Definitions with the job and schedule
defs = Definitions(
    assets=[extracted_data, transformed_data, load_data_to_db],
    jobs=[etl_job],
    schedules=[daily_schedule],
)
