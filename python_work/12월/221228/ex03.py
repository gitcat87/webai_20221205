list = []
holsu = []
jjaksu = []
for i in range(10):
    st = input(f"{i+1} 번째 입력")
    intst = int(st)
    list.append(intst)
    if intst%2 ==0:
        jjaksu.append(intst)
    else:
        holsu.append(intst)
reversed_jjaksu = jjaksu[::-1]

print(f"홀수 {holsu}")
print(f"짝수 {reversed_jjaksu}")




