# Problem Statement:
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms


def main():
    max_number = 4000000
    print(sum_of_fibonacci(max_number))


def sum_of_fibonacci(max_number):
    first_number = 1
    second_number = 2
    if max_number < second_number:
        return 0
    elif max_number == second_number:
        return second_number

    total = 0
    while second_number < max_number:
        if second_number % 2 == 0:
            total += second_number
        next_number = first_number + second_number
        first_number = second_number
        second_number = next_number

    return total


if __name__ == '__main__':
    main()
