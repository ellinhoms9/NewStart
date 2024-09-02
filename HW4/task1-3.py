users_text = input("Enter your text: ")
if users_text.isdigit():
    if int(users_text) % 2 == 0:
        print("This is number and the number is even.")
    else:
        print("This is number and the number is odd.")
else:
    print(f"This is text and them length is {len(users_text)} symbols.")
