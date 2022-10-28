"""10.Write a function that counts how many words exists in a text. A text is considered to be form out of words that
are separated by only ONE space. For example: "I have Python exam" has 4 words."""


def count_words(my_string):
    space = 0
    for element in my_string:
        if element == " ":
            space += 1
    words = space + 1
    return words


def main():

    my_string = "I have Python exam"
    words = count_words(my_string)
    if words > 1:
        print(my_string, "has", words, "words.")
    else:
        print(my_string, "has one word.")


if __name__ == "__main__":
    main()
