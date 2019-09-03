def calc_dollars():
    piggyBank = {
        "pennies": 1200,
        "dimes": 35,
        "nickels": 24,
        "quarters": 420,
    }

    dollars = piggyBank["pennies"]/100 + piggyBank["dimes"]/10 + piggyBank["nickels"]/20 + piggyBank["quarters"]/4
    print(f"${dollars}")
    return dollars

calc_dollars()