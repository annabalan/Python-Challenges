#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
num = int(input("Choose a number: "))
if num > 1:
    for number in range(2,num):
        if (num % number) == 0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number")
else:
    print(num,"is not a prime number")
