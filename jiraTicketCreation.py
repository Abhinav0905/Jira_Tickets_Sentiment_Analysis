# make a program to create some Jira Ticket using Jira API and Python 

import requests
import json
from requests.auth import HTTPBasicAuth
from jira import JIRA
import os

# Jira API URL
Jira_URL = "https://sreeniabhinav.atlassian.net"
Jira_Username = "richagupta361@gmail.com"
Jira_Password = "ATATT3xFfGF0lzNQVBqrPEi-71s25irNsDokviyKJ1z4hBlAAFTlFe5xFzyjyybnRsCiyoOKgwElC8yIjzcVx0LNy_C2UIICnvWooY6yU5n9bljF2EwcU9UTG4DeEFK4QeGZ3IQV-f07bG_Ryh7CSx58OWjTDQ5b4y102fwKcQOvryw_w8zJ-M8=E59C2200"

# Jira Ticket Creation

class JiraTicketCreation:
    def __init__(self):
        self.jira = JIRA(server=Jira_URL, basic_auth=(Jira_Username, Jira_Password))

    def create_jira_ticket(self):
        issue = self.jira.create_issue(project='AIP', summary='Test Ticket', description='This is a test ticket', issuetype={'name': 'Task'})
        print(issue)

def create_jira_ticket():
    url = Jira_URL + "/rest/api/3/issue"
    username = Jira_Username
    password = Jira_Password
    auth = HTTPBasicAuth(username, password)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "fields": {
        "project": {
            "key": "AIP"
        },
        "summary": "Test Ticket",
        "description": "This is a test ticket",
        "issuetype": {
            "name": "Task"
        }
        }
    }
    response = requests.post(url, headers=headers, auth=auth, data=json.dumps(data))
    print(response.text)

jira_ticket_creator = JiraTicketCreation()
jira_ticket_creator.create_jira_ticket()


# Function to create a Jira ticket with given summary and description
def create_critical_issue(summary, description):
    jira_ticket_creator.jira.create_issue(
        project='AIP',
        summary=summary,
        description=description,
        issuetype={'name': 'Task'}
    )

# List of critical issues to create
critical_issues = [
    {"summary": "Critical: API Down", "description": "Server is not responding."},
    {"summary": "Critical: 404 Issue", "description": "Bad reqeust Detected."},
    {"summary": "Critical: Server Not responding", "description": "Server Down Internal Error."}
]

# Create Jira tickets for each critical issue
for issue in critical_issues:
    create_critical_issue(issue['summary'], issue['description'])