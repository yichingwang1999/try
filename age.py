#!/usr/bin/env python3
age = input("age : ")

if age.isdigit():
    age = int(age)
    if(age > 8):
        print("free")
    elif( 65 > age > 8):
        print("pay $50 per person")
    else:
        print("pay $30 per person")
else:
    print("valid age! plz try again!!")        