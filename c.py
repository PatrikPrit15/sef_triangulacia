dt2 = float(input("Zadaj dt2[s]: "))
dt3 = float(input("Zadaj dt3[s]: "))
v = float(input("Zadaj v zvuku vo vode[ms-1]: "))

ds2 = dt2*v/1000
ds3 = dt3*v/1000

x2,y2=1.5, -3*3**0.5/2
x3,y3=-1.5, -3*3**0.5/2

mi=0.0
ma=1000000.0
x,y=0,0

for i in range(1000):
    if (abs(ma-mi)<1e-12):
        print(f"Program spravil {i} iteracii.")
        break
    r = (ma+mi)/2
    r2 = r+ds2
    r3 = r+ds3

    x = (r2**2 - r3**2)/(2*(x3-x2))
    
    a = 1
    b = -2*y2
    c = -r2**2 + ((x-x2)**2) + y2**2

    y = (-b+(b**2-4*a*c)**0.5)/(2*a)

    if (x**2+y**2<r**2):
        mi=r
    else:
        ma=r

x = round(x,10)
y = round(y,10)
print(f"{x=}, {y=}")


