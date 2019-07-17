from jira import JIRA
from IP import IP
from dotenv import load_dotenv
import os, urllib3

class FastTraveler:
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
        self.key = issue.key
        self.report_display_name = issue.fields.reporter.displayName
        self.reporter_name = issue.fields.reporter.name
        self.issue_type = issue.fields.issuetype.name
        self.assignee = issue.fields.assignee
        self.description = issue.fields.description
        self.locations = self.getAddresses("test")
        self.created_time = issue.fields.created

    # return a list of object values for ip address that holds ip info
    def getAddresses(self, description):
        ip_address_objects = []
        # do stuff
        # and get both ip addresses from description

        ip_addresses = ['131.204.144.159']
        for ip in ip_addresses:  # loop through all ip addresses returned
            location_info = IP(ip)  # create object from ip address
            ip_address_objects.append(location_info)  # append to list

        return ip_address_objects

    # string method for string representation of object
    def __str__(self):
        return "key: " + str(self.key) + "\nreporter: "  + str(self.report_display_name) \
               + "\ncreated: " + str(self.created_time) + "\nissue_type: " + str(self.issue_type) \
               + "\nassignee: " + str(self.assignee) + "\ndescription: " + str(self.description)



