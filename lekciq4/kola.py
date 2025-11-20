car1 = {
    "Brand": input("Brand (car 1): "),
    "Model": input("Model (car 1): "),
    "Horsepower": int(input("Horsepower (car 1): "))
}

car2 = {
    "Brand": input("Brand (car 2): "),
    "Model": input("Model (car 2): "),
    "Horsepower": int(input("Horsepower (car 2): "))
}

if car1["Horsepower"] > car2["Horsepower"]:
    print(f"{car1['Brand']} {car1['Model']} is faster")
elif car1["Horsepower"] < car2["Horsepower"]:
    print(f"{car2['Brand']} {car2['Model']} is faster")
else:
    print("I dvete koli sa ednakwo burzi")