def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_primes_in_range(start, end):
    prime_sum = 0
    for number in range(start, end + 1):
        if is_prime(number):
            prime_sum += number
    return prime_sum
