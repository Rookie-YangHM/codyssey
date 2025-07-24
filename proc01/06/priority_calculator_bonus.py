def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

def calculate(tokens):
    try:
        # 0) 괄호 처리: 가장 안쪽 괄호부터 계산
        while '(' in tokens:
            # 가장 마지막 '(' 위치 찾기 (가장 안쪽)
            open_idx = max(i for i, t in enumerate(tokens) if t == '(')
            # 그 뒤 첫 번째 ')' 위치 찾기
            close_idx = next(i for i, t in enumerate(tokens[open_idx+1:], start=open_idx+1) if t == ')')
            # 괄호 안쪽 토큰 계산
            inner_val = calculate(tokens[open_idx+1:close_idx])
            # 괄호 포함 구간을 계산 결과로 치환
            tokens = tokens[:open_idx] + [str(inner_val)] + tokens[close_idx+1:]

        # 1) 토큰을 숫자 리스트와 연산자 리스트로 분리
        nums = [float(tokens[i]) for i in range(0, len(tokens), 2)]
        ops  = [tokens[i]     for i in range(1, len(tokens), 2)]

        # 2) 곱셈·나눗셈 먼저 처리
        i = 0
        while i < len(ops):
            if ops[i] in ("*", "/"):
                a, b = nums[i], nums[i+1]
                nums[i] = multiply(a, b) if ops[i] == "*" else divide(a, b)
                del nums[i+1], ops[i]
            else:
                i += 1

        # 3) 덧셈·뺄셈 처리
        i = 0
        while i < len(ops):
            a, b = nums[i], nums[i+1]
            nums[i] = add(a, b) if ops[i] == "+" else subtract(a, b)
            del nums[i+1], ops[i]

        return nums[0]
    except ZeroDivisionError:
        return "Error: Division by zero."
    except:
        return "Invalid input."

def main():
    print("사칙연산 계산기 (+, -, *, /, 괄호 우선순위 적용)")
    expr = input("식 입력 (예: ( 4 + 5 ) * ( 3 - 2 )): ").strip().split()
    try:
        result = calculate(expr)
        # 최종 결과를 실수로 출력
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    main()