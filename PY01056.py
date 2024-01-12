
def vi_tri_chan(n):
    a = str(n)
    for i in range(1, len(a), 2):
        chu_so = int(a[i])
        if chu_so % 2 == 0:
            return False
    return True
def vi_tri_le(n):
    a = str(n)
    for i in range(0, len(a),2 ):
        chu_so = int(a[i])
        if chu_so % 2 != 0:
            return False
    return True
def tong_cac_chu_so(n):
    a = str(n)
    tach_so = [int(i) for i in a]
    tong = sum(tach_so)
    for j in range(2, int(tong**0.5)+1):
        if tong % j == 0:
            return False
    return True
if __name__=="__main__":
    for i in range(int(input())):
        nhap_so = input()
        if vi_tri_le(nhap_so) and vi_tri_chan(nhap_so) and tong_cac_chu_so(nhap_so):
            print("YES")
        else:
            print("NO")



