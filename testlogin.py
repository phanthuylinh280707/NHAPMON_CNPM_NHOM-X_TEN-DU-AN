def login(username, password):
    if username == "admin" and password == "123456":
        return "Đăng nhập thành công"
    else:
        return "Đăng nhập thất bại"
    
print(login("admin", "123456"))