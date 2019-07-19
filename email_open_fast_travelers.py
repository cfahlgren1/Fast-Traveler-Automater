from jira import JIRA
from FastTraveler import FastTraveler
from dotenv import load_dotenv
import os, urllib3, eel

@eel.expose
def email_open_fast_travelers():
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
    for issue in jira.search_issues('issuetype = "Fast Traveler" AND status = Open', maxResults=50):
        x += 1
        fast_traveler = FastTraveler(issue.key)
        fast_traveler.assign('cdf0022')
        fast_traveler.addParticipants()
        fast_traveler.email()
        print ("Emailed Issue: " + issue.key)

    return x