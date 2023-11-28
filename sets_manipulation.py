set1 = {10, 20, 10, 20, 30}
length = len(set1)  # To get the length of set
print(length)

# Creation of Set objects
s = {10, 20, 30, 40}
print(s)
print(type(s))

# We can create set objects by using set() function
mylist = [10, 20, 30, 40, 10, 20, 10]
s2 = set(mylist)
print(s2)
# OR
s3 = set(range(5))
print(s3)

# If we take s={}, It is treated as dictionary, not as an empty set, e.g.,
s4 = {}
print(s4)
print(type(s4))

# Some important functions of set.
s5 = {10, 20, 30}
s5.add(40)   # adds 40 to the set
print(s5)

s6 = {10, 20, 30}
list2 = [40, 50, 60, 10]
s6.update(list2, range(5))  # Adds list2 elements as well as range(5)={0,1,2,3,4} elements to the s.
print(s6)

s7 = {10, 20, 30}
s8 = s7.copy()  # Copies s elements to s1.
print(s8)

s9 = {40, 10, 30, 20}
print(s9)
print(s9.pop())   # pop() removes and returns some random element from the set.
print(s9)

s10 = {40, 10, 30, 20}
s10.remove(30)  # It removes specified element from the set.
print(s10)

s11 = {10, 20, 30}
s11.discard(10)
print(s11)
# remove generates error when element is not found while as discard doesn't.

s = {10, 20, 30}
print(s)
s.clear()  # To remove all elements from the Set.
print(s)
# Wait for mathematical operations which will be uploaded as part 2
