#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Choose a number: "))
x = list(range(1, num))
divisor_list = []
for number in x:
    if num % number == 0:
        divisor_list.append(number)
print(divisor_list)


