import psycopg2
import os
from urllib.parse import urlparse

# Get the DATABASE_URL environment variable
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://closewave_django_render_user:qygJHD3zdrO3RR1j5xyB4K985wXcRf5v@localhost:5432/closewave_django_render")

# Parse the DATABASE_URL
result = urlparse(DATABASE_URL)

# Extract connection parameters
username = result.username
password = result.password
database = result.path[1:]  # Removing the leading '/'
hostname = result.hostname
port = result.port

print(f"Connecting to database with the following parameters:\nUser: {username}\nPassword: {password}\nDatabase: {database}\nHost: {hostname}\nPort: {port}")

try:
    # Establish the connection
    conn = psycopg2.connect(
        dbname=database,
        user=username,
        password=password,
        host=hostname,
        port=port
    )
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")

# Username: closewave_django_render_user
# Password: qygJHD3zdrO3RR1j5xyB4K985wXcRf5v
# Hostname: dpg-cpid3pect0pc73fq97og-a
# Database: closewave_django_render

# import random
# import string
#
# def generate_secret_key(length=50):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(random.choice(characters) for i in range(length))
#
# print(generate_secret_key())
