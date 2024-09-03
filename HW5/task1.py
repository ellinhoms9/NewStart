users_text = input("Please enter some text: ")
# check if an empty string is entered
if len(users_text) == 0:
    print("You have not entered anything.")
else:
    for symbol in users_text:
        # check if the element from input text is a number
        if symbol.isdigit():
            if int(symbol) == 0:
                print(f"This is number: {symbol} and is not even and not odd")
            if int(symbol) % 2 == 0:
                print(f" This is number: {symbol} and is even")
            else:
                print(f" This is number: {symbol} and is odd")
        # check if the element from input text is a word
        elif symbol.isalpha():
            if symbol.islower():
                print(f" This is letter: {symbol} and is lower")
            else:
                print(f" This is letter: {symbol} and is upper")
        else:
            print(f" This is symbol: {symbol}")
