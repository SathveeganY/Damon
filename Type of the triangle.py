a = float(input("Enter angle 1: "))
b = float(input("Enter angle 2: "))
c = float(input("Enter angle 3: "))
results = ''
if (a+b+c) == 180:
    if a == 0 or b == 0 or c == 0:
        results = 'Angles do not form a triangle'
    elif a == 90 or b == 90 or c == 90:
        results = 'Right angled'
    elif a > 90 or b > 90 or c > 90:
        results = 'Obtuse angled'
    elif a < 90 or b < 90 or c < 90:
        results = 'Acute angled'

else:results = 'Angles do not form a triangle'

print(results)
