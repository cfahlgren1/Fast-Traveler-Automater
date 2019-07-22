from jira import JIRA
from MongoCRUD import MongoCRUD
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

x = 0  # incrementer
mongo = MongoCRUD('ft_data')
for issue in jira.search_issues('issuetype = "Fast Traveler"', maxResults=2000):
    x += 1
    fast_traveler = FastTraveler(issue.key)
    if mongo.check_exists(fast_traveler.key):
        print("skipping   " + str(fast_traveler.key))
    else:
        for coordinates in fast_traveler.locations:
            key = fast_traveler.key
            user = fast_traveler.reporter
            ft_type = "Fast Traveler"
            date = fast_traveler.created_date
            description = fast_traveler.description
            print (str(x) + "\tAdded: " + str(user) + "\t" + str(key) + "\t" + str(date) + "\t" + str(coordinates))
            mongo.write(user, key, ft_type, date, description, coordinates)

mongo.close()
print (x)