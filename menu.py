menu={
    'beefsteak':700,
    'chicken_steak':600,
    'tuna_steak':650,
    'veggie_burger':400,
    'french_fries':300,
    'coke':150,
    'pepsi':150,    
    'pasta':600,
    'ice_cream':200,
    'juice':250
}
print("Welcome to our cafe!")
print("order any item in the menu")
print("Here is our menu:")
for item,price in menu.items():
    print(f"{item}: {price}")
total_amount=0
while True:
    order=input("enter your first order:")
    if order in menu:
        total_amount+=menu[order]
        print(f"{order} is available and the price is {menu[order]} is added to you cart")
    else:
        print(f"sorry {order} is not available in this time please order something else")
    need=input("do you want to order something else? (yes/no):")
    if need!='yes':
        break
print(f"your total bill is {total_amount}")
print("bill payment methods: cash, card, upi")
print("Thank you for visiting our cafe!")