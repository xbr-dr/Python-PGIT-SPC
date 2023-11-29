# Set Theory manipulation (Mathematical)

x1 = {10, 20, 30, 40}
y1 = {30, 40, 50, 60}
print(x1.union(y1))  # Takes the union of two sets
print(x1 | y1)  # Alternate method to take the union

x2 = {100, 200, 300, 400}
y2 = {300, 400, 500, 600}
print(x2.intersection(y2))  # Takes the intersection of two sets
print(x2 & y2)   # Alternate way to take intersection

x3 = {10, 20, 30, 40}
y3 = {30, 40, 50, 60}
print(x3.difference(y3))  # Subtracts the elements of y3 from x3
print(x3 - y3)  # Alternate way
print(y3 - x3)  # Alternate way

x4 = {10, 20, 30, 40}
y4 = {30, 40, 50, 60}
print(x4.symmetric_difference(y4))  # Returns elements present in either x or y but not in both
print(x4 ^ y4)  # Alternate way

# Membership operator
s = set("hello")
print(s)
print('h' in s)  # Checks if 'h' is in set s
print('y' in s)  # Prints boolean answer

set1 = {x*x for x in range(5)}  # Stores {0*0, 1*1, 2*2, 3*3, 4*4} in set1
print(set1)
set2 = {x for x in range(1, 11)}  # Stores {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} in set2
print(set2)


