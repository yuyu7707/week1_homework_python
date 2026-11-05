def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def create_prime_list(n):
    primes = []
    for number in range(1, n + 1):
        if is_prime(number):
            primes.append(number)
    return primes


print(create_prime_list(40))
