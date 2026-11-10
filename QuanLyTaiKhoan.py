
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

        # Lưu mã gốc của tài khoản đang chọn
        self.ma_tai_khoan_dang_chon = None

        self.create_interface()

    # =====================================================
    # CHUYỂN CHỨC NĂNG
    # =====================================================

    def chuyen_chuc_nang(self, ten_chuc_nang):
        ung_dung = self.winfo_toplevel()

        if hasattr(ung_dung, "mo_chuc_nang"):
            ung_dung.mo_chuc_nang(ten_chuc_nang)
        else:
            messagebox.showerror(
                "Lỗi",
                "Không tìm thấy chức năng chuyển trang!"
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

        # THANH ĐIỀU HƯỚNG

        nav_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        nav_frame.pack(fill="x", padx=15, pady=5)

        ctk.CTkButton(
            nav_frame,
            text="QUAY LẠI TRANG CHỦ",
            command=self.quay_lai,
            width=180,
            height=35,
            font=("Times New Roman", 13, "bold"),
            fg_color="#57595A",
            hover_color="#3C3F40",
            text_color="white"
        ).pack(side="left", padx=3)

        cac_chuc_nang = [
            ("QUẢN LÝ ĐIỂM ĐẾN", 165),
            ("QUẢN LÝ TUYẾN DU LỊCH", 165),
            ("QUẢN LÝ KHÁCH HÀNG", 165),
            ("QUẢN LÝ ĐẶT TOUR", 165),
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
            ).pack(side="left", padx=3)

        # TIÊU ĐỀ

        ctk.CTkLabel(
            self,
            text="QUẢN LÝ TÀI KHOẢN",
            font=("Times New Roman", 22, "bold"),
            text_color="#3369A7"
        ).pack(pady=10)

        # KHUNG NHẬP DỮ LIỆU

        input_frame = ctk.CTkFrame(
            self,
            fg_color="#FBF8F1",
            corner_radius=12
        )
        input_frame.pack(fill="x", padx=15, pady=5)

        # MÃ TÀI KHOẢN - LUÔN CHO PHÉP NHẬP

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
            state="normal"
        )
        self.txtMaTaiKhoan.grid(
            row=0, column=1, padx=8, pady=6
        )

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
        self.txtTenDangNhap.grid(
            row=0, column=3, padx=8, pady=6
        )

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
        self.txtMatKhau.grid(
            row=1, column=1, padx=8, pady=6
        )

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
        self.txtHoTen.grid(
            row=1, column=3, padx=8, pady=6
        )

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
        self.txtEmail.grid(
            row=2, column=1, padx=8, pady=6
        )

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
        self.txtSoDienThoai.grid(
            row=2, column=3, padx=8, pady=6
        )

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
        self.txtQuyen.grid(
            row=3, column=1, padx=8, pady=6
        )

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
        self.cboTrangThai.grid(
            row=3, column=3, padx=8, pady=6
        )
        self.cboTrangThai.set("Hoạt động")

        # KHUNG BẢNG

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

        style = ttk.Style()

        style.configure(
            "Treeview",
            font=("Times New Roman", 30),
            rowheight=45,
            background="white",
            foreground="black",
            fieldbackground="white"
        )

        style.configure(
            "Treeview.Heading",
            font=("Times New Roman", 28, "bold"),
            background="#D9D9D9",
            foreground="black"
        )

        style.map(
            "Treeview",
            background=[("selected", "#B7D7F0")],
            foreground=[("selected", "black")]
        )

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

        tieu_de = {
            "MaTaiKhoan": "Mã tài khoản",
            "TenDangNhap": "Tên đăng nhập",
            "MatKhau": "Mật khẩu",
            "HoTen": "Họ tên",
            "Email": "Email",
            "SoDienThoai": "Số điện thoại",
            "Quyen": "Quyền",
            "TrangThai": "Trạng thái"
        }

        do_rong = {
            "MaTaiKhoan": 120,
            "TenDangNhap": 180,
            "MatKhau": 150,
            "HoTen": 200,
            "Email": 220,
            "SoDienThoai": 160,
            "Quyen": 150,
            "TrangThai": 150
        }

        for cot in columns:
            self.tree.heading(cot, text=tieu_de[cot])
            self.tree.column(
                cot,
                width=do_rong[cot],
                anchor="center"
            )

        scrollbar_x = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(xscrollcommand=scrollbar_x.set)

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

        # CHỌN DÒNG TRONG BẢNG

        self.tree.bind(
            "<ButtonRelease-1>",
            self.chon_dong
        )

        # KHUNG NÚT CHỨC NĂNG

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        button_frame.pack(
            fill="x",
            padx=15,
            pady=5
        )

        self.btnThem = ctk.CTkButton(
            button_frame,
            text="THÊM",
            width=130,
            height=38,
            font=("Times New Roman", 14, "bold"),
            fg_color="#2196F3",
            hover_color="#1976D2",
            command=self.them_tai_khoan
        )
        self.btnThem.pack(side="left", padx=3)

        self.btnSua = ctk.CTkButton(
            button_frame,
            text="SỬA",
            width=130,
            height=38,
            font=("Times New Roman", 14, "bold"),
            fg_color="#FF9800",
            hover_color="#E68900",
            command=self.sua_tai_khoan
        )
        self.btnSua.pack(side="left", padx=3)

        self.btnXoa = ctk.CTkButton(
            button_frame,
            text="XÓA",
            width=130,
            height=38,
            font=("Times New Roman", 14, "bold"),
            fg_color="#F44336",
            hover_color="#D32F2F",
            command=self.xoa_tai_khoan
        )
        self.btnXoa.pack(side="left", padx=3)

        self.btnLamMoi = ctk.CTkButton(
            button_frame,
            text="LÀM MỚI",
            width=130,
            height=38,
            font=("Times New Roman", 14, "bold"),
            fg_color="#607D8B",
            hover_color="#455A64",
            command=self.lam_moi
        )
        self.btnLamMoi.pack(side="left", padx=3)

        ctk.CTkFrame(
            button_frame,
            width=2,
            height=32,
            fg_color="#B7A582"
        ).pack(side="left", padx=8)

        self.btnTimKiem = ctk.CTkButton(
            button_frame,
            text="⌕ TÌM KIẾM",
            width=130,
            height=38,
            font=("Times New Roman", 14, "bold"),
            fg_color="#D6E8F8",
            hover_color="#B8D8F5",
            text_color="#1565C0",
            command=self.tim_kiem_tai_khoan
        )
        self.btnTimKiem.pack(side="left", padx=3)

        ctk.CTkLabel(
            button_frame,
            text="Tìm kiếm:",
            font=("Times New Roman", 14),
            text_color="#333333"
        ).pack(side="left", padx=(5, 3))

        self.txtTimKiem = ctk.CTkEntry(
            button_frame,
            width=180,
            height=38,
            font=("Times New Roman", 14),
            placeholder_text="Nhập từ khóa..."
        )
        self.txtTimKiem.pack(side="left", padx=3)

        self.txtTimKiem.bind(
            "<Return>",
            lambda event: self.tim_kiem_tai_khoan()
        )

        self.btnXoaTimKiem = ctk.CTkButton(
            button_frame,
            text="✖ XÓA TÌM KIẾM",
            width=130,
            height=38,
            font=("Times New Roman", 12, "bold"),
            fg_color="#F5A3A3",
            hover_color="#E88B8B",
            text_color="#A32222",
            command=self.xoa_tim_kiem
        )
        self.btnXoaTimKiem.pack(side="right", padx=3)

        # HIỂN THỊ DỮ LIỆU BAN ĐẦU

        self.hien_thi_tai_khoan()

    # =====================================================
    # HIỂN THỊ DỮ LIỆU
    # =====================================================

    def hien_thi_tai_khoan(self, tu_khoa=None):

        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = self.get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            if tu_khoa:
                tu_khoa_sql = f"%{tu_khoa}%"

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
                    WHERE
                        CAST(MaTaiKhoan AS NVARCHAR(50)) LIKE ?
                        OR TenDangNhap LIKE ?
                        OR HoTen LIKE ?
                        OR Email LIKE ?
                        OR SoDienThoai LIKE ?
                        OR Quyen LIKE ?
                        OR CASE
                            WHEN TrangThai = 1 THEN N'Hoạt động'
                            ELSE N'Bị khóa'
                        END LIKE ?
                    ORDER BY MaTaiKhoan
                """, (
                    tu_khoa_sql,
                    tu_khoa_sql,
                    tu_khoa_sql,
                    tu_khoa_sql,
                    tu_khoa_sql,
                    tu_khoa_sql,
                    tu_khoa_sql
                ))

            else:
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
                trang_thai = (
                    "Hoạt động" if row[6] else "Bị khóa"
                )

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

            cursor.close()

            if tu_khoa and not rows:
                messagebox.showinfo(
                    "Thông báo",
                    "Không tìm thấy tài khoản phù hợp!"
                )

        except Exception as e:
            messagebox.showerror(
                "Lỗi",
                f"Không thể hiển thị dữ liệu:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # TÌM KIẾM
    # =====================================================

    def tim_kiem_tai_khoan(self):

        tu_khoa = self.txtTimKiem.get().strip()

        if not tu_khoa:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập từ khóa cần tìm!"
            )
            self.txtTimKiem.focus()
            return

        self.lam_trong_o_nhap()
        self.hien_thi_tai_khoan(tu_khoa)

    # =====================================================
    # XÓA TÌM KIẾM
    # =====================================================

    def xoa_tim_kiem(self):

        self.txtTimKiem.delete(0, "end")

        self.lam_trong_o_nhap()
        self.hien_thi_tai_khoan()

    # =====================================================
    # ĐIỀN MÃ TÀI KHOẢN
    # =====================================================

    def dien_ma_tai_khoan(self, ma):

        # LUÔN ĐỂ Ô MÃ Ở TRẠNG THÁI CÓ THỂ NHẬP

        self.txtMaTaiKhoan.configure(state="normal")
        self.txtMaTaiKhoan.delete(0, "end")

        if ma is not None and str(ma) != "":
            self.txtMaTaiKhoan.insert(0, str(ma))

    # =====================================================
    # CHỌN DÒNG TRONG BẢNG
    # =====================================================

    def chon_dong(self, event=None):

        if event is not None:
            item = self.tree.identify_row(event.y)

            if not item:
                return

            self.tree.selection_set(item)
            self.tree.focus(item)

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(selected, "values")

        if not values:
            return

        # LƯU MÃ GỐC ĐỂ SỬA/XÓA CHÍNH XÁC

        self.ma_tai_khoan_dang_chon = str(values[0])

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

        # LẤY MẬT KHẨU TỪ DATABASE

        conn = self.get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT MatKhau
                FROM TAIKHOAN
                WHERE MaTaiKhoan = ?
            """, (self.ma_tai_khoan_dang_chon,))

            row = cursor.fetchone()

            self.txtMatKhau.delete(0, "end")

            if row and row[0]:
                self.txtMatKhau.insert(0, row[0])

            cursor.close()

        except Exception as e:
            messagebox.showerror(
                "Lỗi",
                f"Không thể lấy mật khẩu:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # LẤY DỮ LIỆU TỪ FORM
    # =====================================================

    def lay_du_lieu_form(self):

        ten_dang_nhap = self.txtTenDangNhap.get().strip()
        mat_khau = self.txtMatKhau.get().strip()
        ho_ten = self.txtHoTen.get().strip()
        email = self.txtEmail.get().strip()
        so_dien_thoai = self.txtSoDienThoai.get().strip()
        quyen = self.txtQuyen.get().strip()

        trang_thai_text = self.cboTrangThai.get().strip()

        if not ten_dang_nhap or not mat_khau or not ho_ten:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên đăng nhập, mật khẩu và họ tên!"
            )
            return None

        if not quyen:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập quyền tài khoản!"
            )
            return None

        if trang_thai_text not in ["Hoạt động", "Bị khóa"]:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn trạng thái tài khoản!"
            )
            return None

        trang_thai = 1 if trang_thai_text == "Hoạt động" else 0

        return (
            ten_dang_nhap,
            mat_khau,
            ho_ten,
            email,
            so_dien_thoai,
            quyen,
            trang_thai
        )

    # =====================================================
    # THÊM TÀI KHOẢN
    # =====================================================

    def them_tai_khoan(self):

        data = self.lay_du_lieu_form()

        if data is None:
            return

        conn = self.get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT COUNT(*)
                FROM TAIKHOAN
                WHERE TenDangNhap = ?
            """, (data[0],))

            if cursor.fetchone()[0] > 0:
                messagebox.showwarning(
                    "Thông báo",
                    "Tên đăng nhập này đã tồn tại!"
                )
                return

            # MaTaiKhoan là IDENTITY nên SQL Server tự tạo mã

            cursor.execute("""
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
            """, data)

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Thêm tài khoản thành công!"
            )

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

        # Dùng mã gốc của dòng đã chọn, không dùng mã đã bị sửa
        ma_goc = self.ma_tai_khoan_dang_chon

        if not ma_goc:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn một tài khoản trong bảng để sửa!"
            )
            return

        data = self.lay_du_lieu_form()

        if data is None:
            return

        conn = self.get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            # Kiểm tra tên đăng nhập trùng với tài khoản khác

            cursor.execute("""
                SELECT COUNT(*)
                FROM TAIKHOAN
                WHERE TenDangNhap = ?
                AND MaTaiKhoan <> ?
            """, (data[0], ma_goc))

            if cursor.fetchone()[0] > 0:
                messagebox.showwarning(
                    "Thông báo",
                    "Tên đăng nhập này đã được sử dụng!"
                )
                return

            cursor.execute("""
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
            """, data + (ma_goc,))

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

        ma_goc = self.ma_tai_khoan_dang_chon

        if not ma_goc:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn tài khoản cần xóa trong bảng!"
            )
            return

        xac_nhan = messagebox.askyesno(
            "Xác nhận",
            f"Bạn có chắc muốn xóa tài khoản mã {ma_goc} không?"
        )

        if not xac_nhan:
            return

        conn = self.get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM TAIKHOAN
                WHERE MaTaiKhoan = ?
            """, (ma_goc,))

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
    # XÓA TRỐNG CÁC Ô NHẬP
    # =====================================================

    def lam_trong_o_nhap(self):

        # XÓA MÃ NHƯNG KHÔNG KHÓA Ô NHẬP

        self.ma_tai_khoan_dang_chon = None

        self.txtMaTaiKhoan.configure(state="normal")
        self.txtMaTaiKhoan.delete(0, "end")

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

    # =====================================================
    # LÀM MỚI
    # =====================================================

    def lam_moi(self):

        self.txtTimKiem.delete(0, "end")

        self.lam_trong_o_nhap()
        self.hien_thi_tai_khoan()


# =========================================================
# CHẠY RIÊNG FILE ĐỂ KIỂM TRA
# =========================================================

if __name__ == "__main__":

    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("1100x650")
    app.configure(fg_color="#F3EBDD")
    app.title("QUẢN LÝ TÀI KHOẢN")

    giao_dien = QuanLyTaiKhoan(
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
