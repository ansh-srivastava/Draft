# how to take input of the string 

my_list = [int(x) for x in input("Enter the list ").split()]
print(my_list) # output = [1, 2, 3, 4, 5]


# how to reverse the list 

emp_list = []
# length = len(my_list)
# for i in range(length,0,-1):
#     emp_list.append(i)
# print(emp_list)
emp_list = my_list[::-1]
print(emp_list)