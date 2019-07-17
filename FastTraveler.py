from jira import JIRA
from dotenv import load_dotenv
import os, urllib3, IP

class FastTraveler(object):
    try:
        load_dotenv()  # setup use for getting environment variables

        # ignore warning from invalid certificate, allan needs to fix
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # jira = JIRA('https://jira.atlassian.com')
        jira = JIRA(basic_auth=(os.getenv('JIRA_USERNAME'), os.getenv('JIRA_PASSWORD')),
                    options={'server': os.getenv('SERVER_ADDRESS'), 'verify': False})
    except:
        print ("jira connection error occurred, please verify env variables")

    # initialize variables from jira
    def __init__(self, issue_name):
        issue = self.jira.issue(issue_name)
        key = issue.key
        report_display_name = issue.fields.reporter.displayName
        reporter_name = issue.fields.reporter.name
        issue_type = issue.fields.issuetype.name
        assignee = issue.fields.assignee
        description = issue.fields.description
        locations = self.getAddresses()

    # return a list of object values for ip address that holds ip info
    def getAddresses(self, description):
        ip_address_objects = []
        # do stuff
        # and get both ip addresses from description

        ip_addresses = []
        for ip in ip_addresses: # loop through all ip addresses returned
            location_info = IP(ip) # create object from ip address
            ip_address_objects.append(location_info) # append to list

        return ip_address_objects;





