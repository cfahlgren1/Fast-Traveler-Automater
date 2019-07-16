from jira import JIRA
from dotenv import load_dotenv
import urllib3, ipinfo, os

load_dotenv() # setup use for getting environment variables

# connect to ipinfo api to get location info from ip address
handler = ipinfo.getHandler(os.getenv("IP_ACCESS_TOKEN"))

# ignore warning from invalid certificate, allan needs to fix
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# jira = JIRA('https://jira.atlassian.com')
jira = JIRA(basic_auth=(os.getenv('JIRA_USERNAME'), os.getenv('JIRA_PASSWORD')), options={'server': os.getenv('SERVER_ADDRESS'), 'verify': False})

def getJiraFields(jira_issue):
    issue = jira.issue(jira_issue)
    print(issue.key)
    print(issue.fields.reporter.displayName)
    print(issue.fields.reporter.name)
    print(issue.fields.issuetype.name)
    print(issue.fields.assignee)
    print(issue.fields.description)

def getDistance(init_ip, final_ip):
    pass

def getIPs(description):
    pass

def getAddresses(ip_address):
    details = handler.getDetails(ip_address)
    city = details.city
    latitude = details.latitude
    longitude = details.longitude
    hostname = details.hostname
    country = details.country_name

