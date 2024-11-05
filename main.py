def quadraticFormula1(a,b,c):
    d = (b**2-4*a*c)**0.5
    r1 = (-b+d)/(2*a)
    return(r1)

def quadraticFormula2(a,b,c):
    d = (b**2-4*a*c)**0.5
    r2 = (-b-d)/(2*a)
    return(r2)

print("I can solve ax^2+bx+c=0")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("The first root is", quadraticFormula1(a,b,c))
print("The second root is", quadraticFormula2(a,b,c))