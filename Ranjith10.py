numbers = [4, 2, -3, 1, 6]
sums = set()
total = 0

for number in numbers:
    total += number
    if total == 0 or total in sums:
        print("There is a sub-list with sum equal to zero.")
        break
    sums.add(total)
else:
    print("There is no sub-list with sum equal to zero.")