MENU = {
    "espresso" : {
        "ingredients": {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.5,
    },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.5,
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 3.0,
    }
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}

def report():
    for bahan, sisabahan in resources.items():
        if bahan in ["water", "milk"]:
            satuan = "ml"
            print(f"{bahan}: {sisabahan}{satuan}")
        elif bahan in ["coffee"]:
            satuan = "g"
            print(f"{bahan}: {sisabahan}{satuan}")
        elif bahan == "Money":
            satuan = "$"
            print(f"{bahan}:{satuan}{sisabahan}")

def prosescoin():
    print("Please insert coins")
    quarters = float(input("How many quarters: "))
    dimes= float(input("How many dimes: "))
    nickles= float(input("How many nickles: "))
    pennies= float(input("How many quarters: "))

    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01 
    return total

def cektransaksi(coin, kopi):
    if coin < MENU[kopi]["cost"]:
        print("Sorry that's not enough money. Money refunded. ")
        return False
    else:
        change = coin - MENU[kopi]["cost"]
        resources["Money"] = resources.get("Money",0) + MENU[kopi]["cost"]
        print(f"Here is ${change:.2f} dollars in change.")
        return True
    
def cekbahan(kopi):
    for i in MENU[kopi]["ingredients"]:
        if MENU[kopi]["ingredients"][i] > resources[i] :
            return False
    return True

def makeACofee(kopi):
    for i in MENU[kopi]["ingredients"]:
        resources[i]-= MENU[kopi]["ingredients"][i]
    print(f"Here is your {kopi}. Enjoy!")

def coffeeMachine():
    masihberjalan = True
    while masihberjalan:
        pesan = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if pesan == "report":
            report()
        elif pesan == "off":
            masihberjalan = False
        elif pesan in MENU:
            bahanlengkap = cekbahan(pesan)
            if bahanlengkap :
                totalcoin = prosescoin()
                berhasil = cektransaksi(totalcoin , pesan)
                if berhasil :
                    makeACofee(pesan)
            else:
                print("Sorry We dont have enough ingredients")
        else:
            print('Please Type the right prompt')

coffeeMachine()