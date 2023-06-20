score = [90,25,40,80,75]

number = 0
for score in score:
    number = number + 1
    if score >=60:
        print("%d번 학생은 합격입니다."%number)
    else:
        print("%d번 학생은 불합격입니다."%number)