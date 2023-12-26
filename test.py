import os

def sum(n1, n2):
    """Sčítání"""
    return n1 + n2

def sub(n1, n2):
    """Odčítání"""
    return n1 - n2

def mul(n1, n2):
    """Násobení"""
    return n1 * n2

def div(n1, n2):
    """Dělení"""
    return n1 / n2

operations = {
    "+": sum,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    num1 = float(input("Jaké je první číslo? "))

    
    while True:
        for symbol in operations:
            print(symbol)

        user_symbol = input("Zvolte jednu z operací výše: ")
        num2 = float(input("Jaké je další číslo? "))

        calc_function = operations[user_symbol]
        result = calc_function(num1, num2)

        print(f"{num1} {user_symbol} {num2} = {result}")
        lets_continue = input("Chcete pokračovat ve výpočtu? 'ano' 'ne' ")
        if lets_continue == "ano":
            num1 = result
            continue
        else:
            os.system("cls")
            calculator()

calculator()