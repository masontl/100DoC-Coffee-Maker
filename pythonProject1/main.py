## TODO 1: establish dictionaries of coffee maker supplies and coin values
import dictionaries

active_option = "" #user input
water = dictionaries.resources["water"]
milk = dictionaries.resources["milk"]
coffee = dictionaries.resources["coffee"]
total_money = 0.0
user_money = 0.0


espresso_drink = False
latte_drink = False
cappuccino_drink = False
adequate_supplies = False
beverage = "espresso"
drink_choice_req_supplies = dictionaries.menu[beverage]["ingredients"]






def espresso():
  if active_option == "e" or "espresso":
    espresso_drink = True
  return espresso_drink
espresso_drink = espresso()

def latte():
  if active_option == "l" or "latte":
    latte_drink = True
  return latte_drink
latte_drink = latte()

def cappuccino():
  if active_option == "c" or "cappuccino":
    cappuccino_drink = True
  return cappuccino_drink
cappuccino_drink = cappuccino()

def drink():
  if espresso():
    drink_choice = dictionaries.menu ["espresso"]
    beverage = "espresso"
  elif latte():
    drink_choice = dictionaries.menu["latte"]
    beverage = "latte"
  elif cappuccino():
    drink_choice = dictionaries.menu["cappuccino"]
    beverage = "cappuccino"
  return beverage
beverage = drink()


## TODO 2: create a report definition which returns the current state of both the above dictionaries
def report():
  if active_option == "report":
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${total_money}")

# TODO 3: check the coffee maker for supplies (including coins?)
def supplies_good():
  if espresso():
    if dictionaries.resources["water"] > drink_choice_req_supplies["water"]:
      adequate_supplies = True
  elif latte() or cappuccino():
    if dictionaries.resources["water"] > drink_choice_req_supplies["water"]:
      if dictionaries.resources["coffee"] > drink_choice_req_supplies["coffee"]:
        if dictionaries.resources["milk"] > drink_choice_req_supplies["milk"]:
          adequate_supplies = True
  return adequate_supplies
adequate_supplies = supplies_good()

## TODO 4: Create definitions of the types of coffees and the supplys they'll utilize

# TODO 5: if supplies are adequate, then ask for money
def pay_me():
  if adequate_supplies:
    payment_info = {
        "quarter": input("How many quarter(s) are you paying?"),
        "dime": input("How many dime(s) are you paying?"),
        "nickel": input("How many nickel(s) are you paying?"),
        "penny": input("How many penny(s) are you paying?"),
    }
    return payment_info

payment_info = pay_me()
dictionaries.user_money["quarter"] = payment_info["quarter"]
dictionaries.user_money["dime"] = payment_info["dime"]
dictionaries.user_money["nickel"] = payment_info["nickel"]
dictionaries.user_money["penny"] = payment_info["penny"]
# TODO 6: see if money is enough; if not then return all money and cancel transaction

# TODO 7: once the coffee is made, ask if they want another coffee
# def another_coffee():
#   agaiiin = input("Would you like another beverage?").lower()
#   idle()


## TODO 8: create an end definition that can be triggered to quit the program
def end():
  if active_option("end"):
    quit()

##TODO 9: ask the user "What would you like?"

## TODO 10: state "Here is your {drink}. Enjoy!"
def drink_deliver():
  print(f"Please enjoy your {beverage}!")
  idle()

## TODO 11: create an idle state?
def idle():
  print("Beverage list:\nEspresso\nLatte\nCappuccino")
  active_option = input("Please place your beverage order\n(can be full name or just first letter of beverage)").lower()

# TODO 12: rewrite the used up resources

# TODO 13: do math to come up with the total math
def math():
  total_money = (dictionaries.resources["quarter"]*dictionaries.coins["quarter"]) + (dictionaries.resources["dime"]*dictionaries.coins["dime"]) + (dictionaries.resources["nickel"]*dictionaries.coins["nickel"]) + (dictionaries.resources["penny"]*dictionaries.coins["penny"])
  return total_money
total_money = math()

def user_math():
  user_money = (dictionaries.user_money["quarter"] * dictionaries.coins["quarter"]) + (dictionaries.user_money["dime"] * dictionaries.coins["dime"]) + (dictionaries.user_money["nickel"] * dictionaries.coins["nickel"]) + (dictionaries.user_money["penny"] * dictionaries.coins["penny"])
  return user_money
user_money = user_math()



print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${total_money}")
