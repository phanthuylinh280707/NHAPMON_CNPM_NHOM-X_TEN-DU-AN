# Chương trình kiểm tra số chẵn hay số lẻ

def kiem_tra_chan_le(so):
    if so % 2 == 0:
        return "Số chẵn"
    else:
        return "Số lẻ"

# Chạy thử chương trình
if __name__ == "__main__":
    n = 7  # Bạn có thể thay đổi số này để kiểm tra các số khác
    ket_qua = kiem_tra_chan_le(n)
    print(f"Số {n} là: {ket_qua}")