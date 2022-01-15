
# inputs

volume = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

# calculations

total_p1 = p1 * hours
total_p2 = p2 * hours

pool_fullness_l = total_p2 + total_p1
pool_fullness_percentage = pool_fullness_l / volume
p1_filling_percentage = total_p1 / pool_fullness_l
p2_filling_percentage = total_p2 / pool_fullness_l

pool_overflow = pool_fullness_l - volume

# to percentage

pool_fullness_percentage *= 100
p1_filling_percentage *= 100
p2_filling_percentage *= 100



# decision

if pool_fullness_percentage <= 100:
    print(f"The pool is {pool_fullness_percentage:.2f}% full. Pipe 1: {p1_filling_percentage:.2f}%. Pipe 2: {p2_filling_percentage:.2f}%.")
else:
    print(f'For {hours} hours the pool overflows with {pool_overflow:.2f} liters.')
