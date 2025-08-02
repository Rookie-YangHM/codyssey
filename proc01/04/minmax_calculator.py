def find_min_and_max(numbers):
    # 첫 번째 숫자를 기준으로 가장 작고 큰 값을 시작함
    min_val = numbers[0]
    max_val = numbers[0]
    
    # 나머지 숫자를 하나씩 보면서 비교함
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

def main():
    try:
        # 사용자에게 숫자들을 입력하라고 안내함
        user_input = input("숫자들을 공백으로 나눠서 입력하세요 (예: 3 5 2 8): ")
        
        # 입력한 문장을 띄어쓰기 기준으로 잘라서 숫자 목록으로 만듦
        tokens = user_input.strip().split()
        
        # 각각의 문자열을 숫자(float)로 바꿔서 리스트에 담음
        numbers = [float(token) for token in tokens]
        
        # 직접 만든 함수로 최소값과 최대값을 찾음
        min_val, max_val = find_min_and_max(numbers)
        
        # 결과를 화면에 보여줌
        print(f"Min: {min_val}, Max: {max_val}")
    except ValueError:
        # 숫자가 아닌 것을 입력했을 때 안내 메시지를 보여줌
        print("숫자가 아닌 값이 들어갔어요. 다시 입력해 주세요.")

# 프로그램을 실행할 때 이 아래 코드가 작동함
if __name__ == "__main__":
    main()