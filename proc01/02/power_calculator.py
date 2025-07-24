def main():
  """
  Python을 사용하여 제곱 계산 프로그램을 구현한다.

    Python 파일명: power_calculator.py

    구현 요구사항:
        사용자로부터 숫자와 제곱할 횟수(지수)를 입력받음
        입력받은 숫자를 지정한 횟수만큼 거듭제곱한 결과 출력
        Python의 내장 연산자 ** 또는 pow() 함수 사용 금지
        반복문을 사용하여 직접 제곱 계산 구현
        숫자는 float(), 지수는 int()로 형변환

    사용자 입력 예시:

    Enter number: 3
    Enter exponent: 4

    출력 형식:

    Result: 81

    예외 처리:
        숫자 입력이 숫자형이 아닐 경우 "Invalid number input." 출력
        지수 입력이 정수가 아닐 경우 "Invalid exponent input." 출력

    지수가 음수일 때에도 처리:
        음수 지수는 내부적으로 양수 지수만큼 곱한 뒤 결과의 역수(1/result)를 계산
        
    테스트 방식:
        Visual Studio Code에서 power_calculator.py 파일을 열고 터미널에서 python power_calculator.py 명령어로 실행한다.

    프로그램의 실행 로직:

    if __name__ == "__main__":
        main()
  """
  try:
    # 입력받은 숫자를 float로 변경
    number = float(input("Enter number: "))
    # 입력받은 지수는 int로 변경
    exponent = int(input("Enter exponent: "))

    # 0번 지수 처리: 어떤 수든 0번 곱하면 1
    result = 1.0
    count = abs(exponent)

    for _ in range(count):
        result *= number

    # 지수가 음수일 경우 역수 계산
    if exponent < 0:
        result = 1 / result

    # 계산된 결과값을 화면에 출력
    print(f"Result: {result}")

  # 숫자가 아닌 다른 것을 입력했을 때 발생하는 오류를 처리
  except ValueError:
    print("Invalid input. Please enter a valid number and exponent.")
  # 그 외 다른 모든 오류가 발생했을 때 처리
  except Exception as e:
    print(f"An error occurred: {e}")

# 이 파이썬 파일을 직접 실행했을 때만 main 함수를 실행
if __name__ == "__main__":
  main()
