# TỔNG CHỮ SỐ THUẬN NGHỊCH
def tong_cac_chu_so(n):
    a = str(n)
    b = []
    for i in a:
        b.append(int(i))
    return sum(b)
def check_thuan_nghich(n):
    so_ban_dau = str(n)
    if len(so_ban_dau) < 2:
        return False
    so_thuan_nghicch = so_ban_dau[::-1]
    return int(so_ban_dau) == int(so_thuan_nghicch)
if __name__=="__main__":
    for i in range(int(input())):
        nhap_so = input()
        tong = tong_cac_chu_so(nhap_so)
        if check_thuan_nghich(tong):
            print("YES")
        else:
            print("NO")
