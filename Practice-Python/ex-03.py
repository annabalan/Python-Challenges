#  Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that prints out all the elements of the list that are less than 5.
numbers = [1, 3, 3, 5, 7, 11, 13, 17, 39]
def below_five(numbers):
    for number in numbers:
        if number <= 5:
            print(number)
        else:
            print("Number greater than 5.")
below_five(numbers)
