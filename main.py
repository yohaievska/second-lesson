#HW1.1

#print("Hello World")

#HW2.1

four_digit_number = int(input("Please enter a 4-digit number: "))
n1 = four_digit_number // 1000
n2 = four_digit_number % 1000 // 100
n3 = four_digit_number // 10 % 10
n4 = four_digit_number % 10

print(f"{n1}\n{n2}\n{n3}\n{n4}")
#v2:
#print(n1)
#print(n2)
#print(n3)
#print(n4)

#HW2.2

five_digit_number = int(input("Please enter a 5-digit number: "))
n1 = five_digit_number // 10000
n2 = five_digit_number % 10000 // 1000
n3 = five_digit_number % 1000 // 100
n4 = five_digit_number % 100 //10
n5 = five_digit_number % 10

result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
print(result)