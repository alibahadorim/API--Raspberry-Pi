import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

# SQLite database file and table name
db_file = "sensors.db"
table_name = "READINGS"

# Define a helper function to get the last 10 sensor data row inserts from the database
def get_sensor_data():
    # Create a connection to the database file
    conn = sqlite3.connect(db_file)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Select the last 10 sensor data row inserts from the READINGS table
    select_statement = f"SELECT * FROM {table_name} ORDER BY DT DESC LIMIT 10"
    cursor.execute(select_statement)
    rows = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Create a list of dictionaries with the sensor data
    sensor_data = []
    for row in rows:
        sensor_data.append({
            'sensor_id': row[1],
            'temperature': row[2],
            'humidity': row[3],
            'pressure': row[4],
            'timestamp': row[5]
        })

    return sensor_data

# Define the '/assignment6/api/sensors' endpoint
@app.route('/assignment6/api/sensors', methods=['GET'])
def sensors():
    # Call the helper function to get the last 10 sensor data row inserts from the database
    sensor_data = get_sensor_data()

    # Return the sensor data as a JSON response
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

