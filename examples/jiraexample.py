from FastTraveler import FastTraveler

jira_issue = FastTraveler('ASOC-1708') # example with jira object with all locations
jira_issue.assign('cdf0022')
jira_issue.resolve()
jira_issue.close()


