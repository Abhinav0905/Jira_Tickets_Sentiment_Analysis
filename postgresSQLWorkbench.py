# Make an interface to interact with the database with CLI type commands

import psycopg2
from psycopg2 import Error
import sys

class PostgresSQLWorkbench:
    def __init__(self):
        self.connection = psycopg2.connect(
            user="postgres",
            password="Gonu@190220",
            host="localhost",
            port="5432",
            database="jira_tickets"
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        create_table_query = '''CREATE TABLE jira_tickets
                  (TICKET_ID INT PRIMARY KEY     NOT NULL,
                  SUMMARY           TEXT    NOT NULL,
                  DESCRIPTION       TEXT    NOT NULL); '''

        self.cursor.execute(create_table_query)
        self.connection.commit()
        print("Table created successfully in PostgreSQL ")

    def insert_ticket(self, ticket_id, summary, description):
        self.cursor.execute("INSERT INTO jira_tickets (TICKET_ID, SUMMARY, DESCRIPTION) VALUES (%s, %s, %s)", (ticket_id, summary, description))
        self.connection.commit()

    def fetch_all_tickets(self):
        self.cursor.execute("SELECT * FROM jira_tickets")
        tickets = self.cursor.fetchall()
        for ticket in tickets:
            print(ticket)

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

def main():
        workbench = PostgresSQLWorkbench()
        while True:
            print("1. Create Table")
            print("2. Insert Ticket")
            print("3. Fetch All Tickets")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                workbench.create_table()
            elif choice == 2:
                ticket_id = int(input("Enter Ticket ID: "))
                summary = input("Enter Summary: ")
                description = input("Enter Description: ")
                workbench.insert_ticket(ticket_id, summary, description)
            elif choice == 3:
                workbench.fetch_all_tickets()
            elif choice == 4:
                workbench.close_connection()
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Run the program and interact with the database using the CLI interface. You can create a table, insert tickets, fetch all tickets, and exit the program. This is a simple example of how you can interact with a PostgreSQL database using Python. You can extend this program to perform more complex operations on the database.    

