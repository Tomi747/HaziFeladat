
import math

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

def feladat_9(a,b,c):
    if a==0:
        if b == 0 and c == 0:
            return "Bármely valós szám megoldás"
        elif b==0 and c!=0:
            return "Nincs megoldás"
        elif b!=0:
            x=-1*(c/b)
            return x
    else:
        if b**2-4*a*c>=0:
            if b**2-4*a*c==0:
                megoldas = -1 * (b / (2 * a))
                return megoldas
            else:
                megoldas1 = (-b + ((b ** 2 - 4 * a * c) ** 0.5)) / 2 * a
                megoldas2 = (-b - ((b ** 2 - 4 * a * c) ** 0.5)) / 2 * a
                return megoldas1, megoldas2
        else:
            return "Nincs valós gyök"

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
    datum = input("Kérem a mai dátumot ÉÉÉÉ.HH.NN formátumban: ")
    lista = datum.split(".")
    ev = int(lista[0])
    honap = int(lista[1])
    nap = int(lista[2])
    evek = ev - 1997
    honapok = honap - 12
    napok = nap - 29
    szokoev_db = feladat_10(1997,ev)
    if napok<0:
        honapok=honapok-1
    if honapok<0:
        evek=evek-1
    honapok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if honap == 1:
        hanyadik = nap
    elif honap == 2:
        hanyadik = honapok[0] + nap
    elif honap == 3:
        hanyadik = sum(honapok[1:3]) + nap
    elif honap == 4:
        hanyadik = sum(honapok[1:4]) + nap
    elif honap == 5:
        hanyadik = sum(honapok[1:5]) + nap
    elif honap == 6:
        hanyadik = sum(honapok[1:6]) + nap
    elif honap == 7:
        hanyadik = sum(honapok[1:7]) + nap
    elif honap == 8:
        hanyadik = sum(honapok[1:8]) + nap
    elif honap == 9:
        hanyadik = sum(honapok[1:9]) + nap
    elif honap == 10:
        hanyadik = sum(honapok[1:10]) + nap
    elif honap == 11:
        hanyadik = sum(honapok[1:11]) + nap
    elif honap == 12:
        hanyadik = sum(honapok[1:12]) + nap
    eltem=evek*365+szokoev_db+hanyadik
    return eltem

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

def feladat_16(a,b):
    r=a%b
    while r!=0:
        r=a%b
        a=b
        b=r
    return a

def feladat_17(a):
    masolat=a
    ujszam=0
    while a>0:
        szamjegy=a%10
        ujszam=ujszam*10+szamjegy
        a=a//10
    if ujszam==masolat:
        return "Palindrom-szám"
    else:
        return "Nem palindrom"

def feladat_18(a,b):
    x=a
    y=b
    eredmeny=0
    while x>0:
        if x%2!=0:
            eredmeny=eredmeny+y
        x=x//2
        y=y+y
    return eredmeny

def feladat_19(n):
    valasz=True
    osztok_szama=0
    for i in range(2,int(n/2)):
        if n%i==0:
            valasz=False
    return valasz

def feladat_20(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        if n==2:
            print(a,b)
        else:
            c=a+b
            print(a,b,c, end=' ')
            k=3
            while k<n:
                a=b
                b=c
                c=a+b
                print(c, end=' ')
                k=k+1
                if k==n:
                    a = b
                    b = c
                    c = a + b
                    print(c)
                    k = k + 1

def feladat_21(n):
    ujszam=0
    while n!=0:
        ujszam=ujszam*10+n%10
        n=n//10
    print(ujszam)

def feladat_22(x,n):
    eredmeny=1
    while n>0:
        if n%2==1:
            eredmeny=eredmeny*x
            n=n-1
        x=x*x
        n=n/2
    return eredmeny

def feladat_23(n):
    def feladat_23(n):
        li = []
        i = 1
        while len(li) != n:
            s = 0
            for j in range(1, int(i / 2) + 1):
                if i % j == 0:
                    s = s + j
            if s == i:
                li.append(i)
            i = i + 1
        print(li)

def feladat_24():
    db_7=0
    db_3=0
    a=1
    while a!=0:
        a=int(input("Kérek egy számot: "))
        if a%7==5:
            db_7=db_7+1
        elif a%13==7:
            db_3=db_3+1
    print(db_7,db_3)

def feladat_25():
    a=int(input("Kérem a lakosok számát: "))
    b=int(input("Kérem a terület nagyságát: "))
    print("Az ország népsűrűsége {0} fő/km2" .format(a/b))
    if a/b<=50:
        print("Ritkán lakott")
    elif a/b>50 and a/b<=300:
        print("Átlagos népsűrűségű")
    else:
        print("Sűrűn lakott")

def feladat_26():
    s=0
    pozitív=0
    negativ=0
    a=1
    while a!=0:
        a=int(input("Kérek egy számot: "))
        if a<0:
            negativ=negativ+1
        else:
            pozitív=pozitív+1
        s=s+a
        print(s)
    print("{0} db pozitív és {1} db negatív szám volt" .format(pozitív,negativ))

def feladat_27():
    pozitiv=0
    negativ=0
    k=True
    i=0
    minusz_plusz=False
    plusz_minusz=False
    while k:
        a=int(input("Kérek egy számot: "))
        if i!=0 and minusz_plusz==True and a>0:
            pozitiv=pozitiv+1
            return "{0} db pozitív és {1} db negatív szám volt".format(pozitiv, negativ)
            break
        elif i!=0 and plusz_minusz==True and a<0:
            negativ=negativ+1
            return "{0} db pozitív és {1} db negatív szám volt".format(pozitiv, negativ)
            break
        else:
            b=int(input("Kérek egy számot: "))
            if a<0 and b>0:
                minusz_plusz=True
                negativ=negativ+1
                pozitiv=pozitiv+1
            elif a>0 and b<0:
                plusz_minusz=True
                pozitiv=pozitiv+1
                negativ=negativ+1
            elif a<0 and b<0:
                k=False
                negativ=negativ+2
                return "{0} db pozitív és {1} db negatív szám volt".format(pozitiv, negativ)
            else:
                k=False
                pozitiv=pozitiv+2
                return "{0} db pozitív és {1} db negatív szám volt".format(pozitiv, negativ)
            i=i+1

def feladat_28(n):
    li=[]
    for i in range(1,n+1):
        gyok=i**0.5
        if gyok==int(gyok):
            li.append(i)
    return li[-1]

def feladat_29(n):
    fakt=1
    for i in range(1,n+1):
        fakt=fakt*i
    return fakt

def feladat_30():
    datum=input("Kérek egy dátumot: ")
    li=datum.split(".")
    ev=int(li[0])
    honap=int(li[1])
    nap=int(li[2])
    hanyadik=0
    honapok=[31,28,31,30,31,30,31,31,30,31,30,31]
    if honap==1:
        hanyadik=nap
    elif honap==2:
        hanyadik=honapok[0]+nap
    elif honap==3:
        hanyadik=sum(honapok[1:3])+nap
    elif honap==4:
        hanyadik = sum(honapok[1:4]) + nap
    elif honap==5:
        hanyadik = sum(honapok[1:5]) + nap
    elif honap==6:
        hanyadik = sum(honapok[1:6]) + nap
    elif honap==7:
        hanyadik = sum(honapok[1:7]) + nap
    elif honap==8:
        hanyadik = sum(honapok[1:8]) + nap
    elif honap==9:
        hanyadik = sum(honapok[1:9]) + nap
    elif honap==10:
        hanyadik = sum(honapok[1:10]) + nap
    elif honap==11:
        hanyadik = sum(honapok[1:11]) + nap
    elif honap==12:
        hanyadik = sum(honapok[1:12]) + nap
    if ev%4==0 and ev%100!=0 or ev%400==0:
        hanyadik=hanyadik+1
    print(hanyadik)

def feladat_31(n):
    li=[]
    for i in range(1,int(n/2)+1):
        tort_oszto=n/i
        if tort_oszto==int(n/i):
            li.append(i)
    li.append(n)
    print(li)

def feladat_32(n1,n2,k):
    li=[]
    for i in range(n1-1,n2):
        oszto=i/k
        if oszto==int(i/k):
            li.append(i)
    return li

def feladat_33(n):
    max_oszto_db=0
    szam=0
    for i in range(1,n+1):
        oszto_db=0
        for j in range(1,int(i/2)+1):
            if i%j==0:
                oszto_db=oszto_db+1
        if oszto_db>max_oszto_db:
            max_oszto_db=oszto_db
            szam=i
    return szam

def feladat_34(n):
    primek=[]
    for i in range(2,n+1):
        i_osztoi_db=0
        for j in range(2,i):
            if i%j==0:
                i_osztoi_db=i_osztoi_db+1
        if i_osztoi_db==0:
            primek.append(i)
    print(primek)

def feladat_35(n):
    li=[]
    p=3
    q=5
    while len(li)!=n:
        p_prim_e = True
        for i in range(2, int(p / 2)):
            if p % i == 0:
                p_prim_e = False
        q_prim_e = True
        for j in range(2, int(q / 2)):
            if q % j == 0:
                q_prim_e = False
        if p_prim_e==True and q_prim_e==True:
            li.append((p,q))
        p=p+1
        q=q+1
    print(li)

def feladat_36(n):
    li=[]
    a = 0
    b = 1
    if n == 1:
        li.append(a)
        return 1
    else:
        if n == 2:
            li.append(a)
            li.append(b)
            return 3
        else:
            c = a + b
            li.append(a)
            li.append(b)
            li.append(c)
            k = 3
            while c < n:
                a = b
                b = c
                c = a + b
                li.append(c)
                k = k + 1
                if k==n:
                    a = b
                    b = c
                    c = a + b
                    li.append(c)
                    k = k + 1
                if c>=n:
                    return len(li)-1

def feladat_37(n):
    li = []
    a = 0
    b = 1
    if n == 1:
        li.append(a)
        return 1
    else:
        if n == 2:
            li.append(a)
            li.append(b)
            return 3
        else:
            c = a + b
            li.append(a)
            li.append(b)
            li.append(c)
            k = 3
            while c < n:
                a = b
                b = c
                c = a + b
                li.append(c)
                k = k + 1
                if k == n:
                    a = b
                    b = c
                    c = a + b
                    li.append(c)
                    k = k + 1
    return li[-1]

def feladat_38():
    s=0
    n=input("Kérek egy legfeljebb 9 jegyű számot: ")
    x=input("Kérek egy számjegyet: ")
    for i in n:
        if i==x:
            s=s+1
    return s

def feladat_39():
    li=[]
    for i in range(1,1001):
        if i>10 and i<100:
            szam1=i%10
            szam2=i//10
            if szam1**3+szam2**3==i:
                li.append(i)
        if i>100 and i<1000:
            szam1=i%10
            szam2=(i%100)//10
            szam3=i//100
            if szam1**3+szam2**3+szam3**3==i:
                li.append(i)
    return li

def main():
    feladat_1(5,3)
    feladat_2(-10.32,3,22)
    print(feladat_3(1.99))
    print(feladat_4(3,0,-19))
    feladat_5(12,32,1,5)
    feladat_6(3,4,5)
    print(feladat_7(43,243,34))
    print(feladat_8(2,5,3,5.5,7))
    print(feladat_9(2,7,5))
    print(feladat_10(2018,1956))
    print(feladat_11())
    print(feladat_12(61))
    feladat_13(5)
    feladat_14(12)
    print(feladat_15(9,5))
    print(feladat_16(360,225))
    print(feladat_17(121))
    print(feladat_18(45,17))
    print(feladat_19(17))
    feladat_20(7)
    feladat_21(12345)
    print(feladat_22(5,3))
    feladat_23(3)
    feladat_24()
    feladat_25()
    feladat_26()
    print(feladat_27())
    print(feladat_28(14))
    print(feladat_29(5))
    feladat_30()
    feladat_31(100)
    print(feladat_32(1,20,5))
    print(feladat_33(30))
    feladat_34(8)
    feladat_35(3)
    print(feladat_36(10))
    print(feladat_37(10))
    print(feladat_38())
    print(feladat_39())

if __name__ == '__main__':
    main()