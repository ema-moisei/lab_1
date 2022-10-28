"""1. Find The greatest common divisor of multiple numbers read from the console."""


def greatest_common_divisors(number_lst):
    div_dict = {}
    nr_list = []
    for number in number_lst:
        div_list = []
        for div in range(2, number):
            nr_pow = 0
            if number % div == 0:
                while number % div == 0:
                    number = number / div
                    nr_pow += 1
                div_list.append(div)
                if div not in div_dict:
                    div_dict[div] = nr_pow
                else:
                    if nr_pow < div_dict[div]:
                        div_dict[div] = nr_pow
        nr_list.append(div_list)
    print(nr_list, "nr list_")
    intersection = nr_list.pop(0)
    print(intersection, "s")
    for second_nr in nr_list:
        print(second_nr, "p")
        intersection = [element for element in intersection if element in second_nr]
    equation = ""
    result = 1
    print(intersection, div_dict, "int")
    for element in intersection:
        result = result * element ** div_dict[element]
        equation = equation + str(element) + " ^ " + str(div_dict[element]) + " * "
    equation = equation[:-3] + " = "

    return result, equation


def main():
    nr_list = []
    loop = 1
    print("Insert the numbers you want to find the greatest common divisor for. Insert \"0\" when ready: ")
    while loop:
        number = int(input())
        loop = number
        if number:
            nr_list.append(number)
    result, equation = greatest_common_divisors(nr_list)
    print("The greatest common divisor of: ", nr_list, "is:")
    print(equation, result)


if __name__ == "__main__":
    main()
