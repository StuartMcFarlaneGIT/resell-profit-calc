platforms = ['ebay', 'vinted', 'facebook']
promo = 0

buy = float(input("How much did you pay? £"))
sell = float(input("How much is it selling for? £"))
platform = input(f"Choose which platform you are selling on {platforms}: ")
if not platform in platforms:
    print('enter one of the patforms stated')
item = str(input("What item are you selling? "))

if platform == 'ebay':
    promo = 0.03

def promotion_fees(sell, promo):
    promo_fee = float(sell*promo)
    return promo_fee

def calculator(buy, sell, promo_fee):
    return(sell - buy - promo_fee)
profit = calculator(buy, sell, promotion_fees(sell, promo))

print(profit)