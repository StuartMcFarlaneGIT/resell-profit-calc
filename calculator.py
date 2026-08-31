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

def profit_percentage(sell, profit):
    return((profit/sell)*100)

promo = 0.00
postage = 0.00
buy = 0.00
sell = 0.00

item = str(input("What item are you selling? "))

category = input(f"Choose which platform you are selling on {categories}: ")
if category not in categories:
    print('enter one of the categories stated')

while buy == 0.00:
    try: 
        buy = float(input(f"How much did {item} cost you? £"))
    except ValueError:
        print('Please only enter a number value')

while sell == 0.00:
    try:
        sell = float(input("How much is it selling for? £"))
    except ValueError:
        print('Please only enter a number value')

platform = input(f"Choose which platform you are selling on {platforms}: ")
if platform not in platforms:
    print('enter one of the patforms stated')

if platform == 'ebay':
    promo = 0.03

if platform in platforms:
    postage = postage_fees[platform]

profit = profit_calculator(buy, sell, promotion_fees(sell, promo), postage)
margins = profit_percentage(sell, profit)

print(f'Total profit = £{profit:.2f} \n Profit percentage = {margins:.2f}%')