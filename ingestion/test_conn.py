
import snowflake.connector

from config.config import (
    SNOWFLAKE_ACCOUNT,
    SNOWFLAKE_USER,
    SNOWFLAKE_PASSWORD,
    SNOWFLAKE_WAREHOUSE,
    SNOWFLAKE_DATABASE,
    SNOWFLAKE_SCHEMA,
    SNOWFLAKE_ROLE
)

print("Account   :", SNOWFLAKE_ACCOUNT)
print("Warehouse :", SNOWFLAKE_WAREHOUSE)
print("Database  :", SNOWFLAKE_DATABASE)
print("Schema    :", SNOWFLAKE_SCHEMA)
print("Role      :", SNOWFLAKE_ROLE)

conn = None
cursor = None

try:
    conn = snowflake.connector.connect(
        account=SNOWFLAKE_ACCOUNT,
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA,
        role=SNOWFLAKE_ROLE
    )

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            CURRENT_ROLE(),
            CURRENT_WAREHOUSE(),
            CURRENT_DATABASE(),
            CURRENT_SCHEMA()
    """)

    result = cursor.fetchone()

    print("\nSnowflake connection successful!")
    print("--------------------------------")
    print("Role      :", result[0])
    print("Warehouse :", result[1])
    print("Database  :", result[2])
    print("Schema    :", result[3])

except snowflake.connector.Error as e:
    print("Snowflake Response:", result[0])

finally:
    if cursor is not None:
        cursor.close()

    if conn is not None:
        conn.close()