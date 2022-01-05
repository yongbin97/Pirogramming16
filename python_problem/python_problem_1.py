num = 0

while num < 31:
    flag=True

    while(flag):
        try:
            inputValue = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
            if inputValue <1 or inputValue>3:
                print("1, 2, 3 중 하나를 입력하세요.")
            else:
                flag = False
        
        except:
            print("정수를 입력하세요.")

    for i in range(inputValue):
        if num + 1 <= 31:
            print("playerA: {}".format(num + 1))
            num += 1
        else:
            break

    flag =True
    while(flag):
        try:
            inputValue = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
            if inputValue <1 or inputValue>3:
                print("1, 2, 3 중 하나를 입력하세요.")
            else:
                flag = False
        
        except:
            print("정수를 입력하세요.")

    for i in range(inputValue):
        if num + 1 <= 31:
            print("playeB: {}".format(num + 1))
            num += 1
        else:
            break
    



