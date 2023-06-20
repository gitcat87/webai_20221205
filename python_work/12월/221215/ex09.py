def doA():
    for i in range(5):
        yield i

for i in doA():
    print(i)
    print()

print(next(doA()))
print(next(doA()))
print(next(doA()))
print(next(doA()))


#print()
#print()
#print(doA())
#print()
#print(doA())