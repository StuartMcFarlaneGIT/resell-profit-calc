platforms = ['ebay', 'vinted', 'facebook']
fee_percentages = {
    'ebay' : 0.04,
    'vinted' : 0.00,
    'facebook' : 0.00,
}


buy = float(input("How much did you pay? £"))
sell = float(input("How much is it selling for? £"))
platform = input(f"Choose which platform you are selling on {platforms}: ")
if platform in fee_percentages:
    fees = fee_percentages[platform]
else:
    print('enter one of the patforms stated')
item = str(input("What item are you selling? "))

def calculator(buy, sell, fees):
    fee = sell * fees
    return(sell - buy - fee)
profit = calculator(buy, sell, fees)

print(profit)