user_input = input()
emoticons = ""
for i in range(len(user_input)):
    if user_input[i] == ":":
        emoticons += user_input[i]
        emoticons += user_input[i+1]
        print(emoticons)
        emoticons = ""
