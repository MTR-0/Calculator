def calculator(num1, num2, op):
    if op == "+":
        return f"Answer: {num1 + num2}"
    elif op == "-":
        return f"Answer: {num1 - num2}"
    elif op == "*":
        return f"Answer: {num1 * num2}"
    elif op == "/":
        return f"Answer: {num1 / num2}"
    else:
        return "Invalid operator."


first_number = int(input("Type the first number: "))
operator = input("Which operator? ")
second_number = int(input("Type the second number: "))
answer = calculator(first_number, second_number, operator)
print(answer)