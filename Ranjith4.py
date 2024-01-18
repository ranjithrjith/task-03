mangoes = [10, 20, 30, 40, 50, 60, 70, 80, 90]
students = 5
mangoes.sort()
min_diff = float('inf')
for i in range(len(mangoes) - students + 1):
    diff = mangoes[i + students - 1] - mangoes[i]
    if diff < min_diff:
        min_diff = diff
        print(f"The minimum difference between the number of mangoes in a bag with maximum mangoes and bag with minimum mangoes given to the student is {min_diff}.")