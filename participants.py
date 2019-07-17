participants = {  # key value dictionary paired between username and custom_field_text
    "spinkca": {'self': 'https://socsd.auburn.edu:8443/rest/api/2/user?username=SPINKCA', 'name': 'SPINKCA',
                'key': 'spinkca',
                'avatarUrls': {'48x48': 'https://www.gravatar.com/avatar/c1e97724f9dd1cf3d3eda9a72c2e87b6?d=mm&s=48',
                               '24x24': 'https://www.gravatar.com/avatar/c1e97724f9dd1cf3d3eda9a72c2e87b6?d=mm&s=24',
                               '16x16': 'https://www.gravatar.com/avatar/c1e97724f9dd1cf3d3eda9a72c2e87b6?d=mm&s=16',
                               '32x32': 'https://www.gravatar.com/avatar/c1e97724f9dd1cf3d3eda9a72c2e87b6?d=mm&s=32'},
                'displayName': 'Cynthia Philpot', 'active': True, 'timeZone': 'America/Chicago'}
}

# if username exists return value of dictionary
def getDictionary(usernames):
    if len(usernames) == 0:
        return False
    custom_fields = []
    for username in usernames:
        if username in participants:
            custom_fields.append(participants[username])
    return custom_fields
