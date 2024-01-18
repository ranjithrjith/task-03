numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = []

def is_happy(n):
    seen = set()
    while n != 1:
        n = sum(int(digit) ** 2 for digit in str(n))
        if n in seen:
            return False
        seen.add(n)
    return True

for number in numbers:
    if is_happy(number):
        happy_numbers.append(number)

print(f"There are {len(happy_numbers)} happy numbers in the list: {happy_numbers}.")