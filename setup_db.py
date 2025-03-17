import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_database(
    db_name, user="postgres", password="yourpassword", host="localhost", port="5432"
):
    conn = psycopg2.connect(user=user, password=password, host=host, port=port)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE {db_name};")
    cursor.close()
    conn.close()


def create_tables():
    conn = psycopg2.connect(
        dbname="kilimodata", user="postgres", password="yourpassword", host="localhost"
    )
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS counties (
        id INT PRIMARY KEY,
        name VARCHAR(255)
    );

    CREATE TABLE IF NOT EXISTS institutions (
        id INT PRIMARY KEY,
        name VARCHAR(255)
    );

    CREATE TABLE IF NOT EXISTS subsectors (
        id INT PRIMARY KEY,
        name VARCHAR(255)
    );
    -- Add tables similarly for domains, subdomains, elements, itemcategories, items, units, and kilimodata
    """
    )

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    create_database("kilimodata")
    create_tables()
