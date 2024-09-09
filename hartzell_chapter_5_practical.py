import csv

# Pull in the CSV file and print candy types and prices
filename = 'candy_type.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    candy_type = []
    candy_price = []

    for row in reader:
        candy = row[1]
        price = float(row[2])
        candy_type.append(candy)
        candy_price.append(price)

    print(candy_type)  # Print the list of candy types
    print(candy_price)  # Print the list of candy prices

# Get the last 5 items
last_five_candies = candy_type[-5:]
last_five_prices = candy_price[-5:]

# Sorting in Alphabetical Order
sorted_type = sorted(candy_type)
print("This is the sorted candy list:", sorted_type)

# Check for duplicates
seen = set()
duplicates = set()
for candy in candy_type:
    if candy in seen:
        duplicates.add(candy)
    else:
        seen.add(candy)

for candy in duplicates:
    print(f"The name {candy} has been duplicated")

# Print the last 5 candies with prices
for candy, price in zip(last_five_candies, last_five_prices):
    print(f"The candy {candy} costs ${price} at Walmart.com")

# Sum of the full price list
total_price = sum(candy_price)
print("The sum of the full price list is...$", total_price)

# Identify and remove candies over $3.00
over_3_candies = [
    candy for candy, price in zip(candy_type, candy_price) if price > 3.00
]
filtered_candies = [
    (candy, price) for candy, price in zip(candy_type, candy_price) if price <= 3.00
]

# The candy names after filtering
filtered_candy_types = [candy for candy, _ in filtered_candies]

print("Filtered candy types:", filtered_candy_types)

# Sum of the filtered price list
filtered_price = sum(price for _, price in filtered_candies)
print("The sum of the new price list is...$", filtered_price)

