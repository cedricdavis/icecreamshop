info = []
print("Hello! Welcome to Cedric's Ice Cream Parlor.")

customer_name = input("May I have a name for your order?")


def main():
    perference()


def perference():
    pereference = input("Are you craving a FRUIT flavor or a CHOCOLATE flavor? ")

    if pereference == "FRUIT":
       choice_Fruity()
    if pereference == "CHOCOLATE":
       choice_Chocolate()
    else:
        print("Please input your choice exactly as stated.")
        perference()

def size():
    sizeinput = input("Would you like 1, 2 ,or 3 scoops? ") 
    if sizeinput == "1":
        scoops = 1
        price = 4.99
        info.append(price)
        info.append(scoops)
        receipt(info)
    if sizeinput  == "2":
        scoops = 2
        price = 8.99
        info.append(price)
        info.append(scoops)
        receipt(info)
    if sizeinput  == "3":
        scoops = 3
        price = 10.99
        info.append(price)
        info.append(scoops)
        receipt(info)
    else:
        size()
    



def choice_Chocolate():
    print("1. Classic Chocolate")
    print("2. Chocolate & Peanut Butter")
    print("3. S'more")
    print("4. Chocolate Chip")
    print("5. Mint Chocolate Chip")
    flavor_number = input("We have a wide selection of Chocolately flavors to choose from! Which would you like? (Please input the number to your corresponding item)")

    if flavor_number == "1":
        flavor = 'Classic Chocolate'
        info.append(flavor)
        print("Great Choice!")
        size()
    if flavor_number == "2":
        flavor = 'Chocolate & Peanut Butter'
        info.append(flavor)
        print("Great Choice!")
        size()
    if flavor_number == "3":
        flavor = "S'more"
        info.append(flavor)
        print("Great Choice!")
        size()
    if flavor_number == "4":
        flavor = 'Chocolate Chip'
        info.append(flavor)
        print("Great Choice!")
        size()
    if flavor_number == "5":
        flavor = 'Mint Chocolate Chip'
        info.append(flavor)
        print("Great Choice!")
        size()
    else:
        choice_Chocolate()

def choice_Fruity():
    print("6. Strawberry")
    print("7. Orange")
    print("8. Lime")
    print("9. Watermelon")
    print("10. Lemonade")
    flavor_number = input("We have a wide selection of fruity flavors to choose from! Which would you like? (Please input the number to your corresponding item)")

    if flavor_number == "6":
        flavor = 'Strawberry'
        info.append(flavor)
        print("Great Choice!")
        size()
    if flavor_number == "7":
        flavor = 'Orange'
        info.append(flavor)
        print("Great Choice!")
        size()
    if flavor_number == "8":
        flavor = 'Lime'
        info.append(flavor)
        print("Great Choice!")
        size()
    if flavor_number == "9":
        flavor = 'Watermelon'
        info.append(flavor)
        print("Great Choice!")
        size()
    if flavor_number == "10":
        flavor = 'Lemonade'
        info.append(flavor)
        print("Great Choice!")
        size()
    else:
        choice_Fruity()

def receipt(info):
    checking = input(str(customer_name) + ", you asked for " + str(info[2]) + " scoops of " + str(info[0]) + " flavored ice cream? (y or n)")
    if checking == "y":
        input("Alright, your total is going to be " + str(info[1]))
        print("Thank you for choosing Cedric's Ice Cream Parlor!")
        quit()
    if checking == "n":
        info.clear()
        main()
    else:
        receipt(info)
    


main() 






       
     