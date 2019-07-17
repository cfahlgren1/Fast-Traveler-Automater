from FastTraveler import FastTraveler

jira_issue = FastTraveler('ASOC-1813') # example with jira object with all locations
print (jira_issue) # print jira object

for location in jira_issue.locations: # loop through locations
    print (str(location) + "\n")
