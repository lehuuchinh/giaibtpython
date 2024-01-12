def tong_cac_chu_so_vi_tri_chan(n):
    a = str(n)
    b = []
    for i in range(0,len(a),2):
        c = int(a[i])
        b.append(c)

    return sum(b)
def tich_cac_chu_so_vi_tri_le(n):
    a = str(n)
    b = []
    d = 0
    e = 0
    for i in range(1, len(a), 2):
        c = int(a[i])
        e += 1
        if c == 0:
            d += 1
        else:
            b.append(c)

    if e == d:
        return 0

    tich = 1

    for j in b:
        tich *= j
    return tich
if __name__=="__main__":
    for i in range(int(input())):
        nhapso = int(input())
        print(tong_cac_chu_so_vi_tri_chan(nhapso), tich_cac_chu_so_vi_tri_le(nhapso))

