## TODO 1: establish dictionaries of coffee maker supplies and coin values
import dictionaries

active_option = "" #user input
water = dictionaries.resources["water"]
milk = dictionaries.resources["milk"]
coffee = dictionaries.resources["coffee"]
drink_cost = 0.0
total_money = 0.0
user_money = 0.0
got_any_change = 0.0


espresso_drink = False
latte_drink = False
cappuccino_drink = False
adequate_supplies_to_make_drink = False
beverage = "espresso"
drink_choice = "espresso"
drink_choice_req_supplies = dictionaries.menu[beverage]["ingredients"]


# def espresso():
#   if active_option == "e" or "espresso":
#     espresso_drink = True
#   return espresso_drink
#
#
# def latte():
#   if active_option == "l" or "latte":
#     latte_drink = True
#   return latte_drink
#
#
# def cappuccino():
#   if active_option == "c" or "cappuccino":
#     cappuccino_drink = True
#   return cappuccino_drink


def drink():
  if active_option == "e" or active_option == "espresso":
    drink_choice = dictionaries.menu ["espresso"]
    beverage = "espresso"
  elif active_option == "l" or active_option == "latte":
    drink_choice = dictionaries.menu["latte"]
    beverage = "latte"
  elif active_option == "c" or active_option == "cappuccino":
    drink_choice = dictionaries.menu["cappuccino"]
    beverage = "cappuccino"
  else:
    beverage = ""
  return beverage


## TODO 2: create a report definition which returns the current state of both the above dictionaries
def report():
  if active_option == "report":
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${total_money}\nProfit: ${user_money}")


# TODO 3: check the coffee maker for supplies (including coins?)
def supplies_good():
  if "espresso":
    if dictionaries.resources["water"] > drink_choice_req_supplies["water"]:
      adequate_supplies_to_make_drink = True
  elif "latte" or "cappuccino":
    if dictionaries.resources["water"] > drink_choice_req_supplies["water"]:
      if dictionaries.resources["coffee"] > drink_choice_req_supplies["coffee"]:
        if dictionaries.resources["milk"] > drink_choice_req_supplies["milk"]:
          adequate_supplies_to_make_drink = True
  return adequate_supplies_to_make_drink


def beverage_cost():
  drink_cost = dictionaries.menu[beverage]["cost"]
  return drink_cost


## TODO 4: Create definitions of the types of coffees and the supplys they'll utilize

# TODO 5: if supplies are adequate, then ask for money
def pay_me():
  # if adequate_supplies_to_make_drink:
  payment_info = {
      "quarter": float(input("How many quarter(s) are you paying?")),
      "dime": float(input("How many dime(s) are you paying?")),
      "nickel": float(input("How many nickel(s) are you paying?")),
      "penny": float(input("How many penny(s) are you paying?")),
  }
  return payment_info


# TODO 6: see if money is enough; if not then return all money and cancel transaction

# TODO 7: once the coffee is made, ask if they want another coffee
# def another_coffee():
#   agaiiin = input("Would you like another beverage?").lower()
#   idle()


## TODO 8: create an end definition that can be triggered to quit the program
def end():
  if active_option == "end":
    quit()


##TODO 9: ask the user "What would you like?"

## TODO 10: state "Here is your {drink}. Enjoy!"
def drink_deliver():
  print(f"Please enjoy your {beverage}!")


## TODO 11: create an idle state?
def idle():
  print("Beverage list:\nEspresso\nLatte\nCappuccino")
  active_option = input("Please place your beverage order\n(can be full name or just first letter of beverage)").lower()
  return active_option


# TODO 12: rewrite the used up resources

# TODO 13: do math to come up with the total math
def math():
  total_money = (dictionaries.resources["quarter"]*dictionaries.coins["quarter"]) + (dictionaries.resources["dime"]*dictionaries.coins["dime"]) + (dictionaries.resources["nickel"]*dictionaries.coins["nickel"]) + (dictionaries.resources["penny"]*dictionaries.coins["penny"])
  return total_money


def user_math():
  user_money = (dictionaries.user_money["quarter"] * dictionaries.coins["quarter"]) + (dictionaries.user_money["dime"] * dictionaries.coins["dime"]) + (dictionaries.user_money["nickel"] * dictionaries.coins["nickel"]) + (dictionaries.user_money["penny"] * dictionaries.coins["penny"])
  return user_money


def produce_change():
  got_any_change = user_money - drink_cost
  print(f"Please take your change of : ${got_any_change}")
  return got_any_change





while(1):
  # idle()
  active_option = idle()
  # espresso_drink = espresso()
  # latte_drink = latte()
  # cappuccino_drink = cappuccino()
  beverage = drink()
  if beverage and beverage != "":
    adequate_supplies_to_make_drink = supplies_good()
    if adequate_supplies_to_make_drink:
      payment_info = pay_me()
      dictionaries.user_money["quarter"] = payment_info["quarter"]
      dictionaries.user_money["dime"] = payment_info["dime"]
      dictionaries.user_money["nickel"] = payment_info["nickel"]
      dictionaries.user_money["penny"] = payment_info["penny"]
      user_money = user_math()
      drink_cost = beverage_cost()
      if user_money >= drink_cost:
        got_any_change = produce_change()
        drink_deliver()
  elif active_option == "report":
    total_money = math()
    user_money = user_math()
    report()
  elif active_option == "end":
    end()



# print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${total_money}\nProfit: ${user_money}")


#TODO: have supplies subtract from the resources

#TODO: have the user_money not overwrite and have it add.  get rid of total_money; not needed