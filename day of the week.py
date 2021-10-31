date_input = input("")
dates = list(date_input.strip().split())
y, m, d = int(dates[0]), int(dates[1]), int(dates[2])

if m < 3:
    m += 12
    y -= 1
a = 2 * m + 6 * (m + 1) // 10
b = y + y // 4 - y // 100 + y // 400
f = d + a + b + 1
f = f % 7

print(f)
