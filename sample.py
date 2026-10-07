def calculate_total(price, tax):

    if price > 0:

        if tax > 0:
            total = price + tax
        else:
            total = price

    else:
        total = 0

    return total


password = "123456"

x = 10
y = 20

result = calculate_total(x, y)

print(result)