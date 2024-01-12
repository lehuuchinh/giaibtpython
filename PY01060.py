def tong_cac_chu_so_vi_tri_chan(n):
    a = str(n)
    b = []
    for i in range(1,len(a),2):
        c = int(a[i])
        b.append(c)

    return sum(b)
def tich_cac_chu_so_vi_tri_le(n):
    a = str(n)
    b = []
    for i in range(0, len(a), 2):
        c = int(a[i])
        b.append(c)
    c = [e for e in b if e != 0]
    tich = 1
    for j in c:
        tich *= j
    return tich
if __name__=="__main__":
    for i in range(int(input())):
        nhapso = int(input())
        print(tich_cac_chu_so_vi_tri_le(nhapso), tong_cac_chu_so_vi_tri_chan(nhapso))

