Name = input("Enter your name")
print("Hello" + " " + Name)
#method 1
a = (input("enter the first number"))
b = (input("Enter the second number"))

sum1 = eval(f"{a} + {b}")
print("The sum of {} and {} is {}".format(a, b, sum1))

#method 2
c = (int(input('Enter the first number ')))
d = (int(input('Enter the second number ')))

sum2 = c + d
print("The sum of {} and {} is {}".format(c, d, sum2))