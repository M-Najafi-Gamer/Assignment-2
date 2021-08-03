count = int(input('pls enter the number of students: '))

scores = []
for i in range(count):
    x = float(input(f'pls enter the score of student {i+1}: '))
    scores.append(x)

sum = 0
for item in scores:
    sum += item
avg = sum/count

max = scores[0]
for item in scores:
    if item>max:
        max = item

min = scores[0]
for item in scores:
    if item<min:
        min = item

print(f'Avg is: {avg:.2f}\nMax is: {max}\nMin is: {min}')