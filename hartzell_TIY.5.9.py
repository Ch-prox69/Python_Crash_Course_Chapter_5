usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, get to work please")
else:
    print("We need to find some users!")