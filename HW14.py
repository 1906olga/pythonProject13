def arithmetic (num1, num2, z):
    if z == "+" :
        return (num1 + num2)
    elif z == "-":
        return (num1 - num2)
    elif z == "*":
        return (num1 * num2)
    elif z == "/":
        return (num1 / num2)
    else:
        return ("Invalid operation")
print (arithmetic(7, 10, '+'))
print (arithmetic(8, 4, '*'))
print (arithmetic(3, 5, '-'))
print (arithmetic(1, 8, '/'))
print (arithmetic(3, 7, '='))