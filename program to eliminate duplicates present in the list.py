# Program to eliminate duplicates present in the list
l0 = eval(input("Enter List of values (separated by commas only): "))
set1 = set(l0)
print(set1)
# Alternate way of doing this
list1 = eval(input("Enter List of values (separated by commas only): "))
l1 = []
for x in list1:
    if x not in l1:
        l1.append(x)
print(l1)
