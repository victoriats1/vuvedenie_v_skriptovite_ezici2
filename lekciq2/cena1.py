
n = int(input("Enter km: "))
daytime = str(input("Enter time:"))

if n < 20:
    print("Taxi is the only way")
    if daytime == "day":
        price = (0.79 * n) + 0.7
    elif daytime == "night":
        price = (0.90 * n) + 0.7
    else:
        print("Invalid time entered.")
        price = None
elif 20 <= n <= 100:
    print("Bus is the better option")
    price = 0.09 * n
else: 
    print("Train is your best option!")
    price = 0.06 * n