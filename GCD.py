def findGCD(a, b):
    while a != 0 and b != 0:
        if abs(a) > abs(b):
            a = a % b
        else:
            b = b % a
    return abs(a + b)


def findLCM(a, b):
    return a * b / findGCD(a, b)


a = int(input("Input a: "))
b = int(input("Input b: "))

print(f'GCD for {a} and {b} is {findGCD(a, b)}')
print(f'LCM for {a} and {b} is {findLCM(a, b)}')