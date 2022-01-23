
prime_numbers = 0
not_prime_numbers = 0

while True:
    is_prime = True
    is_negative = False

    number = input()
    if number == "stop":
        break
    number_int = int(number)

    if number_int >= 0:

        for i in range(2, int(number_int/2) + 1):

            if (number_int % i) == 0:
                is_prime = False

    else:
        print("Number is negative.")
        is_negative = True

    if is_prime and not is_negative:
        prime_numbers += number_int
    elif not is_prime and not is_negative:
        not_prime_numbers += number_int

print(f"Sum of all prime numbers is: {prime_numbers}\n"
      f"Sum of all non prime numbers is: {not_prime_numbers}")
