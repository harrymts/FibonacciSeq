# Fibonacci sequence up to n

n = int(input("Enter a number: "))
#This line prompts the user to enter a number and reads the input as an integer.
#The int() function converts the input string to an integer.

a, b = 0, 1
#This line initializes the first two values of the Fibonacci sequence, a and b, to 0 and 1, respectively.
while a < n:
#his line starts a while loop that will continue as long as a is less than the input number n.
    print(a, end=' ')
#This line prints the current value of a to the console, followed by a space. The end='' \
#' argument specifies that a space should be printed after each value, rather than a newline.
    a, b = b, a + b
#This line updates the values of a and b for the next iteration of the loop.
# a is assigned the current value of b, while b is assigned the sum of the current values of a and b.
# This implements the Fibonacci sequence,
# where each subsequent number is the sum of the previous two.
