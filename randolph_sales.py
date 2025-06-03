import random
import os
cart = []
def taxCalculator(subtotal):
    states = {
        "alabama": 0.04,
        "alaska": 0.00,
        "arizona": 0.056,
        "arkansas": 0.065,
        "california": 0.0725,
        "colorado": 0.029,
        "connecticut": 0.0635,
        "delaware": 0.00,
        "district of columbia": 0.0575,
        "dc": 0.0575,
        "florida": 0.06,
        "georgia": 0.04,
        "hawaii": 0.04,
        "idaho": 0.06,
        "illinois": 0.0625,
        "indiana": 0.07,
        "iowa": 0.06,
        "kansas": 0.065,
        "kentucky": 0.06,
        "louisiana": 0.04,
        "maine": 0.055,
        "maryland": 0.06,
        "massachusetts": 0.0625,
        "michigan": 0.06,
        "minnesota": 0.06875,
        "mississippi": 0.07,
        "missouri": 0.04225,
        "montana": 0.00,
        "nebraska": 0.055,
        "nevada": 0.0685,
        "new hampshire": 0.00,
        "new jersey": 0.06625,
        "new mexico": 0.05125,
        "new york": 0.04,
        "north carolina": 0.0475,
        "north dakota": 0.05,
        "ohio": 0.0575,
        "oklahoma": 0.045,
        "oregon": 0.00,
        "pennsylvania": 0.06,
        "rhode Island": 0.07,
        "south carolina": 0.06,
        "south dakota": 0.04,
        "tennessee": 0.07,
        "texas": 0.0625,
        "utah": 0.0475,
        "vermont": 0.06,
        "virginia": 0.053,
        "washington": 0.065,
        "west virginia": 0.06,
        "wisconsin": 0.05,
        "wyoming": 0.04,
        "puerto rico": 0.06,
        "guam": 0.04,
        "american samoa": 0.04,
        "U.S. virgin islands": 0.04,
        "northern mariana islands": 0.05,
        "palau": 0.04,
    }
    state = input("What state are you in?").lower()
    if state in states:
        tax = subtotal * states[state]
        total = subtotal + tax
        print(f"Your subtotal is: ${subtotal:.2f}")
        print(f"Your tax is: ${tax:.2f}")
        print(f"Your total is: ${total:.2f}")
    else:
        print("State not found. Please check the spelling and try again.")
        taxCalculator(subtotal)
    return subtotal, tax, total
    
    

def itemFinder():
    done = True
    while done:
        itemName = input('What is the name of your item? (type "done" to finish)')
        if itemName.lower() == "done":
            done = False
            print("Your cart is:")
            for item in cart:
                print(f"{item[0]} | ${item[1]} | {item[2]} | ${item[1] * item[2]} total ")
            totalCost = sum(item[1] * item[2] for item in cart)
            print(f"subtotal cost: ${totalCost}")
            taxCalculator(totalCost)
            break
            
        itemCost = input(f'what is the cost of a unit of {itemName}? (type only numbers)')
        itemAmount = input(f"how many {itemName}s are you getting?")
        try:
            itemCost = float(itemCost)
            itemAmount = int(itemAmount)
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            cart.append((itemName, itemCost, itemAmount))
            results = (f"Added {itemAmount} {itemName}s to your cart at price {itemCost}.")
            print(f"{results:_^20}")
itemFinder()