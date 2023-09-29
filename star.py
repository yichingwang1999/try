#!/usr/bin/env python3
# n = input("how many * do you want to have : ")
# if n.isdigit():
#   n = int(n)
#   for i in range(n):
#       for j in range(n-i-1):
#           print(" ", end = " ")
#       for j in range(2*i-1):
#           print("*", end = " ")
#       print()   
# else:
#     print("valid number!")

n = 5
for i in range(n):
    for j in range(n-i):
        print(j+1, end = " ")
    print()    