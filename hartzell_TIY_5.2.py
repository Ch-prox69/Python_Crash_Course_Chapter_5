# 5.2
candy = 'Snickers'
producer = 'Mars'
price = 4

# 1. Tests for equality and inequality with strings
print("Is candy == 'Snickers'? I predict True.")
print(candy == 'Snickers')

print("\nIs candy == 'Candy Corn'? I predict False.")
print(candy == 'Candy Corn')

print("\nIs candy != 'Snickers'? I predict False.")
print(candy != 'Snickers')

print("\nIs producer != 'Mars'? I predict False.")
print(producer != 'Mars')

# 2. Tests using the lower() method
print("\nIs candy.lower() == 'snickers'? I predict True.")
print(candy.lower() == 'snickers')

print("\nIs candy.lower() == 'Snickers'? I predict False.")
print(candy.lower() == 'Snickers')

# 3. Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
print("\nIs price == 4? I predict True.")
print(price == 4)

print("\nIs price != 4? I predict False.")
print(price != 4)

print("\nIs price > 3? I predict True.")
print(price > 3)

print("\nIs price < 5? I predict True.")
print(price < 5)

print("\nIs price >= 4? I predict True.")
print(price >= 4)

print("\nIs price <= 3? I predict False.")
print(price <= 3)

# 4. Tests using the and keyword and the or keyword
print("\nIs candy == 'Snickers' and producer == 'Mars'? I predict True.")
print(candy == 'Snickers' and producer == 'Mars')

print("\nIs candy == 'Snickers' and price > 5? I predict False.")
print(candy == 'Snickers' and price > 5)

print("\nIs candy == 'Snickers' or producer == 'Mars'? I predict True.")
print(candy == 'Snickers' or producer == 'Mars')

print("\nIs candy == 'KitKat' or price > 5? I predict False.")
print(candy == 'KitKat' or price > 5)

# 5. Test whether an item is in a list
banned_candy = ['candy corn', 'circus peanuts']
print("\nIs 'Snickers' in banned_candy? I predict False.")
print('Snickers' in banned_candy)

print("\nIs 'candy corn' in banned_candy? I predict True.")
print('candy corn' in banned_candy)

# 6. Test whether an item is not in a list
print("\nIs 'Snickers' not in banned_candy? I predict True.")
print('Snickers' not in banned_candy)

print("\nIs 'candy corn' not in banned_candy? I predict False.")
print('candy corn' not in banned_candy)