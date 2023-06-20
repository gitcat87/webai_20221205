from ccalcu import Calculator

cal1 =Calculator(10,0)
# cal1.Setdata(10,20)

print(cal1.first)
print(cal1.second)

print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal1.div())
print()
cal1.Setdata(30,16)
print(cal1.mul())

mod = cal1.mod()

print(f"\n mod =  {mod}")