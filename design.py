def tim_so_lon_nhat(danh_sach):
    # Kiểm tra nếu danh sách trống
    if not danh_sach:
        return None
    so_lon_nhat = danh_sach[0]
    for so in danh_sach:
        if so > so_lon_nhat:
            so_lon_nhat = so
            
    return so_lon_nhat

if __name__ == "__main__":
    # Khai báo một danh sách mẫu
    numbers = [12, 45, 7, 23, 56, 89, 34]
    
    # Gọi hàm và in kết quả
    ket_qua = tim_so_lon_nhat(numbers)
    print("Danh sách hiện tại:", numbers)
    print(f"Số lớn nhất trong danh sách là: {ket_qua}")