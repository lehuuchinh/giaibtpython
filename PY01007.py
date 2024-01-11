def lai_suat_ngan_hang(a,b,c):
    so_tien_hien_tai = a
    so_nam = 0
    while so_tien_hien_tai<c:
        tien_lai = so_tien_hien_tai*b/100
        so_tien_hien_tai+=tien_lai
        so_nam+=1
    return so_nam

if __name__=='__main__':
    so_bo_test = int(input())
    for i in range(so_bo_test):
        a,b,c = map(float,input().split())
        ket_qua = lai_suat_ngan_hang(a,b,c)
        print(ket_qua)
