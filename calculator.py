platforms = [
    'ebay', 
    'vinted', 
    'facebook'
    ]
postage_fees = {
    'ebay': 2.94,
    'vinted': 0.00,
    'facebook': 0.00,
    }
categories = [
    'shoes', 
    'watches', 
    'DVDs', 
    'video games', 
    'clothing', 
    'phones',
    'facebook finds'
    ]

def promotion_fees(sell, promo):
    promo_fee = float(sell*promo)
    return promo_fee

def profit_calculator(buy, sell, promo_fee, postage):
    return(sell - buy - promo_fee - postage)

def profit_percentage(buy, profit):
    if buy == 0:
        return 0.00
    return((profit/buy)*100)

while True:
    promo = 0.00
    postage = 0.00
    buy = 0.00
    sell = 0.00

    item = str(input("What item are you selling? "))

    while True:
        category = input(f"Choose which category you are selling on {categories}: ")
        if category in categories:
            break
        if category not in categories:
            print('enter one of the categories stated')
            
    while True:
        try: 
            buy = float(input(f"How much did {item} cost you? £"))
            break
        except ValueError:
            print('Please only enter a number value')

    while True:
        try:
            sell = float(input("How much is it selling for? £"))
            break
        except ValueError:
            print('Please only enter a number value')

    while True:
        platform = input(f"Choose which platform you are selling on {platforms}: ")
        if platform in platforms:
            break
        if platform not in platforms:
            print('enter one of the patforms stated')

    if platform == 'ebay':
        promo = 0.03

    if platform in platforms:
        postage = postage_fees[platform]

    profit = profit_calculator(buy, sell, promotion_fees(sell, promo), postage)
    margins = profit_percentage(buy, profit)

    print(f'Total profit = £{profit:.2f} \n Profit percentage = {margins:.2f}%')
    again = input("Do you have another item? (y/n): ").lower()
    if again != 'y':
        break

#print to csv file next
#documentation, comments
#try change input for categories and platform to choice to allow the user to select from the list instead of typing