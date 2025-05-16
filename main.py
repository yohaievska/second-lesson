#HW1.1

#print("Hello World")

#HW2.1

# four_digit_number = int(input("Please enter a 4-digit number: "))
# n1 = four_digit_number // 1000
# n2 = four_digit_number % 1000 // 100
# n3 = four_digit_number // 10 % 10
# n4 = four_digit_number % 10

#print(f"{n1}\n{n2}\n{n3}\n{n4}")
#v2:
#print(n1)
#print(n2)
#print(n3)
#print(n4)

#HW2.2

# five_digit_number = int(input("Please enter a 5-digit number: "))
# n1 = five_digit_number // 10000
# n2 = five_digit_number % 10000 // 1000
# n3 = five_digit_number % 1000 // 100
# n4 = five_digit_number % 100 //10
# n5 = five_digit_number % 10
#
# result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
# print(result)

#HW3.1

first_number = int(input("Please enter first number: "))
operator = input("Please enter a mathematical operator: ")
second_number = int(input("Please enter second number: "))

if operator == "+":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
elif operator == "*":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
elif operator == "/":
    if second_number == 0:
        print("We're not doing advanced math here... Relax, this isn't rocket science, just enter a different value for the second number.")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
elif operator == "-":
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
else:
    print("Invalid operator")

#HW3.2

numbers = [1, 5, 3, 7, 5, 4, 6, 2, 9]

if len(numbers) > 1:
    last = numbers[-1]
    numbers.insert(0, last)
    numbers.pop()

print(numbers)

#HW3.3

#even number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
middle_numbers = len(numbers) // 2
if len(numbers) % 2 != 0:
    middle_numbers += 1
first_part = numbers[:middle_numbers]
second_part = numbers[middle_numbers:]
result = [first_part, second_part]
print(result)

#odd number
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# middle_numbers = len(numbers) // 2
# if len(numbers) % 2 != 0:
#     middle_numbers += 1
# first_part = numbers[:middle_numbers]
# second_part = numbers[middle_numbers:]
# result = [first_part, second_part]
# print(result)

#empty list
# numbers = []
# middle_numbers = len(numbers) // 2
# if len(numbers) % 2 != 0:
#     middle_numbers += 1
# first_part = numbers[:middle_numbers]
# second_part = numbers[middle_numbers:]
# result = [first_part, second_part]
# print(result)

