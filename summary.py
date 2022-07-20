inp = open("access.log", 'r')
numbers = inp.read()
numbers = numbers.split(sep="\n")
summary = 0
summary_mas = ""

for i in range(len(numbers)):
    numbers_1 = list(numbers[i])
    numbers_1 = numbers_1[::-1]
    summary_mas += " "
    for j in range(len(numbers_1)):
        if numbers_1[j] != " ":
            summary_mas += numbers_1[j]
        else:
            break

summary_mas = summary_mas[::-1]
summary_mas = summary_mas.split()

for i in range(len(summary_mas)):
    summary += int(summary_mas[i])

print(summary)
inp.close()
