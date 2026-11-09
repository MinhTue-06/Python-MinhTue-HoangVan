import customtkinter as ctk
from tkinter import ttk, messagebox
import pyodbc


# =========================================================
# CẤU HÌNH
# =========================================================

SERVER_NAME = r'.\SQLEXPRESS01'
DB_NAME = 'QuanLyCacTuyenDuLich'

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


# =========================================================
# CLASS QUẢN LÝ KHÁCH HÀNG
# =========================================================

class QuanLyKhachHang(ctk.CTkFrame):

    def __init__(self, master, quay_lai):
        super().__init__(master, fg_color="#F3EBDD")

        self.quay_lai = quay_lai

        self.create_interface()

    # =====================================================
    # CHUYỂN SANG CHỨC NĂNG KHÁC
    # =====================================================

    def chuyen_chuc_nang(self, ten_chuc_nang):

        ung_dung = self.winfo_toplevel()

        if hasattr(ung_dung, "mo_chuc_nang"):
            ung_dung.mo_chuc_nang(ten_chuc_nang)
        else:
            messagebox.showerror(
                "Lỗi",
                "Không tìm thấy chức năng chuyển trang! Vui lòng đăng nhập để thực hiện!"
            )

    # =====================================================
    # KẾT NỐI SQL SERVER
    # =====================================================

    def get_connection(self):

        try:

            conn_str = (
                "DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={SERVER_NAME};"
                f"DATABASE={DB_NAME};"
                "Trusted_Connection=yes;"
            )

            return pyodbc.connect(conn_str)

        except Exception as e:

            messagebox.showerror(
                "Lỗi kết nối",
                f"Không thể kết nối SQL Server:\n\n{e}"
            )

            return None

    # =====================================================
    # GIAO DIỆN
    # =====================================================

    def create_interface(self):

        # =================================================
        # THANH ĐIỀU HƯỚNG
        # =================================================

        nav_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        nav_frame.pack(
            fill="x",
            padx=15,
            pady=5
        )

        # NÚT QUAY LẠI TRANG CHỦ

        btn_quay_lai = ctk.CTkButton(
            nav_frame,
            text="QUAY LẠI TRANG CHỦ",
            command=self.quay_lai,
            width=155,
            height=35,
            font=("Times New Roman", 12, "bold"),
            fg_color="#57595A",
            hover_color="#3C3F40",
            text_color="white"
        )

        btn_quay_lai.pack(
            side="left",
            padx=3
        )

        # DANH SÁCH CHỨC NĂNG

        cac_chuc_nang = [
            ("QUẢN LÝ ĐIỂM ĐẾN", "QUẢN LÝ ĐIỂM ĐẾN", 135),
            ("QUẢN LÝ TUYẾN DU LỊCH", "QUẢN LÝ TUYẾN DU LỊCH", 155),
            ("QUẢN LÝ KHÁCH HÀNG", "QUẢN LÝ KHÁCH HÀNG", 145),
            ("QUẢN LÝ ĐẶT TOUR", "QUẢN LÝ ĐẶT TOUR", 135),
            ("QUẢN LÝ TÀI KHOẢN", "QUẢN LÝ TÀI KHOẢN", 145)
        ]

        for ten, ma, chieu_rong in cac_chuc_nang:

            dang_mo = ma == "QUẢN LÝ KHÁCH HÀNG"

            btn = ctk.CTkButton(
                nav_frame,
                text=ten,
                command=lambda m=ma: self.chuyen_chuc_nang(m),
                width=chieu_rong,
                height=35,
                font=(
                    "Times New Roman",
                    11,
                    "bold" if dang_mo else "normal"
                ),
                fg_color="#D8C7A5" if dang_mo else "#57595A",
                hover_color="#C7B38D" if dang_mo else "#3C3F40",
                text_color="#333333" if dang_mo else "white"
            )

            btn.pack(
                side="left",
                padx=3
            )

        # =================================================
        # TIÊU ĐỀ
        # =================================================

        title = ctk.CTkLabel(
            self,
            text="QUẢN LÝ KHÁCH HÀNG",
            font=("Times New Roman", 22, "bold"),
            text_color="#3369A7"
        )

        title.pack(pady=10)

        # =================================================
        # KHUNG NHẬP DỮ LIỆU
        # =================================================

        input_frame = ctk.CTkFrame(
            self,
            fg_color="#FBF8F1",
            corner_radius=12
        )

        input_frame.pack(
            fill="x",
            padx=15,
            pady=5
        )

        # =================================================
        # MÃ KHÁCH HÀNG
        # =================================================

        ctk.CTkLabel(
            input_frame,
            text="Mã khách hàng:",
            font=("Times New Roman", 16)
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=6,
            sticky="w"
        )

        self.txtMaKhachHang = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMaKhachHang.grid(
            row=0,
            column=1,
            padx=8,
            pady=6
        )

        # =================================================
        # HỌ TÊN
        # =================================================

        ctk.CTkLabel(
            input_frame,
            text="Họ tên:",
            font=("Times New Roman", 16)
        ).grid(
            row=0,
            column=2,
            padx=8,
            pady=6,
            sticky="w"
        )

        self.txtHoTen = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtHoTen.grid(
            row=0,
            column=3,
            padx=8,
            pady=6
        )

        # =================================================
        # SỐ ĐIỆN THOẠI
        # =================================================

        ctk.CTkLabel(
            input_frame,
            text="Số điện thoại:",
            font=("Times New Roman", 16)
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=6,
            sticky="w"
        )

        self.txtSoDienThoai = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtSoDienThoai.grid(
            row=1,
            column=1,
            padx=8,
            pady=6
        )

        # =================================================
        # EMAIL
        # =================================================

        ctk.CTkLabel(
            input_frame,
            text="Email:",
            font=("Times New Roman", 16)
        ).grid(
            row=1,
            column=2,
            padx=8,
            pady=6,
            sticky="w"
        )

        self.txtEmail = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtEmail.grid(
            row=1,
            column=3,
            padx=8,
            pady=6
        )

        # =================================================
        # ĐỊA CHỈ
        # =================================================

        ctk.CTkLabel(
            input_frame,
            text="Địa chỉ:",
            font=("Times New Roman", 16)
        ).grid(
            row=2,
            column=0,
            padx=8,
            pady=6,
            sticky="w"
        )

        self.txtDiaChi = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtDiaChi.grid(
            row=2,
            column=1,
            padx=8,
            pady=6
        )

        # =================================================
        # KHUNG BẢNG
        # =================================================

        table_frame = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=12
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        # =================================================
        # CẤU HÌNH BẢNG
        # =================================================

        style = ttk.Style()

        style.configure(
            "Treeview",
            font=("Times New Roman", 26),
            rowheight=45,
            background="white",
            foreground="black",
            fieldbackground="white"
        )

        style.configure(
            "Treeview.Heading",
            font=("Times New Roman", 24, "bold"),
            background="#D9D9D9",
            foreground="black"
        )

        style.map(
            "Treeview",
            background=[
                ("selected", "#B7D7F0")
            ],
            foreground=[
                ("selected", "black")
            ]
        )

        # =================================================
        # CỘT BẢNG
        # =================================================

        columns = (
            "MaKhachHang",
            "HoTen",
            "SoDienThoai",
            "Email",
            "DiaChi"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        # =================================================
        # TÊN CỘT
        # =================================================

        self.tree.heading(
            "MaKhachHang",
            text="Mã khách hàng"
        )

        self.tree.heading(
            "HoTen",
            text="Họ tên"
        )

        self.tree.heading(
            "SoDienThoai",
            text="Số điện thoại"
        )

        self.tree.heading(
            "Email",
            text="Email"
        )

        self.tree.heading(
            "DiaChi",
            text="Địa chỉ"
        )

        # =================================================
        # ĐỘ RỘNG CỘT
        # =================================================

        self.tree.column(
            "MaKhachHang",
            width=150,
            anchor="center"
        )

        self.tree.column(
            "HoTen",
            width=220,
            anchor="center"
        )

        self.tree.column(
            "SoDienThoai",
            width=160,
            anchor="center"
        )

        self.tree.column(
            "Email",
            width=220,
            anchor="center"
        )

        self.tree.column(
            "DiaChi",
            width=300,
            anchor="center"
        )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

                # ================= NÚT CHỨC NĂNG =================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(pady=8)

        self.btnThem = ctk.CTkButton(
            button_frame,
            text="THÊM",
            width=150,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#2196F3",
            command=self.them_khach_hang
        )

        self.btnThem.grid(row=0, column=0, padx=10)

        self.btnSua = ctk.CTkButton(
            button_frame,
            text="SỬA",
            width=150,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#FF9800",
            command=self.sua_khach_hang
        )

        self.btnSua.grid(row=0, column=1, padx=10)

        self.btnXoa = ctk.CTkButton(
            button_frame,
            text="XÓA",
            width=150,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#F44336",
            command=self.xoa_khach_hang
        )

        self.btnXoa.grid(row=0, column=2, padx=10)

        self.btnLamMoi = ctk.CTkButton(
            button_frame,
            text="LÀM MỚI",
            width=150,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#607D8B",
            command=self.lam_moi
        )

        self.btnLamMoi.grid(row=0, column=3, padx=10)

        # =================================================
        # CHỌN DÒNG
        # =================================================

        self.tree.bind(
            "<ButtonRelease-1>",
            self.chon_dong
        )

        # =================================================
        # HIỂN THỊ DỮ LIỆU
        # =================================================

        self.hien_thi_khach_hang()

    # =====================================================
    # HIỂN THỊ KHÁCH HÀNG
    # =====================================================

    def hien_thi_khach_hang(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    MaKhachHang,
                    HoTen,
                    SoDienThoai,
                    Email,
                    DiaChi
                FROM KHACHHANG
                ORDER BY MaKhachHang
            """)

            rows = cursor.fetchall()

            for row in rows:

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2] if row[2] else "",
                        row[3] if row[3] else "",
                        row[4] if row[4] else ""
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                f"Không thể hiển thị dữ liệu:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # CHỌN DÒNG
    # =====================================================

    def chon_dong(self, event):

        selected = self.tree.focus()

        if selected == "":
            return

        values = self.tree.item(
            selected,
            "values"
        )

        if not values:
            return

        self.txtMaKhachHang.delete(0, "end")
        self.txtMaKhachHang.insert(0, values[0])

        self.txtHoTen.delete(0, "end")
        self.txtHoTen.insert(0, values[1])

        self.txtSoDienThoai.delete(0, "end")
        self.txtSoDienThoai.insert(0, values[2])

        self.txtEmail.delete(0, "end")
        self.txtEmail.insert(0, values[3])

        self.txtDiaChi.delete(0, "end")
        self.txtDiaChi.insert(0, values[4])

    # =====================================================
    # THÊM KHÁCH HÀNG
    # =====================================================

    def them_khach_hang(self):

        MaKhachHang = self.txtMaKhachHang.get().strip()
        HoTen = self.txtHoTen.get().strip()
        SoDienThoai = self.txtSoDienThoai.get().strip()
        Email = self.txtEmail.get().strip()
        DiaChi = self.txtDiaChi.get().strip()

        if MaKhachHang == "" or HoTen == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập mã khách hàng và họ tên!"
            )

            return

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM KHACHHANG
                WHERE MaKhachHang = ?
                """,
                (MaKhachHang,)
            )

            if cursor.fetchone()[0] > 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Mã khách hàng này đã tồn tại!"
                )

                return

            cursor.execute(
                """
                INSERT INTO KHACHHANG
                (
                    MaKhachHang,
                    HoTen,
                    SoDienThoai,
                    Email,
                    DiaChi
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    MaKhachHang,
                    HoTen,
                    SoDienThoai,
                    Email,
                    DiaChi
                )
            )

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Thêm khách hàng thành công!"
            )

            self.hien_thi_khach_hang()
            self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                f"Không thể thêm khách hàng:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # SỬA KHÁCH HÀNG
    # =====================================================

    def sua_khach_hang(self):

        MaKhachHang = self.txtMaKhachHang.get().strip()
        HoTen = self.txtHoTen.get().strip()
        SoDienThoai = self.txtSoDienThoai.get().strip()
        Email = self.txtEmail.get().strip()
        DiaChi = self.txtDiaChi.get().strip()

        if MaKhachHang == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn khách hàng cần sửa!"
            )

            return

        if HoTen == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập họ tên!"
            )

            return

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE KHACHHANG
                SET
                    HoTen = ?,
                    SoDienThoai = ?,
                    Email = ?,
                    DiaChi = ?
                WHERE MaKhachHang = ?
                """,
                (
                    HoTen,
                    SoDienThoai,
                    Email,
                    DiaChi,
                    MaKhachHang
                )
            )

            if cursor.rowcount == 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy khách hàng cần sửa!"
                )

                return

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Sửa khách hàng thành công!"
            )

            self.hien_thi_khach_hang()
            self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                f"Không thể sửa khách hàng:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # XÓA KHÁCH HÀNG
    # =====================================================

    def xoa_khach_hang(self):

        MaKhachHang = self.txtMaKhachHang.get().strip()

        if MaKhachHang == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn khách hàng cần xóa!"
            )

            return

        xac_nhan = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc muốn xóa khách hàng này không?"
        )

        if not xac_nhan:
            return

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM KHACHHANG
                WHERE MaKhachHang = ?
                """,
                (MaKhachHang,)
            )

            if cursor.rowcount == 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy khách hàng cần xóa!"
                )

                return

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Xóa khách hàng thành công!"
            )

            self.hien_thi_khach_hang()
            self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa khách hàng này.\n\n"
                "Có thể khách hàng đang có đơn đặt tour.\n\n"
                f"Chi tiết:\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # LÀM MỚI
    # =====================================================

    def lam_moi(self):

        self.txtMaKhachHang.delete(0, "end")
        self.txtHoTen.delete(0, "end")
        self.txtSoDienThoai.delete(0, "end")
        self.txtEmail.delete(0, "end")
        self.txtDiaChi.delete(0, "end")


# =========================================================
# CHẠY RIÊNG FILE ĐỂ KIỂM TRA
# =========================================================

if __name__ == "__main__":

    app = ctk.CTk()
    app.geometry("1100x650")
    app.configure(fg_color="#F3EBDD")

    giao_dien = QuanLyKhachHang(
        app,
        lambda: messagebox.showinfo(
            "Thông báo",
            "Đây là chế độ chạy thử riêng."
        )
    )

    giao_dien.pack(
        fill="both",
        expand=True
    )

    app.mainloop()