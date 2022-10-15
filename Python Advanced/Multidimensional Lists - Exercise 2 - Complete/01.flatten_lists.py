user_input = [y.strip().split() for y in input().split('|')]

nums = [int(x) for lst in user_input[::-1] for x in lst]
result = ' '.join(str(x) for x in nums)
print(result)
