# Kilimostat Data Pipeline Documentation

This repository demonstrates a robust and automated ETL (Extract, Transform, Load) pipeline using **Python**, **Dagster**, and **PostgreSQL**.

---

## Project Overview

This ETL pipeline automatically:

1. Fetches data from various API endpoints.
2. Cleans and transforms the data using Pandas.
3. Loads data into a PostgreSQL database (`kilimodata`).
4. Automates and schedules the pipeline execution with Dagster.

---

## Project Setup

### ① **Database Setup (PostgreSQL)**

First, set up your PostgreSQL database:

```sql
CREATE DATABASE kilimodata OWNER "yourname";

-- Grant permissions explicitly to postgres user (optional):
GRANT ALL PRIVILEGES ON DATABASE kilimodata TO postgres;
```

---

## Environment Setup

### Install Dependencies

```bash
pip install dagster dagit pandas sqlalchemy psycopg2-binary python-dotenv requests
```

### Configure Environment Variables (`.env`)

Create a `.env` file in your project root:

```env
DB_USER=yourname
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
DB_NAME=kilimodata
```

---

## Pipeline Structure

Your Dagster pipeline (`pipeline.py`) contains three main steps:

- **Extract:** Pull data from APIs.
- **Transform:** Clean and validate data.
- **Load:** Insert data into PostgreSQL.

### How to run the Dagster Pipeline

Ensure your environment is activated and variables loaded:

```bash
# Run the pipeline with Dagster
dagster dev -f pipeline.py
```

---

## Running the Pipeline

### Quick Test

Start the Dagster web UI (Dagit):

```bash
dagster dev -f pipeline.py
```

Then open `http://localhost:3000` in your browser to visualize the pipeline execution.

---
---

## Next Steps

- Create a Django frontend to visualize and manage data clearly.
- Implement Django REST Framework for serialization and API creation.

---

Feel free to reach out with any questions or improvements!