def chia_het_cho_3(n):
    if n % 3 == 0:
        return print("YES")
    else:
        return print("NO")
if __name__=="__main__":
    for i in range(int(input())):
        nhap_so = int(input())
        chia_het_cho_3(nhap_so)

