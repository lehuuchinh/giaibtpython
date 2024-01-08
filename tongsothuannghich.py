def tinh_tong_chu_so(n):
    return sum(int(digit) for digit in str(n))
def check_thuan_nghich(n):
    if len(str(n))==1:
        return False
    if str(n)!=str(n)[::-1]:
        return False
    return True

if __name__=="__main__":
    a = int(input())
    for _ in range(a):
        b = input()
        c = tinh_tong_chu_so(b)
        if check_thuan_nghich(c):
            print("YES")
        else:
            print("NO")

