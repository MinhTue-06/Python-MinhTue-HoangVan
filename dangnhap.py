import customtkinter as ctk
from tkinter import messagebox
import pyodbc

# IMPORT CÁC GIAO DIỆN QUẢN LÝ
from QuanLyDiemDen import QuanLyDiemDen
from QuanLyTuyen import QuanLyTuyen
from QuanLyKhachHang import QuanLyKhachHang
from QuanLyDatTour import QuanLyDatTour
from QuanLyTaiKhoan import QuanLyTaiKhoan


# =========================================
# CẤU HÌNH
# =========================================

SERVER_NAME = r'.\SQLEXPRESS01'
DB_NAME = 'QuanLyCacTuyenDuLich'

FONT = "Times New Roman"
MAU_XANH = "#3369A7"
MAU_NEN = "#F3EBDD"


# =========================================
# CHƯƠNG TRÌNH CHÍNH
# =========================================

class UngDung(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("QUẢN LÝ CÁC TUYẾN DU LỊCH")
        self.geometry("1100x650")
        self.resizable(False, False)

        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

        self.configure(fg_color=MAU_NEN)

        self.tai_khoan = None
        self.giao_dien_hien_tai = None

        self.hien_thi_dang_nhap()

    # =====================================
    # KẾT NỐI DATABASE
    # =====================================

    def ket_noi(self):

        try:
            conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={SERVER_NAME};"
                f"DATABASE={DB_NAME};"
                "Trusted_Connection=yes;"
            )

            return conn

        except Exception as e:

            messagebox.showerror(
                "Lỗi kết nối",
                f"Không thể kết nối cơ sở dữ liệu!\n\n{e}"
            )

            return None

    # =====================================
    # XÓA GIAO DIỆN CŨ
    # =====================================

    def xoa_giao_dien(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.giao_dien_hien_tai = None

    # =====================================
    # TRANG ĐĂNG NHẬP
    # =====================================

    def hien_thi_dang_nhap(self):

        self.xoa_giao_dien()

        khung = ctk.CTkFrame(
            self,
            width=450,
            height=460,
            corner_radius=15,
            fg_color="#FBF8F1"
        )

        khung.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        khung.pack_propagate(False)

        # TIÊU ĐỀ LỚN

        ctk.CTkLabel(
            khung,
            text="QUẢN LÝ CÁC TUYẾN DU LỊCH",
            font=(FONT, 23, "bold"),
            text_color=MAU_XANH
        ).pack(pady=(30, 10))

        ctk.CTkLabel(
            khung,
            text="ĐĂNG NHẬP HỆ THỐNG",
            font=(FONT, 19, "bold"),
            text_color="#C62828",
        ).pack(pady=15)

        # TÊN ĐĂNG NHẬP

        ctk.CTkLabel(
            khung,
            text="Tên đăng nhập:",
            font=(FONT, 15)
        ).pack(anchor="w", padx=55)

        self.txtTaiKhoan = ctk.CTkEntry(
            khung,
            width=330,
            height=40,
            font=(FONT, 15),
            placeholder_text="Nhập tên đăng nhập"
        )

        self.txtTaiKhoan.pack(pady=8)

        # MẬT KHẨU

        ctk.CTkLabel(
            khung,
            text="Mật khẩu:",
            font=(FONT, 15)
        ).pack(anchor="w", padx=55, pady=(10, 0))

        self.txtMatKhau = ctk.CTkEntry(
            khung,
            width=330,
            height=40,
            font=(FONT, 15),
            show="*",
            placeholder_text="Nhập mật khẩu"
        )

        self.txtMatKhau.pack(pady=8)

        # HIỆN MẬT KHẨU

        self.hien_mat_khau = ctk.BooleanVar(value=False)

        ctk.CTkCheckBox(
            khung,
            text="Hiện mật khẩu",
            variable=self.hien_mat_khau,
            command=self.bat_tat_mat_khau,
            font=(FONT, 13),
            checkbox_width=18,
            checkbox_height=18
        ).pack(anchor="w", padx=60, pady=5)

        # QUÊN MẬT KHẨU

        ctk.CTkButton(
            khung,
            text="Quên mật khẩu?",
            width=130,
            height=25,
            fg_color="transparent",
            text_color=MAU_XANH,
            hover_color="#EAE2D3",
            font=(FONT, 14, "underline"),
            command=self.quen_mat_khau
        ).pack(anchor="e", padx=55, pady=5)

        # NÚT ĐĂNG NHẬP

        ctk.CTkButton(
            khung,
            text="ĐĂNG NHẬP",
            width=330,
            height=42,
            font=(FONT, 16, "bold"),
            command=self.dang_nhap
        ).pack(pady=18)

        self.txtTaiKhoan.bind(
            "<Return>",
            lambda event: self.dang_nhap()
        )

        self.txtMatKhau.bind(
            "<Return>",
            lambda event: self.dang_nhap()
        )

        self.txtTaiKhoan.focus()

    # =====================================
    # HIỆN / ẨN MẬT KHẨU
    # =====================================

    def bat_tat_mat_khau(self):

        if self.hien_mat_khau.get():

            self.txtMatKhau.configure(show="")

        else:

            self.txtMatKhau.configure(show="*")

    # =====================================
    # QUÊN MẬT KHẨU
    # =====================================

    def quen_mat_khau(self):

        ten_dang_nhap = self.txtTaiKhoan.get().strip()

        if ten_dang_nhap == "":

            messagebox.showwarning(
                "Quên mật khẩu",
                "Vui lòng nhập tên đăng nhập trước!"
            )

            self.txtTaiKhoan.focus()
            return

        conn = self.ket_noi()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute("""
                SELECT HoTen, Email
                FROM TAIKHOAN
                WHERE TenDangNhap = ?
                AND TrangThai = 1
            """, (ten_dang_nhap,))

            tai_khoan = cursor.fetchone()

            if tai_khoan:

                ho_ten = tai_khoan[0]
                email = tai_khoan[1]

                messagebox.showinfo(
                    "Quên mật khẩu",
                    f"Tài khoản: {ten_dang_nhap}\n"
                    f"Họ tên: {ho_ten}\n"
                    f"Email: {email or 'Chưa cập nhật'}\n\n"
                    "Vui lòng liên hệ quản trị viên "
                    "để được cấp lại mật khẩu."
                )

            else:

                messagebox.showerror(
                    "Thông báo",
                    "Tên đăng nhập không tồn tại!"
                )

            cursor.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                str(e)
            )

        finally:

            conn.close()

    # =====================================
    # XỬ LÝ ĐĂNG NHẬP
    # =====================================

    def dang_nhap(self):

        ten_dang_nhap = self.txtTaiKhoan.get().strip()
        mat_khau = self.txtMatKhau.get().strip()

        if not ten_dang_nhap or not mat_khau:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu!"
            )

            return

        conn = self.ket_noi()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute("""
                SELECT MaTaiKhoan, HoTen, Quyen
                FROM TAIKHOAN
                WHERE TenDangNhap = ?
                AND MatKhau = ?
                AND TrangThai = 1
            """, (ten_dang_nhap, mat_khau))

            tai_khoan = cursor.fetchone()

            if tai_khoan:

                self.tai_khoan = {
                    "MaTaiKhoan": tai_khoan[0],
                    "HoTen": tai_khoan[1],
                    "Quyen": tai_khoan[2]
                }

                messagebox.showinfo(
                    "Thông báo",
                    f"Đăng nhập thành công!\n"
                    f"Xin chào {tai_khoan[1]}"
                )

                self.hien_thi_trang_chu()

            else:

                messagebox.showerror(
                    "Đăng nhập thất bại",
                    "Tên đăng nhập hoặc mật khẩu không đúng!"
                )

            cursor.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi đăng nhập",
                str(e)
            )

        finally:

            conn.close()

    # =====================================
    # TRANG CHỦ
    # =====================================

    def hien_thi_trang_chu(self):

        self.xoa_giao_dien()

        # TIÊU ĐỀ

        khung_tieu_de = ctk.CTkFrame(
            self,
            height=100,
            fg_color="#FBF8F1"
        )

        khung_tieu_de.pack(
            fill="x",
            padx=20,
            pady=20
        )

        ctk.CTkLabel(
            khung_tieu_de,
            text="HỆ THỐNG QUẢN LÝ CÁC TUYẾN DU LỊCH",
            font=(FONT, 25, "bold"),
            text_color=MAU_XANH
        ).pack(pady=15)

        # THÔNG TIN TÀI KHOẢN

        ctk.CTkLabel(
            self,
            text=f"Xin chào: {self.tai_khoan['HoTen']}  |  "
                 f"Quyền: {self.tai_khoan['Quyen']}",
            font=(FONT, 16),
            text_color="#333333"
        ).pack(pady=8)

        # KHUNG CHỨC NĂNG

        khung_chuc_nang = ctk.CTkFrame(
            self,
            fg_color="#FBF8F1",
            corner_radius=12
        )

        khung_chuc_nang.pack(
            padx=250,
            pady=8
        )

        ctk.CTkLabel(
            khung_chuc_nang,
            text="DANH SÁCH CHỨC NĂNG",
            font=(FONT, 22, "bold"),
            text_color=MAU_XANH
        ).pack(pady=(15, 10))

        danh_sach = [
            "QUẢN LÝ ĐIỂM ĐẾN",
            "QUẢN LÝ TUYẾN DU LỊCH",
            "QUẢN LÝ KHÁCH HÀNG",
            "QUẢN LÝ ĐẶT TOUR",
            "QUẢN LÝ TÀI KHOẢN"
        ]

        for ten in danh_sach:

            ctk.CTkButton(
                khung_chuc_nang,
                text=ten,
                width=400,
                height=42,
                font=(FONT, 15, "bold"),
                command=lambda t=ten: self.mo_chuc_nang(t)
            ).pack(pady=5)

        # ĐĂNG XUẤT

        ctk.CTkButton(
            self,
            text="ĐĂNG XUẤT",
            width=150,
            height=40,
            fg_color="#C0392B",
            hover_color="#922B21",
            font=(FONT, 15, "bold"),
            command=self.dang_xuat
        ).pack(pady=10)

    # =====================================
    # MỞ CÁC CHỨC NĂNG
    # =====================================

    def mo_chuc_nang(self, ten_chuc_nang):

        danh_sach = {
            "QUẢN LÝ ĐIỂM ĐẾN": QuanLyDiemDen,
            "QUẢN LÝ TUYẾN DU LỊCH": QuanLyTuyen,
            "QUẢN LÝ KHÁCH HÀNG": QuanLyKhachHang,
            "QUẢN LÝ ĐẶT TOUR": QuanLyDatTour,
            "QUẢN LÝ TÀI KHOẢN": QuanLyTaiKhoan
        }

        if ten_chuc_nang not in danh_sach:
            return

        try:

            self.xoa_giao_dien()

            lop_giao_dien = danh_sach[ten_chuc_nang]

            self.giao_dien_hien_tai = lop_giao_dien(
                self,
                self.hien_thi_trang_chu
            )

            self.giao_dien_hien_tai.pack(
                fill="both",
                expand=True
            )

        except Exception as e:

            messagebox.showerror(
                "Lỗi mở chức năng",
                f"Không thể mở {ten_chuc_nang}!\n\n{e}"
            )

            self.hien_thi_trang_chu()

    # =====================================
    # ĐĂNG XUẤT
    # =====================================

    def dang_xuat(self):

        self.tai_khoan = None

        self.hien_thi_dang_nhap()


# =========================================
# CHẠY CHƯƠNG TRÌNH
# =========================================

if __name__ == "__main__":

    app = UngDung()
    app.mainloop()