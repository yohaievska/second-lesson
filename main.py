#HW1.1
import string

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

# first_number = int(input("Please enter first number: "))
# operator = input("Please enter a mathematical operator: ")
# second_number = int(input("Please enter second number: "))
#
# if operator == "+":
#     result = first_number + second_number
#     print(f"{first_number} + {second_number} = {result}")
# elif operator == "*":
#     result = first_number * second_number
#     print(f"{first_number} * {second_number} = {result}")
# elif operator == "/":
#     if second_number == 0:
#         print("We're not doing advanced math here... Relax, this isn't rocket science, just enter a different value for the second number.")
#     else:
#         result = first_number / second_number
#         print(f"{first_number} / {second_number} = {result}")
# elif operator == "-":
#     result = first_number - second_number
#     print(f"{first_number} - {second_number} = {result}")
# else:
#     print("Invalid operator")

#HW3.2

# numbers = [1, 5, 3, 7, 5, 4, 6, 2, 9]
#
# if len(numbers) > 1:
#     last = numbers[-1]
#     numbers.insert(0, last)
#     numbers.pop()
#
# print(numbers)

#HW3.3

# #even number
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# middle_numbers = len(numbers) // 2
# if len(numbers) % 2 != 0:
#     middle_numbers += 1
# first_part = numbers[:middle_numbers]
# second_part = numbers[middle_numbers:]
# result = [first_part, second_part]
# print(result)

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

#HW 4.1
# numbers = [4, 0, 0, 17, 23, 0, 8, 0, 5]
# non_zero_numbers = []
# zero_numbers = []
#
# for number in numbers:
#     if number != 0:
#         non_zero_numbers.append(number)
#     else:
#         zero_numbers.append(number)
# result_list = non_zero_numbers + zero_numbers
# print(result_list)

#HW 4.2

# numbers = []
# sum_even = 0
#
# if numbers:
#     last_number = numbers[-1]
#     for i in range(0, len(numbers), 2):
#         if i % 2 == 0:
#             sum_even += numbers[i]
#     result = sum_even * last_number
#     print(result)
# elif len(numbers) == 0:
#     last_number = 0
#     result = sum_even * last_number
#     print(result)

#v2
# numbers = []
#
# result = 0
# if numbers:
#     sum_even = 0
#     last_number = numbers[-1]
#     for i in range(len(numbers)):
#         if i % 2 == 0:
#             sum_even += numbers[i]
#     result = sum_even * last_number
# print(result)


#HW 4.3
# numbers = [1, 2, 3, 4, 5, 6, 7, 9, 10]
# print(numbers[0], numbers[2], numbers[-2])

# HW 5.1

import keyword
import string

name_value = input("Please enter name of value here:")

check_numbers = name_value[0].isalpha() or name_value[0] == "_"
check_characters = not any(char.isupper() for char in name_value)
check_symbols = " " not in name_value and not any(char in string.punctuation and char !="_" for char in name_value) and "__" not in name_value
check_words = not keyword.iskeyword(name_value)

if check_numbers and check_characters and check_symbols and check_words:
    print(True)
else:
    print(False)

# HW 5.2

while True:
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

    repeat = input("Do you want to calculate another number? (y/n): ").lower()
    if repeat != "y":
        print("Thank you for using this program. See you next time!")
        break

#HW 5.3

import string

text_for_hashtag = input("Please enter text for hashtag here: ")

for char in string.punctuation:
    text_for_hashtag = text_for_hashtag.replace(char, "")

text_for_hashtag = text_for_hashtag.lower()
text_for_hashtag = text_for_hashtag.title()

text_for_hashtag = text_for_hashtag.replace(" ", "")

limit_of_letters = ""
count_of_letters = 0

for char in text_for_hashtag:
    if char.isalpha():
        limit_of_letters += char
        count_of_letters += 1
    if count_of_letters == 139:
        break

hashtag = "#" + limit_of_letters

print(hashtag)