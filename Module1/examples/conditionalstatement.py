age = 17
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

grade = 40
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")


x = 5
y = 10

if x > 0 and y > 0:
    print("Both x and y are positive")

if x > 1 or y > 0:
    print("At least one x and y are positive")

if not x > y:
    print("x is not more than y")

x = 11
if x > 10:
    # This block ill me implemented later
    pass
else:
    print("x is not more than 10")