print("구구단 계산 프로그램 입니다")
print("몇 단을 계산 할까요?")
User_input = int(input())
print("구구단",(User_input),"단을 계산합니다")

i=1
while i<10 :
    result_1 = (User_input) * i
    print(User_input,"X",i,"=",result_1)
    i = i+1
    
