#Question 6
#To print prime numbers in given range

#We take range of numbers as input from the user
x1,x2=input("Enter the range of numbers: ").split()
x1=int(x1)
x2=int(x2)
for i in range(x1,x2,1):
    c=0
    n=1
    while n<=i:
        if i%n==0:
            c+=1
            n+=1
            continue
        n=n+1        
    if c==2:
        print(i)
print()
