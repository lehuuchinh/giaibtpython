def tinh_tong_chu_so(n):
    return sum(int(digit) for digit in str(n))
def check_thuan_nghich(n):
    if len(str(n))==1:
        return False
    if str(n)!=str(n)[::-1]:
        return False
    return True
def lam_tron_so(n):
    # if n > 10:
    #     so_lam_tron = round(n, -1)
    # if n >= 10**2:
    #     so_lam_tron = round(so_lam_tron, -2)
    so_lam_tron = n
    if n >= 10**3:
        if n % 1000 < 500:
            so_lam_tron = round(so_lam_tron, -3)
        else:
            so_lam_tron = round(so_lam_tron + 500, -3)
    if so_lam_tron >= 10**4:
        if so_lam_tron % 10000 < 5000:
            so_lam_tron = round(so_lam_tron, -4)
        else:
            so_lam_tron = round(so_lam_tron + 5000, -4)
    if so_lam_tron >= 10**5:
        if so_lam_tron % 100000 < 50000:
            so_lam_tron = round(so_lam_tron, -5)
        else:
            so_lam_tron = round(so_lam_tron + 50000, -5)
    if so_lam_tron >= 10**6:
        if so_lam_tron % 1000000 < 500000:
            so_lam_tron = round(so_lam_tron, -6)
        else:
            so_lam_tron = round(so_lam_tron + 500000, -6)
    if so_lam_tron >= 10**7:
        if so_lam_tron % 10000000 < 5000000:
            so_lam_tron = round(so_lam_tron, -7)
        else:
            so_lam_tron = round(so_lam_tron + 5000000, -7)
    if so_lam_tron >= 10**8:
        if so_lam_tron % 100000000 < 50000000:
            so_lam_tron = round(so_lam_tron, -8)
        else:
            so_lam_tron = round(so_lam_tron + 50000000, -8)
    return so_lam_tron

def lam_tron_so_1(n):
    b = int(n) % 100
    c = int(n) // 100
    if c > 0:
        if b < 45:
            return c * 100
        if b >= 45:
            return (c + 1) * 100
    else:
        if b < 10:
            return b
        else:
            if (b % 10) < 5:
                return round(b, -1)
            else:
                return round(b + 5, -1)
def lam_tron_bao_quat(n):
    nguong = [10 ** i for i in range(1, 9)]

    for nguong_i in nguong:
        if n >= nguong_i:
            nua_nguong = nguong_i // 2
            if n % nguong_i < nua_nguong:
                n = round(n, -len(str(nguong_i)) + 1)
            else:
                n = round(n + nua_nguong, -len(str(nguong_i)) + 1)

    return n
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def check_snt(n):
    if n<1:
        return False
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def tach_so_thanh_list(n):
    chu_so = []
    while n>0:
        chu_so.insert(0,n%10)
        n //=10
    return chu_so