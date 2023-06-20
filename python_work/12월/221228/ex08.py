import zipfile

with zipfile.ZipFile('my.zip','w') as f:
    f.write('ex01.py')
    f.write('memo.txt')
    f.write('test.txt')
    