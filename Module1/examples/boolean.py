# and, returns true if both operands are true. otherwise it returns false
# or, returns true if at least one of the operands is true. otherwise it returns false
# not, negates the true value of the operand turning to false and vice versa



is_raining = True
is_sunny = False

a = 5
b = 10
result = a > b
print(result)

is_cold = False
bad_weather = is_raining or is_cold
print(f'Weather is bad: {bad_weather}')

really_bad_weather = is_raining and is_cold
print(f"Weather is really bad: {really_bad_weather}")

is_warm = not is_cold
print(is_warm)