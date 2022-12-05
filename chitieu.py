"""
ứng dụng quản lí chi tiêu chco phép thêm, sửa, xóa
list chi tiêu bao gồm các khoản chi
mỗi khoản chi

khoan_chi = {
    "ten": "mua nha"
    "so_tien" : 2000000
    "date": 18/11/2022
}

"""
def them(chi_tieu, khoan_chi):
    chi_tieu.append(khoan_chi)

def xem(chi_tieu):
    for khoan_chi in chi_tieu:
        print(khoan_chi)
        
def xoa(chi_tieu, ten_chi_tieu):
    index = -1
    for i in range(len(chi_tieu)):
        if ten == khoan_chi[i]["ten"]:
            index = i 
            break
        if index == -1:
            print("Không tìm thấy khoản chi", ten)
        else: 
            chi_tieu.remove(chi_tieu[index])
    
chi_tieu = []

while True:
    yeu_cau = int(input("Ấn 1 để xem chi tiêu\
                    Ấn 2 để thêm chi tiêu\
                    Ấn 3 để xóa chi tiêu"))
    if (yeu_cau == 1): 
        print("Hiện thị các chi tiêu")
        xem(chi_tieu)
    elif (yeu_cau ==2):
        print("Thêm 1 chi tiêu mới")
        ten = input("Nhập vào tên khoản chi: ")
        so_tien = int(input("Nhập vào số tiền: "))
        ngay = input("Nhập vào ngày chi: ")
        khoan_chi= {
            "ten": ten,
            "so_tien": so_tien,
            "ngay": ngay,
        }
        them(chi_tieu, khoan_chi)
    elif (yeu_cau == 3):
        print("Xóa 1 chi tiêu")
        ten = input("Nhập vào tên khoản chi cần xóa:")
        xoa(chi_tieu, ten)
    else: 
        print("Bạn nhập vào không đúng yêu cầu")
    y_o_n = input("Bạn muốn tiếp tục [Y/N]?: ")
    if y_o_n.upper() == "N":
        break