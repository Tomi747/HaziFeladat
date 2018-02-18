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
    print(a,b,d,c)

def feladat_6(a,b,c):
    if a+b>c and a+c>b and c+b>a:
        s=(a+b+c)/2
        T=(s*(s-a)*(s-b)*(s-c))**0.5
        r=T/s
        R=a*b*c/(4*T)
        return r,R
    return "Nem szerkeszthető a háromszög"

def feladat_7(a,b,drot):
    K=2*a+2*b
    if K>drot:
        print("%.0f drót kell még!" %(K-drot))
    else:
        print("%.0f drót maradt ki!" %(drot-K))


def main():
    feladat_1(5,3)
    feladat_2(-10.32,3,22)
    print(feladat_3(1.99))
    print(feladat_4(3,0,-19))
    feladat_5(12,32,1,5)
    print(feladat_6(3,4,5))
    feladat_7(43,243,34)
if __name__ == '__main__':
    main()
