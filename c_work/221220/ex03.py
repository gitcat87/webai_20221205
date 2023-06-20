def sfunc(num):
    num = 30 #값이 30으로 변경
    print("num = ",num)
    return num #지역변수 def sfunc(num)에 있는 값을 age에 입력


def main():
    age = 20
    age = sfunc(age) #age 20의 값을 sfunc(num = age)에 넣어준다
    print("age",age)

if __name__ == "__main__":
    main()