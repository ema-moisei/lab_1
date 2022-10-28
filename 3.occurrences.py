"""3.Write a script that receives two strings and prints the number of occurrences of the first string in the second."""


def nr_of_occurrences(string1, string2):
    number = 0
    for element in string2:
        if element == string1[0]:
            index = string2.index(element)
            if string1 == string2[index:index+len(string1)]:
                number += 1
    return number


def main():

    print("Insert a string: ")
    string1 = input("")
    print("Insert an other: ")
    string2 = input("")
    number = nr_of_occurrences(string1, string2)
    print("The number of occurrences of the first string in the second: ", number)


if __name__ == "__main__":
    main()
