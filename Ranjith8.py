numbers = [10, 20, 30, 9]
value = 59

for i in range(len(numbers) - 2):
    for j in range(i + 1, len(numbers) - 1):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == value:
                print(f"The triplet in the list whose sum is equal to {value} is ({numbers[i]}, {numbers[j]}, {numbers[k]}).")
                break
        else:
            continue
        break
    else:
        continue
    break
else:
    print(f"There is no triplet in the list whose sum is equal to {value}.")