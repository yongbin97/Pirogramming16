class wrongInput(Exception):
    def __init__(self):
        super().__init__('1, 2, 3 중 하나를 입력하세요.')

num = 0
winner = 0
flag=True

while num < 31:
    while(flag):
        try:
            inputValue = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
            if inputValue < 1 or inputValue > 3:
                raise wrongInput
            break

        except ValueError:
            print("정수를 입력하세요.")

        except wrongInput:
            print("1, 2, 3 중 하나를 입력하세요.")

    for i in range(inputValue):
        if num + 1 <= 31:
            print("playerA: {}".format(num + 1))
            num += 1
        else:
            winner = 1
            flag=False
            break
        
    while(flag):
        try:
            inputValue = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
            if inputValue < 1 or inputValue > 3:
                raise wrongInput
            break

        except ValueError:
            print("정수를 입력하세요.")
            
        except wrongInput:
            print("1, 2, 3 중 하나를 입력하세요.")

    for i in range(inputValue):
        if num + 1 <= 31:
            print("playeB: {}".format(num + 1))
            num += 1
        else:
            winner = 2 
            flag=False
            break
    
# if winner == 1:
#     print("PlayerA win")
# else:
#     print("PlayerB win")


