items = ['apple', 'orange', 'watermelon', 'banana', 'apple']

if len(items) != len(set(items)):
    print("There are equal items in the list")
else:
    print("All items are unique")


items = ('apple', 'orange', 'watermelon', 'banana', 'apple')

if len(items) != len(set(items)):
    print("There are equal items in the tuple")
else:
    print("All items are unique")
