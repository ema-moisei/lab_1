"""2.Write a script that calculates how many vowels are in a string."""


def vowels_calc(string):
    vowel_nr = 0
    vowel = [a, e, i, o, u, A, E, I, O, U]
    for element in string:
        if element in vowel:
            vowel_nr += 1
    return vowel_nr


def main():

    print("Insert a string: ")
    string = input("")


if __name__ == "__main__":
    main()
