import math

dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here

def cash2coins(cash):
    piggyBank["quarters"] = cash//.25
    piggyBank["dimes"] = (cash%.25)//.10
    piggyBank["nickels"] = ((cash%.25)%.10)//.05
    piggyBank["pennies"] = math.ceil((((cash%.25)%.10)%.05)/.01)
    print(piggyBank) 

cash2coins(dollarAmount)