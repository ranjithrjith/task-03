def first_non_repeating(numbers):
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    for number in numbers:
        if frequency[number] == 1:
            return number

    return None

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
result = first_non_repeating(numbers)

if result is not None:
    print(f"The first non-repeating element in the list is {result}.")
else:
    print("There are no non-repeating elements in the list.")