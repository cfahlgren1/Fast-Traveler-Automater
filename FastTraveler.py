from jira import JIRA
from IP import IP
from MongoCRUD import MongoCRUD
from participants import getDictionary
from dotenv import load_dotenv
from datetime import datetime as dt
import os, urllib3

# Class that Holds Fast Traveler Information
# @author Caleb Fahlgren
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
        self.logging_db = MongoCRUD('logging')
        self.issue = self.jira.issue(issue_name)
        self.key = self.issue.key
        self.report_display_name = self.issue.fields.reporter.displayName
        self.reporter = self.issue.fields.reporter.name
        self.issue_type = self.issue.fields.issuetype.name
        self.assignee = self.issue.fields.assignee
        self.description = self.issue.fields.description
        self.locations = []
        self.locationInfo = self.getAddresses()
        self.created_date = dt.strptime(str(self.issue.fields.created)[:10], "%Y-%m-%d").date() # save string as python date datetime obj
        self.raw = self.issue.raw # raw json of jira issue

    # return a list of object values for ip address that holds ip info
    def getAddresses(self):
        ip_addresses = []
        ip_address_objects = [] # list of IP objects

        description = self.issue.fields.description  # grab description
        for line in description.splitlines():  # loop through all lines in description
            if line.startswith('First IP:') or line.startswith(('Next IP:')):  # find line that starts with it provides
                for word in line.split():  # split line into array of words
                    if word[0].isdigit(): # if it is an ip address add to list
                        ip_addresses.append(word)
        for ip in ip_addresses:  # loop through all ip addresses returned
            try:
                location_info = IP(ip)  # create object from ip address
                self.locations.append([float(location_info.longitude), float(location_info.latitude)])
                ip_address_objects.append(location_info)  # append to list
            except Exception as e:
                location_info = "n/a"
        return ip_address_objects

    # assign jira issue to specified author
    def assign(self, author):
        try:
            self.jira.assign_issue(self.jira.issue(self.key), author)
            self.logging_db.write(self.key, 'assigned')  # note that an issue has been resolved
        except:
            print ('error: could not assign specified user: ' + author)

    # resolve fast traveler
    def resolve(self):
        try:
            self.jira.transition_issue(self.issue, '761')
            self.logging_db.write(self.key, 'resolved')# note that an issue has been resolved
        except Exception as e:
            print(str(e))

    # send email to customer
    def email(self):
        try:
            self.jira.transition_issue(self.key, '951')
            self.logging_db.write(self.key, 'emailed')  # note that an issue has been resolved
        except Exception as e:
            print (str(e))

    # delete jira issue
    def delete(self):
        try:
            self.issue.delete()
            self.logging_db.write(self.key, 'deleted')  # note that an issue has been resolved
        except:
            print('error could not delete issue')

    # add participants from description to the participants field in jira
    def addParticipants(self):
        if self.issue_type == 'Fast Traveler':
            usernames = []
            description = self.issue.fields.description # grab description
            for line in description.splitlines(): # loop through all lines in description
                if line.startswith('IT Providers:'): # find line that starts with it provides
                    for word in line.split(): # split line into array of words
                        if word.endswith('@auburn.edu') or word.endswith('@auburn.edu,'):
                            word = word.replace(',', '')
                            usernames.append(word.replace('@auburn.edu', ''))

            if getDictionary(usernames) != False: # make sure there are emails to add
                self.issue.update(fields={'customfield_10000': getDictionary(usernames)})
        else:
            print ('issue is not fast traveler')

    # close database
    def close(self):
        self.logging_db.close()

    # string method for string representation of object
    def __str__(self):
        return "key: " + str(self.key) + "\nreporter: "  + str(self.reporter) \
               + "\ncreated: " + str(self.created_date) + "\nissue_type: " + str(self.issue_type) \
               + "\nassignee: " + str(self.assignee) + "\ndescription: " + str(self.description)

    # for use when printing from list
    def __repr__(self):
        return str(self)



