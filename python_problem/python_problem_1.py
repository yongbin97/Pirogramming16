class wrongInput(Exception):
    def __init__(self):
        super().__init__('1, 2, 3 중 하나를 입력하세요.')

num = 0

while num < 31:
    while(num < 31):
        try:
            inputValue = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
            if inputValue < 1 or inputValue > 3:
                raise wrongInput
            break

        except ValueError:
            print("정수를 입력하세요.")

        except wrongInput:
            print("1, 2, 3 중 하나를 입력하세요.")

    if (num <31):
        for i in range(inputValue):
            if num + 1 < 31:
                print("playerA: {}".format(num + 1))
                num += 1

            elif num + 1 == 31:
                print("playerA: {}".format(num + 1))
                print("PlayerA win")
                num += 1
                break

            else:
                break
    
    while(num < 31):
        try:
            inputValue2 = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
            if inputValue2 < 1 or inputValue2 > 3:
                raise wrongInput
            break

        except ValueError:
            print("정수를 입력하세요.")
            
        except wrongInput:
            print("1, 2, 3 중 하나를 입력하세요.")

    if num < 31:
        for i in range(inputValue2):
            if num + 1 < 31:
                print("playerB: {}".format(num + 1))
                num += 1

            elif num + 1 == 31:
                print("playerB: {}".format(num + 1))
                print("PlayerB win")
                num += 1
                break

            else:
                break

