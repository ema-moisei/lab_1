"""9.Write a functions that determine the most common letter in a string. For example if the string is "an apple is not
a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
Casing should not be considered "A" and "a" represent the same character."""


def the_most_common_letter(my_string):
    my_string = my_string.lower()
    chr_string = ""
    nr_string = ""
    for element in my_string:
        if element.isalpha():
            if element not in chr_string:
                chr_string += element
                nr_string += "1"
            else:
                index = chr_string.index(element)
                number = int(nr_string[index]) + 1
                nr_string = nr_string[:index] + str(number) + nr_string[index+1:]
    maximum = 0
    for element in nr_string:
        if nr_string.index(element) == 0:
            maximum = element
            continue
        if int(element) > int(maximum):
            maximum = element
    index = nr_string.index(maximum)
    mcl = chr_string[index]

    return mcl, maximum


def main():

    my_string = "an apple is not a tomato"
    mcl, maximum = the_most_common_letter(my_string)
    print("the most common letter in this string is:", mcl, "(", maximum, "times)")


if __name__ == "__main__":
    main()
