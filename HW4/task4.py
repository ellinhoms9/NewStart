# definition of the data type of the entered text
users_text = input("Please enter some text : ")
# checking the data type and outputting the result
match users_text:
    case "":
        print("You have entered an empty string")
    case str() if users_text.isdigit():
        print("You have entered a number")
    case str() if users_text.isalpha():
        print("You have entered a text")
    case _:
        print("You have entered an invalid character")
