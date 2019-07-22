from jira import JIRA
from FastTraveler import FastTraveler
from MongoCRUD import MongoCRUD
from dotenv import load_dotenv
import datetime, os, urllib3, eel

eel.init('web')

# method to email all open fast travelers
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

    print ("Finished " + str(x) + " Fast Travelers!")

# method to resolve tickets longer than two days ago
@eel.expose
def resolve():
    try:
        load_dotenv()  # setup use for getting environment variables

        # ignore warning from invalid certificate, allan needs to fix
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # jira = JIRA('https://jira.atlassian.com')
        jira = JIRA(basic_auth=(os.getenv('JIRA_USERNAME'), os.getenv('JIRA_PASSWORD')),
                    options={'server': os.getenv('SERVER_ADDRESS'), 'verify': False})
    except:
        print("jira connection error occurred, please verify env variables")

    x = 0  # incrementer
    for issue in jira.search_issues('issuetype = "Fast Traveler" AND status = "Waiting for Customer"', maxResults=200):
        x += 1
        fast = FastTraveler(issue.key)
        if (fast.created_date < datetime.datetime.now().date() - datetime.timedelta(
                days=2)):  # check for fast travelers before two days ago
            fast.resolve()
            print("Resolved: " + str(fast.key) + "\t" + str(fast.created_date))
        fast.close()

    print("Finished " + str(x) + " Fast Travelers!")

@eel.expose
def get_resolved():
    mongo = MongoCRUD('logging')
    resolved = mongo.get_resolved()
    mongo.close()
    return resolved

@eel.expose
def get_emailed():
    mongo = MongoCRUD('logging')
    emails = mongo.get_emailed()
    mongo.close()
    return emails

eel.start('main.html')