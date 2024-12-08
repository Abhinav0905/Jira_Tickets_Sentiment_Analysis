# make a program to do Sentiment Analysis on the JIRA Tickets uinsg Python and textBlob using Tickets stored in the Postgres SQL database

# Import the required libraries
from textblob import TextBlob
import psycopg2
from psycopg2 import Error
import openai

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
cursor.execute("SELECT * FROM jira_tickets")
tickets = cursor.fetchall()

# Perform Sentiment Analysis on the Jira tickets

for ticket in tickets:
    summary = ticket[1]
    description = ticket[2]

    # Combine the summary and description
    text = summary + " " + description

    # Perform Sentiment Analysis
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    # Set up the OpenAI API key
    import os
    openai.api_key = ""
    # Define a function to get sentiment using OpenAI
    def get_sentiment(text):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Analyze the sentiment of the following text:"}, {"role": "user", "content": text}],
            max_tokens=1080
        )
        sentiment = response.choices[0].message['content'].strip()
        return sentiment
        return sentiment

    # Replace TextBlob sentiment analysis with OpenAI sentiment analysis
    sentiment = get_sentiment(text)

    # Print the sentiment
    print(f"Summary: {summary}")
    print(f"Description: {description}")
    print(f"Sentiment: {sentiment}")
    print("\n") 

# Close the cursor and connection
cursor.close()
connection.close()

# Run the program to perform Sentiment Analysis on the Jira tickets stored in the Postgres SQL database. The program fetches the tickets, combines the summary and description, performs Sentiment Analysis using TextBlob, and prints the sentiment of each ticket. You can further analyze the sentiment data to gain insights into the overall sentiment of the tickets.


