def fizz_buzz(n):
#range of numbers 1 to n
    for i in range(1, n + 1):
#If the number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
#If the number is divisible by 3
        elif i % 3 == 0:
            print("Fizz")
#If the number is divisible by 
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage
n = 15
fizz_buzz(n)
