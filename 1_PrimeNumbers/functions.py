def is_prime_number(x):
    for i in range(2,x) :
        if (x % i) == 0 :
            return False
    else :
        return True
