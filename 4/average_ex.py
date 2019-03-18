kor_score = [49,79,20,100,80]
math_score =[43,59,85,30,90]
eng_score = [49,79,48,60,100]

midterm_score = [kor_score,math_score,eng_score]
student_score =[0,0,0,0,0]
average_score =[0,0,0,0,0]

for i in range(0,5):
    for j in range(0,3):
        student_score[i] +=midterm_score[j][i]
    average_score[i] = student_score[i]/3
print(average_score)
