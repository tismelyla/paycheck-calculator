while True:

    hourlypay = float(input("How much do you get paid hourly? "))
    hours = float(input("How many hours did you work per day? "))
    days = float(input("How many days did you work? "))
    tax = int(100)

    Bpay = hourlypay * hours * days  # Daily pay

    print("Would you like to calculate your paycheck after tax? y/n ")
    aftertax = input()
    if aftertax == 'y':
        taxin = float(input("What is your tax rate? (%) "))
        Mtaxrate = tax - taxin
        taxrate = Mtaxrate / 100
        Apay = Bpay * taxrate
    else:
        print("Skipping tax rate calculations.")

    print("Do you want to split the paycheck into Savings & Everyday? y/n ")
    s2 = input()
    if s2 == 'y':
        print("You have been paid $",Bpay / 2," into your accounts.")
        print("$",Bpay," total.")
    
    else:
        print("You got paid: $",Bpay)
    
    repeat = input("Do you want to repeat the program? y/n ").strip().lower()
    if repeat != 'y':
        break
    
    
