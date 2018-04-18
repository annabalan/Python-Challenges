#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
word = input("Enter a string: ")
def word_reverse():
  return ' '.join(word.split()[::-1])
