# # # count vowel, consonant, number, symbols in a given string

# my_str = input("Enter the string ")
# splited =[]
# for i in my_str:
#     splited.append(i)
# # print(splited)
# vowel = 0
# conso = 0
# number = 0
# sym = 0
# for j in splited:
#     if j=='a' or j=='A' or j=='e' or j=='E' or j=='o' or j=='O' or j=='i' or j=='I' or j=='u' or j=='U':
#         vowel+=1
#     elif j=='1' or j=='2' or j=='3' or j=='4' or j=='5' or j=='6' or j=='7' or j=='8' or j=='9' or j=='0':
#         number+=1
#     elif j=='!' or j=='@' or j=='#' or j=='$' or j=='%' or j=='^' or j=='&' or j=='*':
#         sym+=1
#     else:
#         conso+=1
# print("Number of Vowel = ",vowel)
# print("Number of Consonant = ",conso)
# print("Number of Symbol = ",sym)
# print("Number of digits = ",number)


# # Palindrome


# num = int(input("enter the number to be checked:- "))
# rev = 0
# copy = num

# while(num>0):
#     rem = num % 10
#     rev = rev*10 + rem
#     num = num // 10

# if copy==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Armstrong

num = int(input("Enter the number to be checked:- "))
cub = 0
copy = num

while(num>0):
    rem = num % 10
    cub = cub + (rem*rem*rem)
    num = num // 10

if copy == cub:
    print("Armstrong")

else:
    print("Not Armstrong")
# Fibonacci
# prime
# odd even
# reverse the string
# Sorting