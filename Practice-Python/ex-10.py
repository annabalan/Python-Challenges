#This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way. and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).
a_list = [1, 1, 2, 3, 4, 4, 5, 14, 34, 67, 99]
b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(set(a_list) & set(b_list))
