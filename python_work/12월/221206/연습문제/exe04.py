a = "881120-1068234"

year = a[:2]
month = a[2:4]
day = a[3:6]
rest = a[6:]

hongcode = year + month + day + rest

print("hongCode=", hongcode)
