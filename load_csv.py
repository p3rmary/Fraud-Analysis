import pandas as pd
from sqlalchemy import create_engine
from io import StringIO

DB_USER = 'postgres'
DB_PASSWORD = 'Mmerichukwu1738'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'Fraud Analysis'
SCHEMA_NAME = 'public'

CSV_FILE = r"AIML Dataset.csv"


def load_csv_to_postgres():
    print("Starting data import...")
    print(f"Reading CSV file: {CSV_FILE}\n")

    connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = create_engine(connection_string)

    try:
        df = pd.read_csv(CSV_FILE)
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

        table_name = CSV_FILE.replace('.csv', '').lower().replace(' ', '_')

        print(f"Rows: {len(df)} | Columns: {list(df.columns)}\n")

        # Step 1: Create table structure
        print("Creating table structure...")
        df.head(0).to_sql(
            name=table_name,
            con=engine,
            schema=SCHEMA_NAME,
            if_exists='replace',
            index=False
        )

        # Step 2: Bulk load via COPY
        print("Bulk loading data via COPY...")
        buffer = StringIO()
        df.to_csv(buffer, index=False, header=False)
        buffer.seek(0)

        conn = engine.raw_connection()
        try:
            cur = conn.cursor()
            cur.copy_expert(
                f"COPY {SCHEMA_NAME}.{table_name} FROM STDIN WITH CSV",
                buffer
            )
            cur.close()
            conn.commit()
        finally:
            conn.close()

        print(f"\nDone! → {SCHEMA_NAME}.{table_name} ({len(df)} rows imported)")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        engine.dispose()


if __name__ == "__main__":
    try:
        load_csv_to_postgres()
    except Exception as e:
        print(f"\nFatal error: {str(e)}")
        print("\nMake sure:")
        print("  1. PostgreSQL is running")
        print("  2. Database and schema exist")
        print("  3. Credentials are correct")
        print("  4. Required packages installed: pip install pandas sqlalchemy psycopg2-binary")