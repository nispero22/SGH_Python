# program that print the first N prime numbers

from functions import is_prime_number

#enter a number
print('enter an integer N')
N = int(input())

# if the number is 1
if N == 1 :
    print("one prime number and it is 1")
else:
    print("1 is a prime number")

# if the number is > 1

# n is the number of repetitions
# i is the divisor
# x is the tested number
x = 2

for x in range (2,N+1) :
    if is_prime_number(x) is True:
        print(f"{x} is a prime number")
    else:
        print(f"{x} is not a prime number")

