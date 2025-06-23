
def hello_world():
    print("Hello World")


hello_world()


def greet(name, age):
    print(f"Hi {name}, you are {age} years old")


greet("Jody", 36)


def sum_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)




sum_numbers(1, 2, 3)
sum_numbers(1, 2, 3, 4, 5)


def display_info(name, age, city="Unknown"):
    print(f" name: {name}, age: {age}, city: {city}")


display_info("Jody", 35)
display_info(name="Doortje", age=63, city="Den Bosch")


def display_fruits(fruits):
    for fruit in fruits:
        print(f"My fruit is : {fruit}")


my_fruits = ["banana", "apple", "kiwi"]
display_fruits(my_fruits)


def multiply(a, b):
    result = a * b
    return result


result = multiply(5,4)
print(result)


def calculate(a,b):
    sum = a + b
    diff = a - b
    return sum, diff


result_sum, result_diff = calculate(7, 3)
print(f"Sum: {result_sum} and Diff: {result_diff}")