while True:
    menu = {
        "1":300,
        "2":200,
        "3":400,
        "4":120,
        "5":250,
        "6":800,
        "7":640,
        "8":1550,
        "9":360,
        "10":450,

    }
    print("---------------------------------")
    print("🍽 Wellcome to python restaurant 🐍")
    print("---------------------------------")
    print("---------------------------")
    print("✨️ Made by Kaifrajput ✨️")
    print("---------------------------")
    print("(1),coffee Rs= 300\n(2),burger Rs=200\n(3),zinger Rs=400\n(4),pepse Rs= 120\n(5),pizza Rs= 250\n(6),large pizza Rs=800\n(7),1kg beef biryani Rs=640\n(8),deal=1 large pizza,1 zinger,2 pizza Rs= 1550\n(9),mango juice Rs= 350\n(10),chicken tikka Rs=450")
    total_2 =0
    total =0
    items =input("Enter your first order in list(1,2,3,4,5,6,7,8,9,10):")
    operator_1 =int(input("How many items enter number:"))
    if items in menu:
        total += menu[items]
        total *= operator_1
        print(f"your order is {items} added:")
    else:
        print(f"your order is {items} is not available:")
    another=input("if you want another items say (yes,no)")
    if another == "yes":
        items_2 = input("Enter your second items in list(1,2,3,4,5,6,7,8,9,10):")
        operator_2 = int(input("how many items enter number:"))
        if items_2 in menu:
            total_2 += menu[items_2]
            total_2 *= operator_2
            print(f"your second order {items_2} added:")
        else:
            print(f"your order is {items_2} not available")
    sum=total+total_2
    print("------------------------------")
    print("💵 your total bill is: 💰",sum )
    print("------------------------------")
    operator=input("quit (yes,no)")
    if operator == "yes":
        break

    


