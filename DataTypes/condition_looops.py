# # # number1 = int(input('Enter the first number: '))
# # # number2 = int(input('Enter the second number: '))

# # # operator = input('Enter the operator: ')

# # # if operator == '+':
# # #     print(number1 + number2)
# # # elif operator == '-':
# # #     print(number1 - number2)
# # # elif operator == '*':
# # #     print(number1 * number2)
# # # elif operator == '/':
# # #     print(number1 / number2)
# # # else:
# # #     print('Invalid operator')


# # #classwork
# # #find the greatest number from a,b,c 
# # #find number is even or odd from input 


# # #for loop 

# # first_list = [1,2,3,4,5,6,7]

# # #find the max number from list 
# # max_number = first_list[0]
# # for elelment in first_list:
# #     if elelment > max_number:
# #         max_number = elelment
        
# # print(max_number)






# # # create dictionary from two given list 

# # a = ['name','age','grade']
# # b = ['xyz',10,2]




# # output = {
# #     'name':'xyz',
# #     'age':10,
# #     'grade':2
# # }


# # for i in range(3):
# #     print(i)


# # #check the existence of element in list 

# # #input list with a search element 
# # #output true or false
# # a=[1,2,5,3,1,6,7,8]
# # search_element = 8 

# # output:Boolean True/False


# # #reverse a list 


# # #find the second largest number from the list



# # #find sub list from list to match a sum value 

# # sum_value = 20
# # listing = [5,4,11,9,3]
# # output = [11,9]



# #reposition all the zeros to end of the list 

# #example
# listing = [1,2,3,4,0,0,0,12]
# listing.sort(reverse=True)
# print(listing)
# outpout = [1,2,3,4,12,0,0,0]



# #break and continue in for loop 
# a = [2,3,1,5,9,8]
# search_num = 1
# for element in a:
#     if element == search_num:
#         print('element found') 
#         break


# #continue 
# voters_age = [18,19,20,21,22,23,24,5]
# for age in voters_age:
#     if age >= 18:
#         print('voter id is being generated')
#         continue

#     print('not a voter')
#     print('voter id is not being generated')
#     remaning_age = 18 - age
#     print(f'{remaning_age}' + ' years remaining')




#while loop 

number = 0 

while number < 10:
    print(number)
    number = number + 1


stored_number = 10
while True:
    number1 = int(input('Enter the number between 1 to 10: '))
    if number1 == stored_number:
        print('number found')
        break


#complete guess number game with good response message to user
    







