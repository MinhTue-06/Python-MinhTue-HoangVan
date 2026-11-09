import customtkinter as ctk
from tkinter import ttk, messagebox
import pyodbc


# =========================================================
# CẤU HÌNH
# =========================================================

SERVER_NAME = r'.\SQLEXPRESS01'
DB_NAME = 'QuanLyCacTuyenDuLich'


# =========================================================
# CLASS QUẢN LÝ TÀI KHOẢN
# =========================================================

class QuanLyTaiKhoan(ctk.CTkFrame):

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
    # TẠO GIAO DIỆN
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
            width=180,
            height=35,
            font=("Times New Roman", 13, "bold"),
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
            ("QUẢN LÝ ĐIỂM ĐẾN", 155),
            ("QUẢN LÝ TUYẾN DU LỊCH", 175),
            ("QUẢN LÝ KHÁCH HÀNG", 165),
            ("QUẢN LÝ ĐẶT TOUR", 150),
            ("QUẢN LÝ TÀI KHOẢN", 165)
        ]

        for ten, chieu_rong in cac_chuc_nang:

            dang_mo = ten == "QUẢN LÝ TÀI KHOẢN"

            ctk.CTkButton(
                nav_frame,
                text=ten,
                command=lambda t=ten: self.chuyen_chuc_nang(t),
                width=chieu_rong,
                height=35,
                font=(
                    "Times New Roman",
                    13,
                    "bold" if dang_mo else "normal"
                ),
                fg_color="#C8B99A" if dang_mo else "#57595A",
                hover_color="#B7A582" if dang_mo else "#3C3F40",
                text_color="#333333" if dang_mo else "white"
            ).pack(
                side="left",
                padx=3
            )

        # =================================================
        # TIÊU ĐỀ
        # =================================================

        title = ctk.CTkLabel(
            self,
            text="QUẢN LÝ TÀI KHOẢN",
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

        # MÃ TÀI KHOẢN

        ctk.CTkLabel(
            input_frame,
            text="Mã tài khoản:",
            font=("Times New Roman", 16)
        ).grid(row=0, column=0, padx=8, pady=6, sticky="w")

        self.txtMaTaiKhoan = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center",
            state="disabled"
        )

        self.txtMaTaiKhoan.grid(row=0, column=1, padx=8, pady=6)

        # TÊN ĐĂNG NHẬP

        ctk.CTkLabel(
            input_frame,
            text="Tên đăng nhập:",
            font=("Times New Roman", 16)
        ).grid(row=0, column=2, padx=8, pady=6, sticky="w")

        self.txtTenDangNhap = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtTenDangNhap.grid(row=0, column=3, padx=8, pady=6)

        # MẬT KHẨU

        ctk.CTkLabel(
            input_frame,
            text="Mật khẩu:",
            font=("Times New Roman", 16)
        ).grid(row=1, column=0, padx=8, pady=6, sticky="w")

        self.txtMatKhau = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center",
            show="*"
        )

        self.txtMatKhau.grid(row=1, column=1, padx=8, pady=6)

        # HỌ TÊN

        ctk.CTkLabel(
            input_frame,
            text="Họ tên:",
            font=("Times New Roman", 16)
        ).grid(row=1, column=2, padx=8, pady=6, sticky="w")

        self.txtHoTen = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtHoTen.grid(row=1, column=3, padx=8, pady=6)

        # EMAIL

        ctk.CTkLabel(
            input_frame,
            text="Email:",
            font=("Times New Roman", 16)
        ).grid(row=2, column=0, padx=8, pady=6, sticky="w")

        self.txtEmail = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtEmail.grid(row=2, column=1, padx=8, pady=6)

        # SỐ ĐIỆN THOẠI

        ctk.CTkLabel(
            input_frame,
            text="Số điện thoại:",
            font=("Times New Roman", 16)
        ).grid(row=2, column=2, padx=8, pady=6, sticky="w")

        self.txtSoDienThoai = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtSoDienThoai.grid(row=2, column=3, padx=8, pady=6)

        # QUYỀN

        ctk.CTkLabel(
            input_frame,
            text="Quyền:",
            font=("Times New Roman", 16)
        ).grid(row=3, column=0, padx=8, pady=6, sticky="w")

        self.txtQuyen = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center",
            placeholder_text="Ví dụ: Quản trị viên, Nhân viên"
        )

        self.txtQuyen.grid(row=3, column=1, padx=8, pady=6)

        # TRẠNG THÁI

        ctk.CTkLabel(
            input_frame,
            text="Trạng thái:",
            font=("Times New Roman", 16)
        ).grid(row=3, column=2, padx=8, pady=6, sticky="w")

        self.cboTrangThai = ctk.CTkComboBox(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center",
            values=["Hoạt động", "Bị khóa"]
        )

        self.cboTrangThai.grid(row=3, column=3, padx=8, pady=6)
        self.cboTrangThai.set("")

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

        # CẤU HÌNH BẢNG

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
            background=[("selected", "#B7D7F0")],
            foreground=[("selected", "black")]
        )

        # CỘT BẢNG

        columns = (
            "MaTaiKhoan",
            "TenDangNhap",
            "MatKhau",
            "HoTen",
            "Email",
            "SoDienThoai",
            "Quyen",
            "TrangThai"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.tree.heading("MaTaiKhoan", text="Mã tài khoản")
        self.tree.heading("TenDangNhap", text="Tên đăng nhập")
        self.tree.heading("MatKhau", text="Mật khẩu")
        self.tree.heading("HoTen", text="Họ tên")
        self.tree.heading("Email", text="Email")
        self.tree.heading("SoDienThoai", text="Số điện thoại")
        self.tree.heading("Quyen", text="Quyền")
        self.tree.heading("TrangThai", text="Trạng thái")

        self.tree.column("MaTaiKhoan", width=120, anchor="center")
        self.tree.column("TenDangNhap", width=180, anchor="center")
        self.tree.column("MatKhau", width=150, anchor="center")
        self.tree.column("HoTen", width=200, anchor="center")
        self.tree.column("Email", width=220, anchor="center")
        self.tree.column("SoDienThoai", width=160, anchor="center")
        self.tree.column("Quyen", width=150, anchor="center")
        self.tree.column("TrangThai", width=150, anchor="center")

        # THANH CUỘN NGANG

        scrollbar_x = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            xscrollcommand=scrollbar_x.set
        )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(8, 0)
        )

        scrollbar_x.pack(
            fill="x",
            padx=8,
            pady=(0, 8)
        )

                # =================================================
        # NÚT CHỨC NĂNG
        # =================================================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(pady=8)

        # NÚT THÊM

        self.btnThem = ctk.CTkButton(
            button_frame,
            text="THÊM",
            width=150,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#2196F3",
            command=self.them_tai_khoan
        )

        self.btnThem.grid(row=0, column=0, padx=10)

        # NÚT SỬA

        self.btnSua = ctk.CTkButton(
            button_frame,
            text="SỬA",
            width=150,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#FF9800",
            command=self.sua_tai_khoan
        )

        self.btnSua.grid(row=0, column=1, padx=10)

        # NÚT XÓA

        self.btnXoa = ctk.CTkButton(
            button_frame,
            text="XÓA",
            width=150,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#F44336",
            command=self.xoa_tai_khoan
        )

        self.btnXoa.grid(row=0, column=2, padx=10)

        # NÚT LÀM MỚI

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

        # CHỌN DÒNG

        self.tree.bind("<ButtonRelease-1>", self.chon_dong)

        # HIỂN THỊ DỮ LIỆU

        self.hien_thi_tai_khoan()

    # =====================================================
    # HIỂN THỊ DỮ LIỆU
    # =====================================================

    def hien_thi_tai_khoan(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    MaTaiKhoan,
                    TenDangNhap,
                    HoTen,
                    Email,
                    SoDienThoai,
                    Quyen,
                    TrangThai
                FROM TAIKHOAN
                ORDER BY MaTaiKhoan
            """)

            rows = cursor.fetchall()

            for row in rows:

                trang_thai = "Hoạt động" if row[6] else "Bị khóa"

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        "********",
                        row[2] if row[2] else "",
                        row[3] if row[3] else "",
                        row[4] if row[4] else "",
                        row[5] if row[5] else "",
                        trang_thai
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
    # HÀM ĐIỀN MÃ TÀI KHOẢN
    # =====================================================

    def dien_ma_tai_khoan(self, ma):

        self.txtMaTaiKhoan.configure(state="normal")
        self.txtMaTaiKhoan.delete(0, "end")
        self.txtMaTaiKhoan.insert(0, str(ma))
        self.txtMaTaiKhoan.configure(state="disabled")

    # =====================================================
    # CHỌN DÒNG
    # =====================================================

    def chon_dong(self, event):

        selected = self.tree.focus()

        if selected == "":
            return

        values = self.tree.item(selected, "values")

        if not values:
            return

        self.dien_ma_tai_khoan(values[0])

        self.txtTenDangNhap.delete(0, "end")
        self.txtTenDangNhap.insert(0, values[1])

        self.txtHoTen.delete(0, "end")
        self.txtHoTen.insert(0, values[3])

        self.txtEmail.delete(0, "end")
        self.txtEmail.insert(0, values[4])

        self.txtSoDienThoai.delete(0, "end")
        self.txtSoDienThoai.insert(0, values[5])

        self.txtQuyen.delete(0, "end")
        self.txtQuyen.insert(0, values[6])

        self.cboTrangThai.set(values[7])

        # LẤY MẬT KHẨU THẬT TỪ DATABASE

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT MatKhau
                FROM TAIKHOAN
                WHERE MaTaiKhoan = ?
                """,
                (values[0],)
            )

            row = cursor.fetchone()

            self.txtMatKhau.delete(0, "end")

            if row:
                self.txtMatKhau.insert(
                    0,
                    row[0] if row[0] else ""
                )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                f"Không thể lấy mật khẩu:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # THÊM TÀI KHOẢN
    # =====================================================

    def them_tai_khoan(self):

        TenDangNhap = self.txtTenDangNhap.get().strip()
        MatKhau = self.txtMatKhau.get().strip()
        HoTen = self.txtHoTen.get().strip()
        Email = self.txtEmail.get().strip()
        SoDienThoai = self.txtSoDienThoai.get().strip()
        Quyen = self.txtQuyen.get().strip()

        TrangThai = 1 if self.cboTrangThai.get() == "Hoạt động" else 0

        if TenDangNhap == "" or MatKhau == "" or HoTen == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên đăng nhập, mật khẩu và họ tên!"
            )
            return

        if Quyen == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập quyền tài khoản!"
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
                FROM TAIKHOAN
                WHERE TenDangNhap = ?
                """,
                (TenDangNhap,)
            )

            if cursor.fetchone()[0] > 0:
                messagebox.showwarning(
                    "Thông báo",
                    "Tên đăng nhập này đã tồn tại!"
                )
                return

            cursor.execute(
                """
                INSERT INTO TAIKHOAN
                (
                    TenDangNhap,
                    MatKhau,
                    HoTen,
                    Email,
                    SoDienThoai,
                    Quyen,
                    TrangThai
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    TenDangNhap,
                    MatKhau,
                    HoTen,
                    Email,
                    SoDienThoai,
                    Quyen,
                    TrangThai
                )
            )

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Thêm tài khoản thành công!"
            )

            self.hien_thi_tai_khoan()
            self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                f"Không thể thêm tài khoản:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # SỬA TÀI KHOẢN
    # =====================================================

    def sua_tai_khoan(self):

        MaTaiKhoan = self.txtMaTaiKhoan.get().strip()
        TenDangNhap = self.txtTenDangNhap.get().strip()
        MatKhau = self.txtMatKhau.get().strip()
        HoTen = self.txtHoTen.get().strip()
        Email = self.txtEmail.get().strip()
        SoDienThoai = self.txtSoDienThoai.get().strip()
        Quyen = self.txtQuyen.get().strip()

        TrangThai = 1 if self.cboTrangThai.get() == "Hoạt động" else 0

        if MaTaiKhoan == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn tài khoản cần sửa!"
            )
            return

        if TenDangNhap == "" or MatKhau == "" or HoTen == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên đăng nhập, mật khẩu và họ tên!"
            )
            return

        if Quyen == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập quyền tài khoản!"
            )
            return

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            # KIỂM TRA TÊN ĐĂNG NHẬP CÓ BỊ TRÙNG KHÔNG

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM TAIKHOAN
                WHERE TenDangNhap = ?
                AND MaTaiKhoan <> ?
                """,
                (TenDangNhap, MaTaiKhoan)
            )

            if cursor.fetchone()[0] > 0:
                messagebox.showwarning(
                    "Thông báo",
                    "Tên đăng nhập này đã được sử dụng!"
                )
                return

            cursor.execute(
                """
                UPDATE TAIKHOAN
                SET
                    TenDangNhap = ?,
                    MatKhau = ?,
                    HoTen = ?,
                    Email = ?,
                    SoDienThoai = ?,
                    Quyen = ?,
                    TrangThai = ?
                WHERE MaTaiKhoan = ?
                """,
                (
                    TenDangNhap,
                    MatKhau,
                    HoTen,
                    Email,
                    SoDienThoai,
                    Quyen,
                    TrangThai,
                    MaTaiKhoan
                )
            )

            if cursor.rowcount == 0:
                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy tài khoản cần sửa!"
                )
                return

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Sửa tài khoản thành công!"
            )

            self.hien_thi_tai_khoan()
            self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                f"Không thể sửa tài khoản:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # XÓA TÀI KHOẢN
    # =====================================================

    def xoa_tai_khoan(self):

        MaTaiKhoan = self.txtMaTaiKhoan.get().strip()

        if MaTaiKhoan == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn tài khoản cần xóa!"
            )
            return

        xac_nhan = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc muốn xóa tài khoản này không?"
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
                DELETE FROM TAIKHOAN
                WHERE MaTaiKhoan = ?
                """,
                (MaTaiKhoan,)
            )

            if cursor.rowcount == 0:
                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy tài khoản cần xóa!"
                )
                return

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Xóa tài khoản thành công!"
            )

            self.hien_thi_tai_khoan()
            self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa tài khoản này.\n\n"
                "Có thể tài khoản đang được sử dụng ở bảng khác.\n\n"
                f"Chi tiết:\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # LÀM MỚI
    # =====================================================

    def lam_moi(self):

        self.dien_ma_tai_khoan("")

        self.txtTenDangNhap.delete(0, "end")
        self.txtMatKhau.delete(0, "end")
        self.txtHoTen.delete(0, "end")
        self.txtEmail.delete(0, "end")
        self.txtSoDienThoai.delete(0, "end")
        self.txtQuyen.delete(0, "end")

        self.cboTrangThai.set("Hoạt động")

        for item in self.tree.selection():
            self.tree.selection_remove(item)

        self.tree.focus("")


# =========================================================
# CHẠY RIÊNG FILE ĐỂ KIỂM TRA
# =========================================================

if __name__ == "__main__":

    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("1100x650")
    app.configure(fg_color="#F3EBDD")

    giao_dien = QuanLyTaiKhoan(
        app,
        lambda: messagebox.showinfo(
            "Thông báo",
            "Đây là chế độ chạy thử riêng."
        )
    )

    giao_dien.pack(fill="both", expand=True)

    app.mainloop()