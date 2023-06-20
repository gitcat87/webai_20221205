class A:
    pass
class B:
    pass
a = A()
b = B()

print( 'a. isinstance(A)', isinstance(a,A))
print( 'a. isinstance(B)', isinstance(a,B))

print( 'b. isinstance(A)', isinstance(b,A))
print( 'b. isinstance(B)', isinstance(b,A))


if isinstance(a,A):
    print("a는 A 입니다.")

if isinstance(b,B):
    print("a는 A 입니다.")
