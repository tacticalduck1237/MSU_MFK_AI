import numpy as np
a=np.arange(1, int(input())+1)
def check_divisibility(n):
    if n % 3 == 0 and n % 5 == 0:
        return f"FizzBuzz"
    elif n % 3 == 0:
        return f"Fizz"
    elif n % 5 == 0:
        return f"Buzz"
    else:
        return f"{n}"

# Vectorize the function
vectorized_check = np.vectorize(check_divisibility)

# Apply the function to the array
results = vectorized_check(a)

# Print the results
result_string = ' '.join(results)

print(result_string)