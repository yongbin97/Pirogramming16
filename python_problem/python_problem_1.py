class wrongInput(Exception):
    def __init__(self):
        super().__init__('1, 2, 3 중 하나를 입력하세요.')


def brGame(num, player):
    flag = True
    while flag:
        try:
            inputValue = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "))
            if inputValue < 1 or inputValue > 3:
                raise wrongInput

        except ValueError:
            print("정수를 입력하세요.")

        except wrongInput:
            print("1, 2, 3 중 하나를 입력하세요.")

        else:
            for i in range(inputValue):
                if num + 1 < 31:
                    print("player{}: {}".format(player, num + 1))
                    num += 1

                elif num + 1 == 31:
                    print("player{}: {}".format(player, num + 1))
                    print("Player{} win".format(player))
                    num += 1
                    break

                else:
                    break
            return num

# main code
num = 0
while num < 31:
    num = brGame(num, "A")
    if num < 31:
        num = brGame(num, "B")