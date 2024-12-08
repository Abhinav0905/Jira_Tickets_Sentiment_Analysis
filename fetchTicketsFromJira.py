# A python program to  fetch Jira Tickets using JIRA API and Python and store them in the Postgres SQL database

import psycopg2
from psycopg2 import Error
from jira import JIRA
import requests
import json
from requests.auth import HTTPBasicAuth

# Jira API URL
Jira_URL = "https://sreeniabhinav.atlassian.net"
Jira_Username = "richagupta361@gmail.com"
Jira_Password= "ATATT3xFfGF0lzNQVBqrPEi-71s25irNsDokviyKJ1z4hBlAAFTlFe5xFzyjyybnRsCiyoOKgwElC8yIjzcVx0LNy_C2UIICnvWooY6yU5n9bljF2EwcU9UTG4DeEFK4QeGZ3IQV-f07bG_Ryh7CSx58OWjTDQ5b4y102fwKcQOvryw_w8zJ-M8=E59C2200"

# Connect to the Jira API
jira = JIRA(server=Jira_URL, basic_auth=(Jira_Username, Jira_Password))

# Connect to the Postgres SQL database
connection = psycopg2.connect(
    user="postgres",
    password="Gonu@190220",
    host="localhost",
    port="5432",
    database="jira_tickets"
)

# Create a cursor to perform database operations
cursor = connection.cursor()

# Fetch all the Jira tickets

issues = jira.search_issues('project=AIP', maxResults=100)

# Insert the Jira tickets into the database
for issue in issues:
    ticket_id = issue.id
    summary = issue.fields.summary
    description = issue.fields.description

    cursor.execute("INSERT INTO jira_tickets (TICKET_ID, SUMMARY, DESCRIPTION) VALUES (%s, %s, %s) ON CONFLICT (TICKET_ID) DO NOTHING", (ticket_id, summary, description)) 

# Export the database into the CSV file

with open('/Users/kumarabhinav/Desktop/jira_tickets.csv', 'w') as f_output:
    cursor.copy_expert("COPY Jira_tickets TO STDOUT WITH CSV HEADER", f_output)
print("Data exported successfully")
# Commit the changes
connection.commit()
