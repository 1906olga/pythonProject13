def product_of_numbers (num):
    product = 1
    while num != 0:
        last_digit = num % 10
        if last_digit > 0:
            product*=last_digit
        num = num // 10
    return product
print (product_of_numbers (12057))



