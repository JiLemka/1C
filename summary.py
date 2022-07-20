inp = open("access.log", 'r')
summary_mass = list()
numbers = inp.read()
numbers = numbers.split(sep="\n")

summary = 0
for i in range(len(numbers)):
    numbers_1 = list(numbers[i])
    numbers_1 = numbers_1[::-1]
    for j in range(len(numbers_1)):
        if numbers_1[j] != " ":
            summary += int(numbers_1[j])
        else:
            break

print(summary)

inp.close()
