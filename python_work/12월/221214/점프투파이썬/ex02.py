score = [90,25,40,80,75]

number = 0
for score in score:
    number = number + 1
    if score >=60:
        print("%d번 학생은 합격입니다."%number)
        print("축하합니다! 합격입니다")
        print()
        continue
        