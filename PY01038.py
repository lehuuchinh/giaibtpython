def so_dao_nguoc(n):
    return str(n)[::-1]

def tong(n):
    sodau = int(n)
    sosau = int(so_dao_nguoc(n))
    ketqua = sodau + sosau
    ketqua += sosau
    return ketqua

if __name__=="__main__":
    dauvao = int(input())
    for _ in range(dauvao):
        nhapso = int(input())
    for i in range(tong(nhapso)):

        if i % 7 == 0:
            print(i)
        else:
            print(-1)
