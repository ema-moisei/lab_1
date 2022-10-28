"""8.Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format 
is 00011000, meaning 2 bits with value "1" """


def count_bits(number):
    bits = 0
    while number:
        if number % 2 != 0:
            bits += 1
        number = number // 2
    return bits


def main():

    number = 24
    bits = count_bits(number)
    print("Number", number, "has", bits, "bits")


if __name__ == "__main__":
    main()
