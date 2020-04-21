
import math
import re
def int_input(text):
    pattern = r"^[-\d]\d*$"
    user_input = input(text)
    while not re.match(pattern, user_input):
        user_input = input("Введіть ціле число:")
    return int(user_input)

def multiply(x, y):
    if x < 10 and y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = int(math.ceil(float(n) / 2))

    xh = int(math.floor(x / 10  m))
    xl = int(x % (10  m))

    yh = int(math.floor(y / 10  m))
    yl = int(y % (10  m))

    s1 = multiply(xh, yh)
    s2 = multiply(yl, xl)
    s3 = multiply(xh + xl, yh + yl)
    s4 = s3 - s2 - s1

    return int(s1 * (10  (m*2)) + s4 * (10  m) + s2)

x = int_input("Введіть х: ")
y = int_input("Введіть у")
print('Результат: ', multiply(x,y))