def check_snt(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def so_chu_so_la_snt(n):
    a = str(n)

    if check_snt(len(a)):
        return True
    else:
        return False

def check(n):
    a = str(n)
    b = 0
    c = 0
    for i in a:

        if check_snt(int(i)):
            b += 1
        else:
            c += 1
    return b > c
if __name__=="__main__":
    for i in range(int(input())):
        nhap_so = int(input())
        result = so_chu_so_la_snt(nhap_so) and check(nhap_so)
        print("YES" if result else "NO")
