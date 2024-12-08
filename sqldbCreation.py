# Now create a postgres sql data base to store the jira ticket details

import psycopg2
from psycopg2 import Error

# Connect to the default database to create the new database
connection = psycopg2.connect(
    user    = "postgres",
    password= "Gonu@190220",
    host    = "localhost",
    port    = "5432",
    database= "postgres"
)

# Set the connection to autocommit mode
connection.autocommit = True

# Create a cursor to perform database operations
cursor = connection.cursor()

# Check if the database already exists
cursor.execute("SELECT 1 FROM pg_database WHERE datname='jira_tickets'")
exists = cursor.fetchone()
if not exists:
    # Create the new database
    cursor.execute("CREATE DATABASE jira_tickets")
    print("Database created successfully in PostgreSQL")
else:
    print("Database jira_tickets already exists")

# Close the cursor and connection to the default database
cursor.close()
connection.close()

# Connect to the new database
connection = psycopg2.connect(
    user    = "postgres",
    password= "Gonu@190220",
    host    = "localhost",
    port    = "5432",
    database= "jira_tickets"
)

# Create a cursor to perform database operations
cursor = connection.cursor()

# Create a table
create_table_query = '''CREATE TABLE jira_tickets
          (TICKET_ID INT PRIMARY KEY     NOT NULL,
          SUMMARY           TEXT    NOT NULL,
          DESCRIPTION       TEXT    NOT NULL); '''

cursor.execute(create_table_query)
connection.commit()
print("Table created successfully in PostgreSQL ")

# Close the cursor

cursor.close()

# Close the connection

connection.close()

