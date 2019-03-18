
User_input = 1
while (User_input is not 0):
    print("구구단 몇 단을 계산할까요(1~9)?")
    User_input = int(input())
    if User_input > 9 :
        print("숫자가 너무 큽니다 1~9사이의 숫자를 입력해주세요")
    elif User_input == 0 :
        print("구구단 게임을 종료합니다 ")
    else :
        print("구구단",User_input,"단을 계산합니다.")
        for i in range(1,10) :
            print(User_input,"X",i,"=",User_input * i)
