def check_snt(n):
    if n<1:
        return False
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def dem_so_nt(n):
    a = 0
    for i in range(1,n):
        if gcd(i,n)==1:
            a = a + 1
    return a
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a





if __name__=="__main__":
    a = int(input())
    for i in range(a):
        b = int(input())
        c = dem_so_nt(b)

        if check_snt(c):
            print("YES")
        else:
            print("NO")




