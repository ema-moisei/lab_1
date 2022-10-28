"""4.Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores."""


def lowercase(my_string):
    new_string = ""
    for element in my_string:
        if 65 <= ord(element) <= 90:
            if not new_string:
                new_string += chr(ord(element) + 32)
            else:
                new_string += "_" + chr(ord(element) + 32)
        elif 97 <= ord(element) <= 122:
            new_string += element
    return new_string


def main():

    print("Insert a string written in UpperCamelCase: ")
    my_string = input("")
    new_string = lowercase(my_string)
    print(new_string)


if __name__ == "__main__":
    main()
