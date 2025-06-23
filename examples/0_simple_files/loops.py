for i in range(5):
    print(i)
print('- - - - -')

for i in range(2, 11, 2):
    print(i)

fruits = ["apple", "cherry", "banana"]
for fruits in fruits:
    print(fruits)

text = "Python"
for char in text:
    print(char)

person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, value)

counter = 1
while counter < 5:
    print(counter)
    counter += 1

total = 0
number = 1
while number <= 10:
    total += number
    number += 1
print("Sum of numbers from 1 to 10 is", total)

for i in range(1, 11):
    if i == 6:
        break
    print(i)

for i in range(1, 11):
    if i == 6:
        continue
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        continue