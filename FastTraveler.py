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
        self.issue = self.jira.issue(issue_name)
        self.key = self.issue.key
        self.report_display_name = self.issue.fields.reporter.displayName
        self.reporter_name = self.issue.fields.reporter.name
        self.issue_type = self.issue.fields.issuetype.name
        self.assignee = self.issue.fields.assignee
        self.description = self.issue.fields.description
        self.locations = self.getAddresses("test")
        self.created_time = self.issue.fields.created

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

    # assign jira issue to specified author
    def assign(self, author):
        try:
            self.jira.assign_issue(self.jira.issue(self.key), author)
        except:
            print ('error: could not assign specified user: ' + author)

    # resolve fast traveler
    def resolve(self):
        self.jira.transition_issue(self.key, '51')

    # send email to customer
    def email(self):
        self.jira.transition_issue(self.key, '951')

    def delete(self):
        self.issue.delete()

    def search(self):
        for issue in self.jira.search_issues('issuetype = "Fast Traveler" AND status = Open', maxResults=50):
            print('{} \t {}'.format(issue.key, issue.fields.created))

    # string method for string representation of object
    def __str__(self):
        return "key: " + str(self.key) + "\nreporter: "  + str(self.report_display_name) \
               + "\ncreated: " + str(self.created_time) + "\nissue_type: " + str(self.issue_type) \
               + "\nassignee: " + str(self.assignee) + "\ndescription: " + str(self.description)

    # for use when printing from list
    def __repr__(self):
        return str(self)



