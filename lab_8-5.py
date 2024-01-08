# Define the function factorial that takes a number num as input
def factorial(num):
    # Initialize the result to 1 since multiplying by 1 doesn't change the value
    result = 1
    
    # Iterate from 1 to num (inclusive)
    for i in range(1, num + 1):
        # Multiply the current result by the current value of i
        result *= i
    
    # Return the final result after the loop completes
    return result

# Example usage:
# You can test the function with different numbers
num1 = 5
num2 = 0
num3 = 15
num4 = 6

result1 = factorial(num1)
result2 = factorial(num2)
result3 = factorial(num3)
result4 = factorial(num4)

# Print the results
print(f"The factorial of {num1} is: {result1}")
print(f"The factorial of {num2} is: {result2}")
print(f"The factorial of {num3} is: {result3}")
print(f"The factorial of {num4} is: {result4}")
