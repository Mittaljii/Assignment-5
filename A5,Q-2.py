#Question 2
#To  print numbers in a given range divisible by a number

#We take range of numbers as input from the user
x1,x2=input("Enter the range of numbers: ").split()
x1=int(x1)
x2=int(x2)
n=int(input("Enter number: "))
for i in range(x1,x2,1):
    if i%n==0: #If it is divisible print the number
        print(i)
        continue
