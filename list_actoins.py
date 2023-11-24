# to initialise a list named 'mylist'
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 2]
print("The list initially ia as:", mylist)
# to print the length of that list in 'length'
print("The length of the list is:", len(mylist))
# to count the occurrence of a particular element (e.g. 1)
print("'1' occurs", mylist.count(1), "times in the list")
# to return the first occurrence of the element
print("'5' is at index", mylist.index(5))
# to append the list and add a new element
mylist.append(99)
print("The appended list is:", mylist)
# to insert an element at specified position
mylist.insert(0, 100)
print("The list after insertion of '100' at index '0' is:", mylist)
# to remove a specified element from the list
mylist.remove(6)
print("The list after removal of '6' is:", mylist)
# to remove and return the last element of the list
print("The last element of the list which will be popped is", mylist.pop())
print("The list after applying POP is:", mylist)
# to extend a list by the elements of new list
my_new_list = [11, 22, 33, 44]
my_new_list.extend(mylist)
print("The new extended list is:", my_new_list)
# to remove an element from a list
my_new_list.remove(100)
print("The list after removing '100' is:", my_new_list)
# to print a list sorted
print("The sorted list is:", sorted(my_new_list), "\n")
# to sort, reverse a list (homogenous)
lis = ["A", "B", "C", "A", "C", "D", "A"]
print("The new list is:", lis)
lis.sort()
print("The sorted new list is:", lis)
lis.reverse()
print("The reversed new list is", lis, "\n")
# miscellaneous operations involving lists
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The list is:", l1)
# print only even nos., then odd nos. from a list
print("Now the even numbers from the list are:")
for i in l1:
    if i % 2 == 0:
        print(i)
print("Now the odd numbers from the list are:")
for i in l1:
    if i % 2 != 0:
        print(i)
# to print the elements with their indices
print("The elements with their +ve and -ve indices are:")
n = len(l1)
for i in range(n):
    print(l1[i], "is at +ve index", i, "and is at -ve index", i-n)
# end
# visit my GitHub repository for this code. 