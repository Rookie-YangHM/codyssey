# 💡 4개의 연산 함수를 정의했음

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # 나눗셈에서 b가 0이면 에러 처리
    if b == 0:
        return "Error: Division by zero."
    return a / b


# main 함수처럼 사용하는 코드 블록
if __name__ == "__main__":
    try:
        # 사용자로부터 숫자 2개를 입력받음
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        
        # 연산자 입력
        operator = input("Enter operator (+, -, *, /): ")

        # 연산자에 따라 함수 호출
        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = subtract(a, b)
        elif operator == "*":
            result = multiply(a, b)
        elif operator == "/":
            result = divide(a, b)
        else:
            result = "Invalid operator."  # 잘못된 연산자 처리

        # 결과 출력
        print(f"Result: {result}")
    
    except ValueError:
        # 숫자를 제대로 입력하지 않았을 때 처리
        print("Error: Please enter valid integers.")