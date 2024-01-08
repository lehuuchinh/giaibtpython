from mypacked import lib_thuan_nghich

if __name__=="__main__":
    a = int(input())
    for _ in range(a):
        b = input()
        c = lib_thuan_nghich.tinh_tong_chu_so(b)
        if lib_thuan_nghich.check_thuan_nghich(c):
            print("YES")
        else:
            print("NO")


