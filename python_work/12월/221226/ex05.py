a = [1,5,3,4]
print(sorted(a))
print(a[1]+a[3])

b = ["gg","aa","bbb","cc","kkk"]
print(sorted(b))
print(b[1]+b[3])
print()
print(sorted(b,key=lambda x:len(x)))