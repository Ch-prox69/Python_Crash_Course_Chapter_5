# 5.10 TIY
# Our lists
current_users = ['john', 'peyton', 'daniel', 'quinn', 'jacob']
new_users = ['aiden', 'brendan', 'john', 'peyton', 'matthew']

# Case sensitive
current_users_lower = [user.lower() for user in current_users]

# The for statements
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Dear {new_user}, name already taken, please use a new name.")
    else:
        print(f"Dear {new_user}, name is available, please proceed.")

