"""6.Write a function that validates if a number is a palindrome."""


def check_palindrome(number):
    palindrome = True
    element = str(number)
    for first_nr in element[:len(element) // 2]:
        index = element.index(first_nr)
        last_nr = element[(len(element) - 1) - index]
        if not first_nr == last_nr:
            palindrome = False
            break

    return palindrome


def main():

    print("Insert a number: ")
    number = input("")
    palindrome = check_palindrome(number)
    if palindrome:
        print("The number is a palindrome")
    else:
        print("The number is NOT a palindrome")


if __name__ == "__main__":
    main()
