# Problem Statement:
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_multiples(max_number, factors):
    total = 0
    for i in range(1, max_number):
        for factor in factors:
            if i % factor == 0:
                total += i
                break

    return total


def main():
    max_number = 1000
    factors = [3, 5]
    print(sum_of_multiples(max_number, factors))


if __name__ == "__main__":
    main()
