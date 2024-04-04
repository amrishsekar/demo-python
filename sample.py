print("Hello Team")


# This program adds two numbers
num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print(f"The sum of {num1} and {num2} is {sum}")


# Python Program to calculate the square root

# Note: change this value for a different result
num = 8 

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
