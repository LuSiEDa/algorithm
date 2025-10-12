while True:
    try:
        a, b = map(int, input().split())
        if 0 < a < 10 and 0 < b < 10:
            print(a+b)
        else:
            print("0 이상 10이하의 숫자를 입력해주세요.")
    except EOFError:
        break
    except ValueError:
        print("0 이상 10 이하의 숫자를 입력해주세요.")
        
