print("당신이 태어난 년도를 입력하세요 : " )
birth_year = int(input())
age = 2019-birth_year +1
print(age)

if age <=26 and age >= 20 :
    print("대학생")
elif age <20 and age >=17 :
    print("고등학생")
elif age <17 and age >=14 :
    print("중학생")
elif age <14 and age >=8 :
    print("초등학생")
else :
    print("학생이 아닙니다")
