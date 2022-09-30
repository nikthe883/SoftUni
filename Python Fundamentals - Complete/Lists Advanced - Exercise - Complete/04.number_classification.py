text_input = [int(x) for x in input().split(', ')]

positive = ", ".join(str(i) for i in [x for x in text_input if x >= 0])
negative = ", ".join(str(i) for i in [x for x in text_input if x < 0])
even = ", ".join(str(i) for i in [x for x in text_input if x % 2 == 0])
odd = ", ".join(str(i) for i in [x for x in text_input if x % 2 != 0])

print(f"Positive: {positive}\n"
      f"Negative: {negative}\n"
      f"Even: {even}\n"
      f"Odd: {odd}")
