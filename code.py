Water = 10000
Milk = 1000
Coffee = 1000
Money = 0
user_input="on"
while(user_input!="off"):
    user_input=input("What would you like? (espresso/latte/cappuccino):").lower()
    if(user_input=="report"):
        print(f"Water : {Water} ml")
        print(f"Milk : {Milk} ml")
        print(f"Coffee : {Coffee} g")
        print(f"Money : {Money} $")
    elif(user_input=="espresso"):
        req_coffee = 20
        req_water = 40
        req_milk = 170
        cost = 3.25
        if(Water >= 45 and Milk >= 200 and Coffee >= 25):
            Water = Water - 40
            Milk = Milk - 170
            Coffee = Coffee - 20
            Quarter = int(input("Enter number of Quarter : "))
            Dime = int(input("Enter number of Dime : "))
            Nickle = int(input("Enter number of Nickle : "))
            Pennie = int(input("Enter number of Pennie : "))
            given_money = 0.25*(Quarter) + 0.1*(Dime) + 0.05*(Nickle) + 0.01*(Pennie)
            if(cost<=given_money):
                if(given_money==cost):
                    Money = Money + cost
                    print("Here is your Espresso. Enjoy!")
                else:
                    change = given_money - cost
                    final_change = round(change,2)
                    print(f"Here is your Change : {final_change} $ . Enjoy your Espresso!! ")
                    Money = Money + cost
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if(Water < 45):
                print("Sorry there is not enough water")
            if(Milk < 200):
                print("Sorry there is not enough milk")
            if(Coffee < 25):
                print("Sorry there is not enough resources")
    elif(user_input=="latte"):
        req_coffee = 25
        req_water = 45
        req_milk = 200
        cost = 2.95
        if(Water >= 45 and Milk >= 200 and Coffee >= 25):
            Water = Water - 45
            Milk = Milk - 200
            Coffee = Coffee - 25
            Quarter = int(input("Enter number of Quarter : "))
            Dime = int(input("Enter number of Dime : "))
            Nickle = int(input("Enter number of Nickle : "))
            Pennie = int(input("Enter number of Pennie : "))
            given_money = 0.25*(Quarter) + 0.1*(Dime) + 0.05*(Nickle) + 0.01*(Pennie)
            if(cost<=given_money):
                if(given_money==cost):
                    Money = Money + cost
                    print("Here is your latte. Enjoy!")
                else:
                    change = given_money - cost
                    final_change = round(change,2)
                    print(f"Here is your Change : {final_change} $ . Enjoy your Latte!! ")
                    Money = Money + cost
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if(Water < 45):
                print("Sorry there is not enough water")
            if(Milk < 200):
                print("Sorry there is not enough milk")
            if(Coffee < 25):
                print("Sorry there is not enough resources")
    elif(user_input=="cappuccino"):
        req_coffee = 30
        req_water = 50
        req_milk = 150
        cost = 2.75
        if(cost<=given_money):
            Water = Water - 50
            Milk = Milk - 150
            Coffee = Coffee -30
            Quarter = int(input("Enter number of Quarter : "))
            Dime = int(input("Enter number of Dime : "))
            Nickle = int(input("Enter number of Nickle : "))
            Pennie = int(input("Enter number of Pennie : "))
            given_money = 0.25*(Quarter) + 0.1*(Dime) + 0.05*(Nickle) + 0.01*(Pennie)
            if(cost<=given_money):
                if(given_money==cost):
                    Money = Money + cost
                    print("Here is your Cappucino. Enjoy!")
                else:
                    change = given_money - cost
                    final_change = round(change,2)
                    print(f"Here is your Change : {final_change} $ . Enjoy your Cappuccino!! ")
                    Money = Money + cost
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if(Water < 45):
                print("Sorry there is not enough water")
            if(Milk < 200):
                print("Sorry there is not enough milk")
            if(Coffee < 25):
                print("Sorry there is not enough resources")
