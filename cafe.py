#creating the list and the two dictionaries

my_menu = ["croissants", "muffins", "lattes", "cookies"]
stock_dict= {"croissants":10, "muffins": 20, "lattes":30, "cookies":15}
price_dict= {"croissants": 2, "muffins":3, "lattes": 2.50, "cookies": 1.50}

#assigning the values of the stock dictioanry to stock
#assigning the values of price to the variable price
stock = stock_dict.values
price = price_dict.values

total_value = 0

for item in my_menu:
    total_value += stock_dict[item]*price_dict[item]
#prints out total value with an f-string
print(f"The total value of stock is £{total_value}")