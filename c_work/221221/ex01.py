print(ord('L'))
print(ord('O'))
print(ord('V'))
print(ord('E'))
a = "LOVE"
max = "L"
for item in a:
    if ord(max)<ord(item):
        max =  item

print(f"max = {max}")
