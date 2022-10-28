"""7.Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract
only the first number that is found."""


def extract_a_number(my_string):
    number = ""
    sign = ""
    point = ""
    for element in my_string:
        if (element == "-" or element == "+") and not sign and not number:
            sign = element
            number += sign
            continue
        if element.isnumeric():
            number += element
            continue
        if element == "." and not point:
            if (not sign and number) or (sign and len(number) > 1):
                point = element
                number += point
                continue
        if not element.isnumeric():
            if (not sign and number) or (sign and len(number) > 1):
                if number[len(number)-1] == ".":
                    number = number[:-1]
                break
            else:
                number = ""
                sign = ""
                point = ""
    return number


def main():

    my_string = "An apple is 123 USD"
    number = extract_a_number(my_string)
    if number:
        print("The number is: ", number)
    else:
        print("There is no number in the string")


if __name__ == "__main__":
    main()
