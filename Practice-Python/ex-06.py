# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
user_input = input("Enter a string: ")

#function which return reverse of a string
def reverse(user_input):
    return user_input[::-1]

def ispalinodrome():
    rev = reverse(user_input)
    if rev == user_input:
        print("True")
    else:
        print("False")
ispalinodrome()
