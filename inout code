import sqlite3
import schedule
import time
from datetime import datetime
from sense_hat import SenseHat

# SQLite database file and table name
db_file = "sensors.db"
table_name = "READINGS"

# Create a connection to the database file
conn = sqlite3.connect(db_file)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the READINGS table if it doesn't exist
cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    SENSOR_ID INTEGER NOT NULL,
                    TEMPERATURE REAL NOT NULL,
                    HUMIDITY REAL NOT NULL,
                    PRESSURE REAL NOT NULL,
                    DT TEXT NOT NULL
                    );''')

# Initialize the sensor_id counter
sensor_id = 1

def log_sensor_data():
    global sensor_id
    # Get sensor data
    sense = SenseHat()
    temp = round(sense.get_temperature(), 2)
    humidity = round(sense.get_humidity(), 2)
    pressure = round(sense.get_pressure(), 2)
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    # Insert sensor data into the READINGS table
    insert_statement = f"INSERT INTO {table_name} (SENSOR_ID, TEMPERATURE, HUMIDITY, PRESSURE, DT) VALUES (?, ?, ?, ?, ?);"
    values = (sensor_id, temp, humidity, pressure, dt_string)
    cursor.execute(insert_statement, values)

    # Increment the sensor_id counter
    sensor_id += 1

    # Save changes and close the connection
    conn.commit()

# Schedule the log_sensor_data function to run every 5 minutes
schedule.every(5).seconds.do(log_sensor_data)

# Infinite loop to run scheduled tasks
while True:
    # Run any pending scheduled tasks
    schedule.run_pending()
    # Sleep for 1 second
    time.sleep(1)

