menu  = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
is_on = True
def process_coins():
        """ Returns the total number of coins processed"""
        print("Please input the required coins ? ")
        total  = int(input("How many Qarters? : "))*0.25
        total += int(input("How many dimes?: "))* 0.1
        total += int(input("How many nickels?: "))* 0.05
        total += int(input("How many pennies? : "))*0.01
        return total 

def resource_manager(selection):
    ingredients = menu[selection]
    for i in ingredients:
        resources[i] -= ingredients[i]
    


def payment_processing(money_received, drink_amount):
    if money_received >= drink_amount:
        profit += drink_amount
        print("Sorry you do not have enough Money")
        change = round (money_received - drink_amount,2)
        return True
    else:
        return False 

while is_on :
    selection = input("What would like (Espresso, Latte, Cappucino?)") 
    if selection == "off":
        is_on = False
    else:
        def resource_checker(user_selection):
            if user_selection == "espresso":
                if menu["espresso"]["ingredients"]["water"] <= resources["water"]:
                    if menu['espresso']["ingredients"]["coffee"] <= resources["coffee"]:
                        print("Please wait for your espresso")
                    else:
                        print("Print not enough coffee")
                else:
                    print("not enough water")
            else:
                def other_checker(user_selection2):
                    if menu[user_selection2]["ingredients"]["water"] <= resources["water"]:
                        if menu[user_selection2]["ingredients"]["coffee"] <= resources["coffee"]:
                            if menu[user_selection2]["ingredients"]["milk"] <= resources["milk"]:
                                payment = process_coins()
                                

                                print(f"We are making your {user_selection2}")
                            else:
                                print("No enough milk")
                        else:
                            print("No enough coffee")

                    else:
                        print("No enough water")
                
                other_checker(user_selection2 = selection)

        resource_checker(selection)






report_output = input("Would you like a report of the remaining resourceds?(YES OR NO) ")
def report():

    return resources 


if report_output == 'yes':
    print(report())
    print(f"The profit is {profit}")

else:
    print("Thank you")
    
