num = 0

flag=True

while(flag):
    try:
        inputValue = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
        if inputValue <1 or inputValue>3:
            print("1, 2, 3 중 하나를 입력하세요.")
        else:
            flag = False
            print(inputValue)
    
    except:
        print("정수를 입력하세요.")

for i in range(inputValue):
    print("playerA: {}".format(num + 1))
    num += 1

flag =True
while(flag):
    try:
        inputValue = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
        if inputValue <1 or inputValue>3:
            print("1, 2, 3 중 하나를 입력하세요.")
        else:
            flag = False
            print(inputValue)
    
    except:
        print("정수를 입력하세요.")

for i in range(inputValue):
    print("playerB: {}".format(num + 1))
    num += 1


