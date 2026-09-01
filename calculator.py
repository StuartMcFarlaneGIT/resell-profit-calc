"""
This project was made to allo me to document my whole reselling business.
The program takes in the item, category, what it was bought for, sold for and will display the profit and margins made on the item.
This project will save inputs to a CSV file, allowing future SQL to be performed to gather in depth details on the profits of each category.
"""
import csv
import os
from datetime import date

CSV_FILE = 'sales.csv'
HEADERS = ["date", "item", "category", "platform", "buy", "sell", "postage", "promo_fee", "profit", "margin"]

#all platforms within reselling business
platforms = [
    'ebay', 
    'vinted', 
    'facebook'
    ]
#Postage fees per platform
postage_fees = {
    'ebay': 2.94,
    'vinted': 0.00,
    'facebook': 0.00,
    }
#Reselling categories
categories = [
    'shoes', 
    'watches', 
    'DVDs', 
    'video games', 
    'clothing', 
    'phones',
    'facebook finds'
    ]

#function uses the sell and promotion fees of each platform to allow the total promotion fee for the sold item.
def promotion_fees(sell, promo):
    promo_fee = float(sell*promo)
    return promo_fee

#function calculates the profit of the item, taking the sell price and subtracting the buy, promo_fee and postage.
def profit_calculator(buy, sell, promo_fee, postage):
    return(sell - buy - promo_fee - postage)

#function calculates the profit margins for the item, dividing the profit by the buy price *100.
def profit_percentage(buy, profit):
    if buy == 0:
        return 0.00
    return((profit/buy)*100)

def save_to_csv(row):
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(HEADERS)
        writer.writerow(row)

#loops the project so the user doesnt need to keep restarting the program.
while True:
    #pre sets the following values to 0.00 at the start of each loop.
    promo = 0.00
    postage = 0.00
    buy = 0.00
    sell = 0.00

    #inital input for the user to assign the item to their input.
    item = str(input("What item are you selling? "))

    #Loop the category input so that it must match one of the categories in the preset categories list
    while True:
        category = input(f"Choose which category you are selling on {categories}: ")
        #will break if the category entered is in categories
        if category in categories:
            break
        #if not in categories it will be printed and reasked
        if category not in categories:
            print('enter one of the categories stated')

    #Loops the buy input, so the user has to enter a numeric value and not a string
    while True:
        try: 
            buy = float(input(f"How much did {item} cost you? £"))
            break
        #if the value isnt a number the valueerror will occur and print the following message
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

    #if the entered platfrom string is ebay the promo is set 0.03
    if platform == 'ebay':
        promo = 0.03

    #the platform is in platforms, the postage is assigned the associated postage fee.
    if platform in platforms:
        postage = postage_fees[platform]

    promo_fee = promotion_fees(sell,promo)
    #profit is the result of the profit calculator function
    profit = profit_calculator(buy, sell, promo_fee, postage)
    #margins is the result of the profit percentage function
    margins = profit_percentage(buy, profit)

    save_to_csv([
    date.today(), item, category, platform,
    f"{buy:.2f}", f"{sell:.2f}", f"{postage:.2f}",
    f"{promo_fee:.2f}", f"{profit:.2f}", f"{margins:.2f}"
    ])

    #will print the profit and the margins of each item
    print(f'Total profit = £{profit:.2f} \n Profit percentage = {margins:.2f}%')
    #asks the user if they have another item to add, if yes restarts the loop, if no then it breaks and ends the loop.
    again = input("Do you have another item? (y/n): ").lower()
    if again != 'y':
        break

#print to csv file next