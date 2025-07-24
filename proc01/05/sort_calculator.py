def bubble_sort(numbers):
    # 옆에 있는 숫자와 비교해서 더 큰 숫자를 뒤로 보냄
    # 제일 큰 숫자가 한 칸씩 뒤로 "둥둥" 떠오르는 방식
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def selection_sort(numbers):
    # 남은 숫자들 중에서 가장 작은 걸 찾아서 앞으로 보내는 방식
    # 줄을 서 있는데, 제일 키 작은 친구를 맨 앞으로 부르는 느낌
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

def insertion_sort(numbers):
    # 앞에 있는 숫자들 사이에 알맞은 자리를 찾아 끼워 넣는 방식
    # 숫자를 하나씩 꺼내서 정리된 곳에 정확히 꽂아넣는 느낌
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

def shell_sort(numbers):
    # 멀리 떨어진 숫자끼리 먼저 비교해서 정리하고, 점점 가까운 숫자를 비교하는 방식
    # 큰 걸음으로 정리하다가 점점 작게 정리하는 느낌
    n = len(numbers)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap
            numbers[j] = temp
        gap //= 2
    return numbers

def quick_sort(numbers):
    # 기준이 되는 숫자를 하나 정하고, 그것보다 작은 것과 큰 것을 나눠서 정렬하는 방식
    # 가운데 숫자를 중심으로 양쪽을 나누고, 각각 다시 정렬함
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left = [x for x in numbers[1:] if x < pivot]
    right = [x for x in numbers[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def radix_sort(numbers):
    # 정수를 기준으로 자릿수별로 정렬하는 방식
    # 숫자를 자릿수마다 정리해가며 차례로 정렬
    if not numbers:
        return numbers
    is_float = any('.' in str(num) for num in numbers)
    if is_float:
        print("Radix sort는 정수만 지원합니다.")
        return numbers

    nums = [int(num) for num in numbers]
    max_num = max(nums)
    exp = 1
    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in nums:
            buckets[(num // exp) % 10].append(num)
        nums = [num for bucket in buckets for num in bucket]
        exp *= 10
    return [float(num) for num in nums]

def heapify(arr, n, i):
    # heapify는 부모-자식 구조에서 가장 큰 값을 부모로 만드는 과정
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(numbers):
    # 큰 값을 위로 보내는 힙 구조를 이용한 정렬 방식
    # 트리 구조로 만든 다음, 하나씩 꺼내 정렬
    n = len(numbers)
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)
    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)
    return numbers

def main():
    # ⚠️ 제한사항: sorted() 및 .sort() 사용 금지!
    try:
        print("정렬 알고리즘을 선택하세요:")
        print("1. 거품 정렬 (Bubble Sort)")
        print("2. 선택 정렬 (Selection Sort)")
        print("3. 삽입 정렬 (Insertion Sort)")
        print("4. 셀 정렬 (Shell Sort)")
        print("5. 퀵 정렬 (Quick Sort)")
        print("6. 기수 정렬 (Radix Sort, 정수만 가능)")
        print("7. 힙 정렬 (Heap Sort)")
        method = input("번호를 입력하세요 (1~7): ").strip()

        if method not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Invalid input.")
            return

        user_input = input("숫자들을 공백으로 나눠서 입력하세요 (예: 3 1 4 2): ").strip()
        if not user_input:
            print("Invalid input.")
            return

        tokens = user_input.split()
        numbers = [float(token) for token in tokens]

        if method == "1":
            sorted_numbers = bubble_sort(numbers)
        elif method == "2":
            sorted_numbers = selection_sort(numbers)
        elif method == "3":
            sorted_numbers = insertion_sort(numbers)
        elif method == "4":
            sorted_numbers = shell_sort(numbers)
        elif method == "5":
            sorted_numbers = quick_sort(numbers)
        elif method == "6":
            sorted_numbers = radix_sort(numbers)
        elif method == "7":
            sorted_numbers = heap_sort(numbers)

        formatted = " ".join([str(float(num)) for num in sorted_numbers])
        print(f"Sorted: {formatted}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()