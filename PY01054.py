def tich_cac_chu_so_in_list(n):
    tach = str(n)
    tach_so = [int(i) for i in tach]
    loai_0 = [j for j in tach_so if j != 0]
    tich = 1
    for c in loai_0:
        tich*=c
    return tich
if __name__=="__main__":
    for i in range(int(input())):
        nhap_so = input()
        kq = tich_cac_chu_so_in_list(nhap_so)
        print(kq)



