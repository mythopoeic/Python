def is_prime(x):
    if x == 0 or x == 1 or x < 0:
        print False
        return False
    else:
        for n in range(2, x - 1):
            if x % n == 0:
                print False
                return False
        else:
            print True
            return True

is_prime(10)
is_prime(21)
is_prime(-1)
is_prime(13)
is_prime(0)