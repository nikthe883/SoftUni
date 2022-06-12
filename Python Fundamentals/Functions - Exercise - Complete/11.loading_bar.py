user_input = int(input())


def loading_bar(number):
    if number == 100:
        print(f"100% Complete!\n[%%%%%%%%%%]")
    else:
        print(f"{number}% [{(number // 10) * '%'}{(10 - number // 10) * '.'}]\nStill loading...")


loading_bar(user_input)
