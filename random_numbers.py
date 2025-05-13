import random

numbers = range(1, 100)

select = random.sample(numbers, 10)

print(select)

select2 = random.uniform(1, 10)
print(round(select2 * 10, 0))


