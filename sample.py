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


# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
