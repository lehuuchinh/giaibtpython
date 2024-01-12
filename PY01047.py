def check_snt(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def lay_4_so_cuoi(n):
    a = str(n)
    b = a[-4:]
    if check_snt(int(b)):
        return print("YES")
    else:
        return print("NO")
if __name__=="__main__":
    for i in range(int(input())):
        nhap_so = int(input())
        lay_4_so_cuoi(nhap_so)