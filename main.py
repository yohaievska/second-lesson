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

# import keyword
# import string
#
# name_value = input("Please enter name of value here:")
#
# check_numbers = name_value[0].isalpha() or name_value[0] == "_"
# check_characters = not any(char.isupper() for char in name_value)
# check_symbols = " " not in name_value and not any(char in string.punctuation and char !="_" for char in name_value) and "__" not in name_value
# check_words = not keyword.iskeyword(name_value)
#
# if check_numbers and check_characters and check_symbols and check_words:
#     print(True)
# else:
#     print(False)

# HW 5.2

# while True:
#     first_number = int(input("Please enter first number: "))
#     operator = input("Please enter a mathematical operator: ")
#     second_number = int(input("Please enter second number: "))
#
#     if operator == "+":
#         result = first_number + second_number
#         print(f"{first_number} + {second_number} = {result}")
#     elif operator == "*":
#         result = first_number * second_number
#         print(f"{first_number} * {second_number} = {result}")
#     elif operator == "/":
#         if second_number == 0:
#             print("We're not doing advanced math here... Relax, this isn't rocket science, just enter a different value for the second number.")
#         else:
#             result = first_number / second_number
#             print(f"{first_number} / {second_number} = {result}")
#     elif operator == "-":
#         result = first_number - second_number
#         print(f"{first_number} - {second_number} = {result}")
#     else:
#         print("Invalid operator")
#
#     repeat = input("Do you want to calculate another number? (y/n): ").lower()
#     if repeat != "y":
#         print("Thank you for using this program. See you next time!")
#         break

#HW 5.3

# import string
#
# text_for_hashtag = input("Please enter text for hashtag here: ")
#
# for char in string.punctuation:
#     text_for_hashtag = text_for_hashtag.replace(char, "")
#
# text_for_hashtag = text_for_hashtag.lower()
# text_for_hashtag = text_for_hashtag.title()
#
# text_for_hashtag = text_for_hashtag.replace(" ", "")
#
# limit_of_letters = ""
# count_of_letters = 0
#
# for char in text_for_hashtag:
#     if char.isalpha():
#         limit_of_letters += char
#         count_of_letters += 1
#     if count_of_letters == 139:
#         break
#
# hashtag = "#" + limit_of_letters
#
# print(hashtag)

#HW 6.1

# import string
#
# ALL_LETTERS = string.ascii_letters
# SEPARATOR = "-"
#
# user_input = input("Please enter 2 letters separated by a hyphen: ").strip()
#
# if len(user_input) == 3:
#     start = user_input[0]
#     end = user_input[2]
#     sep = user_input[1]
#
#     if sep == SEPARATOR and start in ALL_LETTERS and end in ALL_LETTERS:
#         start_index = ALL_LETTERS.index(start)
#         end_index = ALL_LETTERS.index(end)
#         result = ALL_LETTERS[start_index:end_index + 1]
#         print(result)

#HW 6.2

# seconds = int(input("Enter number of seconds (0 - 8640000): "))
#
# # 1 day = 86400 sec
# days, remaining = divmod(seconds, 86400)
# hours, remaining = divmod(remaining, 3600)
# minutes, seconds = divmod(remaining, 60)
#
# if days == 1:
#     day_word = "день"
# elif 2 <= days <= 4:
#     day_word = "дні"
# else:
#     day_word = "днів"
#
# hours = str(hours).zfill(2)
# minutes = str(minutes).zfill(2)
# seconds = str(seconds).zfill(2)
#
# print(f"{days} {day_word}, {hours}:{minutes}:{seconds}")

#HW 6.3

# number = int(input("Enter number: "))
#
# while number > 9:
#     result = 1
#     for digit in str(number):
#         result *= int(digit)
#     number = result
#
# print(number)

#HW 7.1


# def say_hi(name, age):
#     return f"Hi. My name is {name} and I'm {age} years old"
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')

#HW 7.2

# def correct_sentence(text):
#     text = text[0].upper() + text[1:]
#     if text[-1] != ".":
#         text += "."
#     return text
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')

#HW 7.3

# def second_index(text, some_str):
#     first = text.find(some_str)
#     if first == -1:
#         return None
#     second = text.find(some_str, first + len(some_str))
#     return second if second != -1 else None
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')

#HW 7.4

# def common_elements():
#
#     nums = list()
#
#     for i in range(100):
#         # if i % 3 == 0 and i % 5 == 0:
#         if i % 3 == 0:
#             if i % 5 == 0:
#                 nums.append(i)
#     return set(nums)
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print('ОК')

#HW 8.1

# def add_one(some_list):
#     number_str = ""
#     for digit in some_list:
#         number_str += str(digit)
#     number = int(number_str)
#     number += 1
#
#     result = []
#     for char in str(number):
#         result.append(int(char))
#
#     return result
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")

#HW 8.2

# def is_palindrome(text):
#     text = text.lower()
#
#     clean_text = ""
#     for char in text:
#         if char.isalnum():
#             clean_text += char
#
#     return clean_text == clean_text[::-1]
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")

#HW 8.3

# def find_unique_value(some_list):
#     for num in some_list:
#         if some_list.count(num) == 1:
#             return num
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")

#HW 9.1

# def popular_words(text, words):
#
#     text = text.lower()
#     text_words = text.split()
#     result = {}
#
#     for word in words:
#         result[word] = text_words.count(word)
#
#     return result
#
# assert popular_words(
#     '''When I was One I had just begun When I was Two I was nearly new''',
#     ['i', 'was', 'three', 'near']
# ) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
# print('OK')
#
#HW 9.2
#
# def difference(*args):
#     if len(args) == 0:
#         return 0
#     return round(max(args) - min(args), 2)
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')

#HW 10.1

# def some_gen(begin, end, func):
#     current = begin
#     for _ in range(end):
#         yield current
#         current = func(current)
#
# def pow(x):
#     return x ** 2
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')

#HW 10.2

# import re
#
# def first_word(text):
#     match = re.search(r"[a-zA-Z']+", text)
#     return match.group(0) if match else ""
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')

#HW 10.3
# def is_even(digit):
#     return digit % 2 == 0
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')

#HW 11.1

# def prime_generator(end):
#
#     for num in range(2, end + 1):
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield num

# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')

#HW 11.2

# def generate_cube_numbers(end):
#     num = 2
#     while True:
#         cube = num ** 3
#         if cube > end:
#             return
#         yield cube
#         num += 1
#
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
# print('OK')

#HW 11.3

# def is_even(number):
#     return (number & 1) == 0
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
# print('OK')

#HW 12.1

import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned = re.sub(r'<.*?>', '', html, flags=re.DOTALL)

    lines = cleaned.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(non_empty_lines))

delete_html_tags('draft.html')

print('Cleaning is complete. Check the file cleaned.txt')

#HW 12.2

class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name.title()} {self.surname.title()}"


class Purchase:
    def __init__(self, user):
        self.products = {}  # словник: товар -> кількість
        self.user = user

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        all_products = ""
        for product, count in self.products.items():
            all_products += f"\n{product.name}: {count} pcs."
        return f"User: {self.user}\nItems:{all_products}"

    def get_total(self):
        all_sum = 0
        for product, count in self.products.items():
            all_sum += product.price * count
        return all_sum

lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40

# HW 13.1

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o."

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student {self.first_name} {self.last_name}, ID: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)

    def __str__(self):
        all_students = '\n'.join(str(s) for s in self.group)
        return f'Group number: {self.number}\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

# HW 13.2

class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_max):
        self.max_value = max_max

    def set_min(self, min_min):
        self.min_value = min_min

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError('Maximum achieved')

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError('Minimum achieved')

    def get_current(self):
        return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум

assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум

assert counter.get_current() == 7, 'Test4'
