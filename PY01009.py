def bien_doi_xau(xau):
    sl_chu_hoa = sum(1 for chu in xau if chu.isupper)
    sl_chu_thuong = len(xau) - sl_chu_hoa
    if sl_chu_thuong>sl_chu_hoa:
        return xau.lower()
    if sl_chu_hoa>sl_chu_thuong:
        return xau.upper()
if __name__=='__main__':
    xau = input().strip()
    ket_qua = bien_doi_xau(xau)
    print(ket_qua)