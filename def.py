
a = 5

def change(num): #copy by value#這邊a本來應該等於25
    num = 25
    change(a)
print(a)

b = [1,3,5,7,9]

def change(num2)  #copy by reference
    num2[0] = 100
    print(b)
change(b)    
    


    