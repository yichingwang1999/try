#!/usr/bin/env python3
question = input("Do you want pizza?(Y / N)")
if question.isalpha():
    print("Ok , let's check some info about you oizza order!" )

number = input("how many pizza do you want:")
if number.isdigit():
 print(f"i want {number} of pizza")
number2 = input("whats size per pizza?")
if number2.isdigit():
 print(f"i want {number2} per pizza")

 cash = int(number) * int(number2)
 tax = cash * 1.1
 tips = cash* 0.15
 discount = 5

 total = cash + tax + tips - discount
 print(f"Ok! Yor order is {total}. Have a nice day!")