"""5.Given a square matrix of characters write a script that prints the string obtained by going through the matrix in
spiral order (as in the example): =>   first_python_lab"""


def matrix_of_characters(characters, positions):
    my_string = ""
    for line in positions:
        for number in line:
            c_line = positions.index(line)
            c_col = line.index(number)
            my_char = characters[c_line][c_col]
            if number == len(my_string)+1:
                my_string += my_char
            elif number > len(my_string)+1:
                my_string += "*" * (number - len(my_string) - 1)
                my_string += my_char
            else:
                my_string = my_string[:number-1] + my_char + my_string[number:]

    return my_string


def main():

    characters = [["f", "i", "r", "s"],
                  ["n", "_", "l", "t"],
                  ["o", "b", "a", "_"],
                  ["h", "t", "y", "p"]]
    positions = [[1, 2, 3, 4],
                 [12, 13, 14, 5],
                 [11, 16, 15, 6],
                 [10, 9, 8, 7]]
    my_string = matrix_of_characters(characters, positions)
    print(my_string)


if __name__ == "__main__":
    main()
