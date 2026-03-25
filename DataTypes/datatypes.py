# a = True
# # b = False

# # print(a)
# # print(b)

# # print(type(a))
# # print(type(b))

# # print(a+b)
# # print(type(a+b))


# # #arithmetic operator

# # a = 2
# # b = 3

# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)
# # print(a%b)
# # print(a//b)
# # print(a**b)

# # #relational operator
# # a = 2
# # b = 3

# # print(a==b)
# # print(a!=b)
# # print(a>b)
# # print(a<b)
# # print(a>=b)
# # print(a<=b)

# #logical operator
# a = False 
# b = False

# print(a and b)
# print(a or b)
# print(not a)

#identity operator
# a = 2
# b = 3

# print(a is b)
# print(a is not b)

# #membership operator
# a = 9
# b = [1,2,3,4,5,9]

# print(a in b)
# print(a not in b)



#list data type in python 


#insert element in list

#list.insert(index, value)
#list.index(value)

# print(a.index(4))
#list.remove(value)

a = [1,4,3,4,4]
print(id(a))
b= a.copy()
print(id(b))

a = [1,4,3,4,4]
#slicing
print(a[2:])
print(a[:2])
print(a[::2])
print(a[::-1])


#tuple in python 

first_tuple = (1,2,3,4,5,6)
second_tuple = (5,6,7)
print(type(first_tuple))
# #indexing
# print(first_tuple[-2])

# #slicing
# print(first_tuple[1:4])


#concatenation in tuple


#set in python

first_set = {1,2,3,4,5,6}
print(first_set)

#set to list 
first_set = {1,2,3,4,5,6}
first_list = list(first_set)
print(first_list)

#set to tuple
first_set = {1,2,3,4,5,6}
first_tuple = tuple(first_set)
print(first_tuple)
# print(id(first_set))
# print(type(first_set))
# first_set.add(7)
# print(id(first_set))
# print(first_set)

#methods in set

first_set = {1,2,3,4,5,6}
first_set.add(7)
first_set.remove(3)
print(first_set)

#mutiple element add to set 

first_set = {1,2,3,4,5,6}
first_set.update({7,8,9})
#pop method in set 
value = first_set.pop()
print(value)

#remove duplicate element from list without using any condition and loops
duplicate_list = [2,1,1,1,3,4,2,5,4,5]


interesting_set = {True,"nepal",3.4,False}
print(interesting_set)

#another methods 

first_set = {1,2,3,4,5,6}
second_set = {3,4,5,6,7,8}
print(first_set.union(second_set))
print(first_set.intersection(second_set))
print(first_set.difference(second_set))
print(first_set.symmetric_difference(second_set))



# first_set = {1,2,3,4,5,6}
# second_set = {3,4,5,6,7,8}
# print(first_set.isdisjoint(second_set))
# print(first_set.issubset(second_set))
# print(first_set.issuperset(second_set))

#classwork 
#find if the list contains duplicate element
duplicate_list = [1,2,3,1,4,1,2,5,6,7,6]

#remove the duplicate tuple from the list
duplicate_tuple = [(1,2,3),(4,5,6),(7,8,9),(1,2,3)]

#find the comman element from all the given list
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
list3 = [5,6,7,8,9]



