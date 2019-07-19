from jira import JIRA
from FastTraveler import FastTraveler
from dotenv import load_dotenv
import datetime, os, urllib3

try:
    load_dotenv()  # setup use for getting environment variables

    # ignore warning from invalid certificate, allan needs to fix
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # jira = JIRA('https://jira.atlassian.com')
    jira = JIRA(basic_auth=(os.getenv('JIRA_USERNAME'), os.getenv('JIRA_PASSWORD')),
                options={'server': os.getenv('SERVER_ADDRESS'), 'verify': False})
except:
    print("jira connection error occurred, please verify env variables")

x = 0 # incrementer
for issue in jira.search_issues('issuetype = "Fast Traveler" AND status = "Waiting for Customer"', maxResults=200):
    x += 1
    fast = FastTraveler(issue.key)
    if (fast.created_time < datetime.datetime.now().date() - datetime.timedelta(days = 2)): # check for fast travelers before two days ago
        fast.resolve()
        print ("Resolved: " + str(fast.key) + "\t" + str(fast.created_time))
    fast.close()

print ("Finished " + str(x) + " Fast Travelers!")