# 연산 함수 정의

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b


def calculate_expression(expression):
    """문자열 수식(예: '2 + 3')을 계산하는 함수"""
    try:
        parts = expression.strip().split()  # 공백 기준으로 나누기
        if len(parts) != 3:
            return "Error: Invalid expression format."

        a = float(parts[0])
        operator = parts[1]
        b = float(parts[2])

        if operator == "+":
            return add(a, b)
        elif operator == "-":
            return subtract(a, b)
        elif operator == "*":
            return multiply(a, b)
        elif operator == "/":
            return divide(a, b)
        else:
            return "Error: Invalid operator."

    except ValueError:
        return "Error: Please enter numbers only."


if __name__ == "__main__":
    print("🧮 계산기 모드 선택")
    print("1. 숫자 연산자 숫자 입력 (공백으로 구분, 연산자는 하나만, 허용 연산자: +, -, *, /)")
    print("2. 숫자 두 개 입력후, 연산자 입력 (원래 과제)")

    mode = input("Select mode (1 or 2): ")

    if mode == "1":
        expr = input("Enter expression: ")  # 예: 2 + 3
        result = calculate_expression(expr)
        print(f"Result: {result}")

    elif mode == "2":
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            operator = input("Enter operator (+, -, *, /): ")

            if operator == "+":
                result = add(a, b)
            elif operator == "-":
                result = subtract(a, b)
            elif operator == "*":
                result = multiply(a, b)
            elif operator == "/":
                result = divide(a, b)
            else:
                result = "Invalid operator."

            print(f"Result: {result}")
        except ValueError:
            print("Error: Please enter valid integers.")
    else:
        print("Invalid mode selected.")