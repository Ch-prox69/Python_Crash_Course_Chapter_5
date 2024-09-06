usernames = ['admin', 'john', 'peter', 'jack', 'matthew']
for user in usernames:
    if user == 'admin':
        print(f"Hello {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, get to work please")
