import json
import requests
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

OPENSKY_URL = "https://opensky-network.org/api/states/all"

response = requests.get(OPENSKY_URL)
response.raise_for_status()

data = response.json()

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

cursor.execute( 
"""
INSERT INTO OPENSKY_STATES_RAW (RAW_DATA)
SELECT PARSE_JSON(%s)
""",

(json.dumps(data),)

)

conn.commit()

print("Flight data loaded successfully!")

cursor.close()
conn.close()