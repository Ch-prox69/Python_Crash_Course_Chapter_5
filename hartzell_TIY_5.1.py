# 5.1
candy = 'Snickers'
producer = 'Mars'
price = 4

print("Is candy == 'Snickers'? I predict True.")
print(candy == 'Snickers')

print("\nIs candy == 'Candy Corn'? I predict False.")
print(candy == 'Candy Corn')

# True tests
print("\nIs Snickers apart of candy? I predict True")
print(candy == 'Snickers')

print("\nIs candy apart of Snickers? I predict True")
print(candy == 'Snickers')

banned_candy = ['candy corn', 'circus peanuts']
candy = 'Snickers'
if candy not in banned_candy:
    print(f"\n{candy.title()},it is true, Snickers is apart of candy")

print("\n Is candy made by Mars? I predict True")
print(producer == 'Mars')

# False tests
print("\nIs producer of candy Kellog? I predict false")
print(producer == 'Kellog')

print("\nI think the price of a snikers bar is $12, I predict true")
if price != 12:
    print("\nFalse")

print("\nIs the price of a snikers bar $20? I predict False")
print(price != 4)

print("\nIs name == KitKat?")
print(candy == 'KitKat')



