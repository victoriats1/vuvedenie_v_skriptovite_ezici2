s = {'peach', 'chips', 'pizza', 'orange', 'apple', 'banana', 'cherry'}
lst = ["apple", "pizza"]

for item in lst:
    if item in s:
        s.remove(item)

print(s)
