#task1 Naive approach
n = int(input("Enter a number: "))
if n <= 1:
    print("Not a Prime Number")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
#optimised approach
n = int(input("Enter a number: "))
if n <= 1:
    print("Not a Prime Number")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
