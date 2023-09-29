#!/usr/bin/env python3
name = input("name :")  #input裡的東西永遠都是string
if name.isalpha():
    print(f"ok! {name} should go to breakfast store")
    cash = input("your cash: ")
    if cash.isdigit():
        cash = int(cash)
        if( cash > 30 ):
            print(f"{name} can buy a sandwish meal and have a nice day")
        elif(30 > cash > 15 ):
            print(f"{name} can buy a coffe only")
        else:
            print(f"{name} need to earn money then you can enjoy tour breakfast") 
else:
    print("please type a valid name.")