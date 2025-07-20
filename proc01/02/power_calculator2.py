def power(number: float, exponent: int):
    """
    재귀함수 + 반복문을 사용
    number를 exponent만큼 거듭제곱한 값을 반환
    exponent == 0 -> 1
    exponent < 0  -> 재귀 호출로 역수 계산
    exponent > 0  -> 반복문으로 곱셈 수행
    """
    if exponent == 0:
        return 1.0
    if exponent < 0:
        return 1 / power(number, -exponent)
    result = 1.0
    for _ in range(exponent):
        result *= number
    return result

    # return number * power(number, exponent - 1)  # 재귀 호출로 구현할 수도 있음
    # 나중에 해결 ㅡ.ㅡ;;

def main():
    try:
        num = float(input("Enter number: "))
    except ValueError:
        print("Invalid number input.")
        return
    try:
        exp = int(input("Enter exponent: "))
    except ValueError:
        print("Invalid exponent input.")
        return

    try:
        res = power(num, exp)
        print(f"Result: {res}")
    except ZeroDivisionError:
        print("Error: zero cannot be raised to a negative exponent.")

if __name__ == "__main__":
    main()
