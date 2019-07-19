# Jira Fast Traveler

Python classes that hold Fast Traveler Issues in Jira as objects. With these objects you can run a variety of methods that perform different actions such as:

- Emailing a Fast Traveler to Participants and Customers
- Assign ticket to user
- Resolving a Ticket
- Deleting a Ticket
- Getting location information from IP addressed parsed from Fast Traveler description
- Return Fast Traveler fields such as:
	- Assignee
	- Description
	- Issue Key
	- Reporter Name
	- Description
	- Created Time
	-  Raw JSON of all fields


# Fast Traveler Emailer

A script built on top of the Fast Traveler classes that automates assigning issue to user, adding request participants, and emailing users.

# Example Code that works on Fast Traveler
edit .env field to include JIRA_USERNAME and JIRA_PASSWORD and SERVER_ADDRESS

    from FastTraveler import FastTraveler
    jira_issue = FastTraveler('ASOC-813')
    print (jira_issue.assignee) 
    print (jira_issue.description)
    print (jira_issue.created_time)
    print (jira_issue.raw)
    print (jira_issue.issue_type)
    jira_issue.resolve() # resolve issue
    jira_issue.assign('cdf0022') # assign to user cdf0022
    jira_issue.addParticipants() # add participants from description
    jira_issue.email() # email user and participants
    print (jira_issue.locations) # print jira location info from IP Addresses
     

