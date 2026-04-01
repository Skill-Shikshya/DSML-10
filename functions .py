# # # def add(a,b):
# # #     return a+b

# # # #function calling 

# # # # #create simple user defined function like subtract multiply and divide

# # # # def subtract(a,b):
# # # #     return a-b

# # # # def multiply(a,b):
# # # #     return a*b

# # # # def divide(a,b):
# # # #     if b == 0:
# # # #         return "cannot divide by zero"
# # # #     return a/b


# # # # result = divide(10,0)
# # # # print(result)


# # # #classwork
# # # def find_max(**kwargs):
# # #     name = kwargs.get('name')
# # #     age = kwargs.get('age')
# # #     print(name,age)

# # # print(find_max(name = "nepal",age = 20))


# # #class work using arbitary arguments 
# # #check the existence of a particular key in a dictionary

# # def check_key(key,**kwargs):
# #     print(key)
# #     name = kwargs.get('name')
# #     age = kwargs.get('age')
# #     print(name,age)

# # print(check_key('value',name = "nepal",age = 20))


# # #find the sum of all the values in a dictionary 
# # kwargs = {'a': 1, 'b': 2, 'c': 3}

# # def sum_number(**kwargs):
# #     pass

# # result = sum_number(a=10,b=20,c=90,d=100)
# # print(result)

# # #nested function 

# for i in range(5):
#     for j in range(5):
#         print(i,j)

# #classword nested for loop
# #find the sum of all the value in nested for loop


# #nested function to greet 

# def greet(name):
#     def get_message(name):
#         print(f"hello {name}")
#     return get_message(name)

# result = greet('Ram')
# print(result)
# #state rentention counter example
# def parent_counter():
#     count = 0 
#     def child_counter():
#         nonlocal count
#         count += 1
#         return count

#     return child_counter
# counter = parent_counter()
# print(counter())
# print(counter())
# print(counter())
# #classwork for nested function 
# #find the max value from a list of parent scope and pop the max value from the list until the list is empty



# def parent_list():
#     listing = [1,2,3,4,5]
#     def child_list():
#         nonlocal listing
#         max_value = max(listing)
#         listing.remove(max_value)
#         return max_value,listing
#     return child_list


# check = parent_list()
# value_max,array = check()
# print(value_max,array)

# while len(array) > 0:
#     value_max,array = check()
#     print(value_max,array)




#create discount_parent function with nested child function of apply_discount and set_discount
def discount_parent():
    current_discount = 0.1

    def apply_discount(price):
        nonlocal current_discount
        return price * (1 - current_discount)
    def set_discount(discount_rate):
        nonlocal current_discount
        current_discount = discount_rate
    return apply_discount, set_discount


apply_discount, set_discount = discount_parent()
print(apply_discount(100))
set_discount(0.2)
print(apply_discount(100))




#sum of natural nummbers using recursive function
def natural_sum(n):
    if n == 1:
        return 1
    return n + natural_sum(n-1)

print(natural_sum(10))


# #flatten the list using recursive function and find the max value without using built in function

# example_list = [1,2,[3,4,[5,6],7],8,9,[10]]


# result_list = []
# def flatten_list(l):
#     for i in l:
#         if isinstance(i,list):
#             flatten_list(i)
#         else:
#             result_list.append(i)
#     return result_list

# print(flatten_list(example_list))


#higher order function 
#what is higher order function 
#example
def validate_divider(func_add):
    print(func_add)
    def child_function_add(a,b):
        if b == 0:
            return "cannot divide by zero"
        return func_add(a,b)
    return child_function_add

@validate_divider
def divide(a,b):
    return a/b

print(divide)

print(divide(10,2))









