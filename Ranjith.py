numbers = [10, 501, 22, 37, 100, 999, 87, 351]
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f"The even numbers are {even_numbers}.")
print(f" The odd numbers are {odd_numbers}.")