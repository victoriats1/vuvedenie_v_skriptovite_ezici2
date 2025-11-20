numbers = []
n = int(input("Vuvedi broj elementi:"))

for i in range(n):
    num=int(input(f"Vuvedete element: "))
    numbers.append(num)

numbers.sort()
print(numbers)

