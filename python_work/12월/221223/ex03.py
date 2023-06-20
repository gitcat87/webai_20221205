# print(1e-4)

delta_x = 1e-4

x = 2

def mibun(x):
    return float((x+0.0001)**2-x**2)/float(0.0001)
    #return (x**2+delta_x)-(x**2/delta_x)        
value = mibun(2)
print(value)