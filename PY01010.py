def dau_cuoi(n):
    dau = str(n)[:2]
    cuoi = str(n)[-2:]
    if dau == cuoi:
        return print("YES")
    else:
        return print("NO")
if __name__=="__main__":
    bo_test = int(input().strip())
    for i in range(bo_test):
        nhap = int(input().strip())
        ket_qua = dau_cuoi(nhap)
