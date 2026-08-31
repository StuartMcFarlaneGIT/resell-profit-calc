platforms = ['ebay', 'vinted', 'facebook']
postage_fees = {
    'ebay': 2.94,
    'vinted': 0.00,
    'facebook': 0.00
}

promo = 0.00
postage = 0.00

buy = float(input("How much did you pay? £"))
sell = float(input("How much is it selling for? £"))
platform = input(f"Choose which platform you are selling on {platforms}: ")
if not platform in platforms:
    print('enter one of the patforms stated')
item = str(input("What item are you selling? "))

if platform == 'ebay':
    promo = 0.03

if platform in platforms:
    postage = postage_fees[platform]

def promotion_fees(sell, promo):
    promo_fee = float(sell*promo)
    return promo_fee

def profit_calculator(buy, sell, promo_fee, postage):
    return(sell - buy - promo_fee - postage)

profit = profit_calculator(buy, sell, promotion_fees(sell, promo), postage)

def profit_percentage(sell, profit):
    return((profit/sell)*100)
margins = profit_percentage(sell, profit)

print(f'Total profit = £{profit} \n Profit percentage = {margins:.2f}%')