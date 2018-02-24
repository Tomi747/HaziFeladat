def feladat_1(n1,n2):
    n1=n1+n2
    n2=n1-n2
    n1=n1-n2
    print(n1,n2)

def feladat_2(a,b,c):
    if a<b and a<c:
        if b<c:
            print(a,b,c)
        else:
            print(a,c,b)
    elif b<a and b<c:
        if a<c:
            print(b,a,c)
    else:
        if a<b:
            print(c,a,b)
        print(c,b,a)


def feladat_3(x):
    if x>-2 and x<0:
        return 2*x
    elif x>=0 and x<2:
        return x*x
    elif x>2:
        return 10
    return "Nem megfelelő az x!"

def feladat_4(a,b,c):
    return min(a,b,c),max(abs(a),abs(b),abs(c))

def feladat_5(a,b,c,d):
    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)

def feladat_6(a,b,c):
    if a+b>c and a+c>b and c+b>a:
        s=(a+b+c)/2
        T=(s*(s-a)*(s-b)*(s-c))**0.5
        r=T/s
        R=a*b*c/(4*T)
        print(r,R)
    else:
        print("Nem szerkeszthető a háromszög")

def feladat_7(a,b,drot):
    K=2*a+2*b
    if K>drot:
        return "%.0f drót kell még!" %(K-drot)
    else:
        return "%.0f drót maradt ki!" %(drot-K)

def feladat_8(x,a,b,c,d):
    if x<5:
        x=3*x-5
    elif x<=10 and x>=5:
        x=10
    else:
        x=9*x+1
    if a+c>2*d and b>0:
        E=d-3*b
    elif a+c<2*d and b<0:
        E=d+3*b
    else:
        E=4
    return x,E

def feladat_10(a,b):
    db=0
    if a<b:
        for i in range (a,b+1):
            if i%4==0 and i%100!=0:
                db+=1
            elif i%400==0:
                db+=1
    else:
        for i in range (b,a+1):
            if i%4==0 and i%100!=0:
                db+=1
            elif i%400==0:
                db+=1
    return db

def feladat_11():
    datum=input("Kérem a mai dátumot ÉÉÉÉ.HH.NN formátumban")
    lista=datum.split(".")
    ev=int(lista[0])
    honap=int(lista[1])
    nap=int(lista[2])
    evek=ev-1997
    honapok=honap-12
    napok=nap-29
    szokoev=feladat_10(1997,ev)

def feladat_12(pont):
    max=int(input("Mennyi volt az elérhető pont? "))
    szazalek=pont/max*100
    if szazalek>=60:
        return "sikeres"
    else:
        return "sikertelen"
def feladat_13(jegy):
    if jegy==1:
        print("elégtelen")
    elif jegy==2:
        print("elégséges")
    elif jegy==3:
        print("közepes")
    elif jegy==4:
        print("jó")
    elif jegy==5:
        print("jeles")
    else:
        print("A jegy nem megfelelő")

def feladat_14(a):
    if a==1:
        print("Január")
    elif a==2:
        print("Február")
    elif a==3:
        print("Március")
    elif a==4:
        print("Április")
    elif a==5:
        print("Május")
    elif a==6:
        print("Június")
    elif a==7:
        print("Július")
    elif a==8:
        print("Augusztus")
    elif a==9:
        print("Szeptember")
    elif a==10:
        print("Október")
    elif a==11:
        print("November")
    elif a==12:
        print("December")
    else:
        print("Nem megfelelő a hónap sorszáma")

def feladat_15(a,b):
    hanyados=0
    while a>=b:
        hanyados+=1
        a=a-b
    return hanyados






def main():
    feladat_1(5,3)
    feladat_2(-10.32,3,22)
    print(feladat_3(1.99))
    print(feladat_4(3,0,-19))
    feladat_5(12,32,1,5)
    feladat_6(3,4,5)
    print(feladat_7(43,243,34))
    print(feladat_8(2,5,3,5.5,7))
    print(feladat_10(2018,1956))
    print(feladat_12(61))
    feladat_13(5)
    feladat_14(12)
    print(feladat_15(9,5))
if __name__ == '__main__':
    main()