def get_primes(integers: list):
    for number in integers:
        divisions = 0

        for num in range(2, number):
            if number % num == 0:
                divisions += 1

        if divisions == 0 and number >= 2:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))