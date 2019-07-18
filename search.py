from jira import JIRA
from FastTraveler import FastTraveler
from dotenv import load_dotenv
import os, urllib3

try:
    load_dotenv()  # setup use for getting environment variables

    # ignore warning from invalid certificate, allan needs to fix
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # jira = JIRA('https://jira.atlassian.com')
    jira = JIRA(basic_auth=(os.getenv('JIRA_USERNAME'), os.getenv('JIRA_PASSWORD')),
                options={'server': os.getenv('SERVER_ADDRESS'), 'verify': False})
except:
    print("jira connection error occurred, please verify env variables")

participants = {}
# ex. find all open fast travelers and return as string
for issue in jira.search_issues('issuetype = "Fast Traveler"', maxResults=200):
    if (len(issue.raw.get('fields').get('customfield_10000')) > 0):
        for field in issue.raw.get('fields').get('customfield_10000'):
            email = field.get('key')
            jira_str = field
            participants.update({email : jira_str})

print (participants)
