#Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

a_list = [1, 1, 2, 3, 4, 4, 5, 14, 34, 67, 99]
b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c_list = []
for number in a_list:
    if number in b_list:
        c_list.append(number)
print(c_list)
