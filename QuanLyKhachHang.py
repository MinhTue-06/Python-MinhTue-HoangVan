
import customtkinter as ctk
from tkinter import ttk, messagebox
import pyodbc
from datetime import datetime


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
    # GIAO DIỆN
    # =====================================================

    def create_interface(self):

        # ================= THANH ĐIỀU HƯỚNG =================

        nav_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        nav_frame.pack(fill="x", padx=15, pady=5)

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

        btn_quay_lai.pack(side="left", padx=3)

        cac_chuc_nang = [
            ("QUẢN LÝ ĐIỂM ĐẾN", "QUẢN LÝ ĐIỂM ĐẾN", 165),
            ("QUẢN LÝ TUYẾN DU LỊCH", "QUẢN LÝ TUYẾN DU LỊCH", 165),
            ("QUẢN LÝ KHÁCH HÀNG", "QUẢN LÝ KHÁCH HÀNG", 165),
            ("QUẢN LÝ ĐẶT TOUR", "QUẢN LÝ ĐẶT TOUR", 165),
            ("QUẢN LÝ TÀI KHOẢN", "QUẢN LÝ TÀI KHOẢN", 165)
        ]

        for ten, ma, chieu_rong in cac_chuc_nang:

            dang_mo = ma == "QUẢN LÝ KHÁCH HÀNG"

            ctk.CTkButton(
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
            ).pack(side="left", padx=3)

        # ================= TIÊU ĐỀ =================

        title = ctk.CTkLabel(
            self,
            text="QUẢN LÝ KHÁCH HÀNG",
            font=("Times New Roman", 22, "bold"),
            text_color="#3369A7"
        )

        title.pack(pady=10)

        # ================= KHUNG NHẬP DỮ LIỆU =================

        input_frame = ctk.CTkFrame(
            self,
            fg_color="#FBF8F1",
            corner_radius=12
        )

        input_frame.pack(fill="x", padx=15, pady=5)

        # MÃ KHÁCH HÀNG

        ctk.CTkLabel(
            input_frame,
            text="Mã khách hàng:",
            font=("Times New Roman", 16)
        ).grid(row=0, column=0, padx=8, pady=6, sticky="w")

        self.txtMaKhachHang = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMaKhachHang.grid(row=0, column=1, padx=8, pady=6)

        # HỌ TÊN

        ctk.CTkLabel(
            input_frame,
            text="Họ tên:",
            font=("Times New Roman", 16)
        ).grid(row=0, column=2, padx=8, pady=6, sticky="w")

        self.txtHoTen = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtHoTen.grid(row=0, column=3, padx=8, pady=6)

        # SỐ ĐIỆN THOẠI

        ctk.CTkLabel(
            input_frame,
            text="Số điện thoại:",
            font=("Times New Roman", 16)
        ).grid(row=1, column=0, padx=8, pady=6, sticky="w")

        self.txtSoDienThoai = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtSoDienThoai.grid(row=1, column=1, padx=8, pady=6)

        # EMAIL

        ctk.CTkLabel(
            input_frame,
            text="Email:",
            font=("Times New Roman", 16)
        ).grid(row=1, column=2, padx=8, pady=6, sticky="w")

        self.txtEmail = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtEmail.grid(row=1, column=3, padx=8, pady=6)

        # GIỚI TÍNH

        ctk.CTkLabel(
            input_frame,
            text="Giới tính:",
            font=("Times New Roman", 16)
        ).grid(row=2, column=0, padx=8, pady=6, sticky="w")

        self.txtGioiTinh = ctk.CTkComboBox(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            values=["Nam", "Nữ", "Khác"],
            justify="center"
        )

        self.txtGioiTinh.grid(row=2, column=1, padx=8, pady=6)
        self.txtGioiTinh.set("")

        # NGÀY SINH

        ctk.CTkLabel(
            input_frame,
            text="Ngày sinh:",
            font=("Times New Roman", 16)
        ).grid(row=2, column=2, padx=8, pady=6, sticky="w")

        self.txtNgaySinh = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center",
            placeholder_text="DD/MM/YYYY"
        )

        self.txtNgaySinh.grid(row=2, column=3, padx=8, pady=6)

        # ĐỊA CHỈ

        ctk.CTkLabel(
            input_frame,
            text="Địa chỉ:",
            font=("Times New Roman", 16)
        ).grid(row=3, column=0, padx=8, pady=6, sticky="w")

        self.txtDiaChi = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtDiaChi.grid(row=3, column=1, padx=8, pady=6)

        # ================= KHUNG BẢNG =================

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
            "MaKhachHang",
            "HoTen",
            "SoDienThoai",
            "Email",
            "GioiTinh",
            "NgaySinh",
            "DiaChi"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        headings = {
            "MaKhachHang": "Mã khách hàng",
            "HoTen": "Họ tên",
            "SoDienThoai": "Số điện thoại",
            "Email": "Email",
            "GioiTinh": "Giới tính",
            "NgaySinh": "Ngày sinh",
            "DiaChi": "Địa chỉ"
        }

        widths = {
            "MaKhachHang": 120,
            "HoTen": 180,
            "SoDienThoai": 130,
            "Email": 190,
            "GioiTinh": 90,
            "NgaySinh": 110,
            "DiaChi": 200
        }

        for col in columns:

            self.tree.heading(
                col,
                text=headings[col],
                anchor="center"
            )

            self.tree.column(
                col,
                width=widths[col],
                anchor="center"
            )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

        # CHỌN DÒNG

        self.tree.bind(
            "<ButtonRelease-1>",
            self.chon_dong
        )

        # ================= NÚT CHỨC NĂNG =================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=15,
            pady=8
        )

        left_frame = ctk.CTkFrame(
            button_frame,
            fg_color="transparent"
        )

        left_frame.pack(side="left")

        self.btnThem = ctk.CTkButton(
            left_frame,
            text="THÊM",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#2196F3",
            command=self.them_khach_hang
        )

        self.btnThem.pack(side="left", padx=3)

        self.btnSua = ctk.CTkButton(
            left_frame,
            text="SỬA",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#FF9800",
            command=self.sua_khach_hang
        )

        self.btnSua.pack(side="left", padx=3)

        self.btnXoa = ctk.CTkButton(
            left_frame,
            text="XÓA",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#F44336",
            command=self.xoa_khach_hang
        )

        self.btnXoa.pack(side="left", padx=3)

        self.btnLamMoi = ctk.CTkButton(
            left_frame,
            text="LÀM MỚI",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#607D8B",
            command=self.lam_moi
        )

        self.btnLamMoi.pack(side="left", padx=3)

        # VẠCH PHÂN CÁCH

        vach_ngan = ctk.CTkFrame(
            button_frame,
            width=2,
            height=40,
            fg_color="#B7A582"
        )

        vach_ngan.pack(side="left", padx=7)

        # NÚT TÌM KIẾM

        self.btnTimKiem = ctk.CTkButton(
            button_frame,
            text="⌕ TÌM KIẾM",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#D6E8F8",
            hover_color="#B8D8F5",
            text_color="#1565C0",
            command=self.tim_kiem
        )

        self.btnTimKiem.pack(side="left", padx=3)

        # NHÃN TÌM KIẾM

        lblTimKiem = ctk.CTkLabel(
            button_frame,
            text="Tìm kiếm:",
            font=("Times New Roman", 14, "bold")
        )

        lblTimKiem.pack(side="left", padx=3)

        # Ô NHẬP TỪ KHÓA

        self.txtTimKiem = ctk.CTkEntry(
            button_frame,
            width=180,
            height=40,
            font=("Times New Roman", 14),
            placeholder_text="Nhập từ khóa..."
        )

        self.txtTimKiem.pack(side="left", padx=3)

        self.txtTimKiem.bind(
            "<Return>",
            lambda event: self.tim_kiem()
        )

        # NÚT XÓA TÌM KIẾM

        self.btnXoaTimKiem = ctk.CTkButton(
            button_frame,
            text="✖  XÓA TÌM KIẾM",
            width=130,
            height=40,
            font=("Times New Roman", 12, "bold"),
            fg_color="#F5A3A3",
            hover_color="#E88B8B",
            text_color="#A32222",
            command=self.xoa_tim_kiem
        )

        self.btnXoaTimKiem.pack(side="right", padx=3)

        # HIỂN THỊ DỮ LIỆU BAN ĐẦU

        self.hien_thi_khach_hang()

    # =====================================================
    # HIỂN THỊ KHÁCH HÀNG
    # =====================================================

    def hien_thi_khach_hang(self, tu_khoa=None):

        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            if tu_khoa:

                noi_dung = f"%{tu_khoa}%"

                cursor.execute("""
                    SELECT
                        MaKhachHang,
                        HoTen,
                        SoDienThoai,
                        Email,
                        GioiTinh,
                        NgaySinh,
                        DiaChi
                    FROM KHACHHANG
                    WHERE
                        CAST(MaKhachHang AS NVARCHAR(50)) LIKE ?
                        OR HoTen LIKE ?
                        OR SoDienThoai LIKE ?
                        OR Email LIKE ?
                        OR GioiTinh LIKE ?
                        OR CONVERT(NVARCHAR(10), NgaySinh, 23) LIKE ?
                        OR CONVERT(NVARCHAR(10), NgaySinh, 103) LIKE ?
                        OR DiaChi LIKE ?
                    ORDER BY MaKhachHang
                """, (
                    noi_dung,
                    noi_dung,
                    noi_dung,
                    noi_dung,
                    noi_dung,
                    noi_dung,
                    noi_dung,
                    noi_dung
                ))

            else:

                cursor.execute("""
                    SELECT
                        MaKhachHang,
                        HoTen,
                        SoDienThoai,
                        Email,
                        GioiTinh,
                        NgaySinh,
                        DiaChi
                    FROM KHACHHANG
                    ORDER BY MaKhachHang
                """)

            rows = cursor.fetchall()

            for row in rows:

                ngay_sinh = ""

                if row[5] is not None:
                    ngay_sinh = row[5].strftime("%d/%m/%Y")

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1] if row[1] else "",
                        row[2] if row[2] else "",
                        row[3] if row[3] else "",
                        row[4] if row[4] else "",
                        ngay_sinh,
                        row[6] if row[6] else ""
                    )
                )

            cursor.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                f"Không thể hiển thị dữ liệu:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # TÌM KIẾM KHÁCH HÀNG
    # =====================================================

    def tim_kiem(self):

        tu_khoa = self.txtTimKiem.get().strip()

        if tu_khoa == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập nội dung cần tìm kiếm!"
            )
            return

        # Tìm kiếm nhưng không xóa dữ liệu trong các ô nhập

        self.hien_thi_khach_hang(tu_khoa)

        for item in self.tree.selection():
            self.tree.selection_remove(item)

        if not self.tree.get_children():

            messagebox.showinfo(
                "Thông báo",
                "Không tìm thấy khách hàng phù hợp!"
            )

    # =====================================================
    # XÓA TÌM KIẾM
    # =====================================================

    def xoa_tim_kiem(self):

        # Xóa từ khóa trong ô tìm kiếm
        self.txtTimKiem.delete(0, "end")

        # Bỏ chọn dòng trên bảng
        for item in self.tree.selection():
            self.tree.selection_remove(item)

        # Hiển thị lại toàn bộ danh sách khách hàng
        self.hien_thi_khach_hang()

        # Không gọi lam_trong_o_nhap()
        # Vì cần giữ nguyên dữ liệu đang nhập

    # =====================================================
    # XÓA TRẮNG CÁC Ô NHẬP
    # =====================================================

    def lam_trong_o_nhap(self):

        self.txtMaKhachHang.delete(0, "end")
        self.txtHoTen.delete(0, "end")
        self.txtSoDienThoai.delete(0, "end")
        self.txtEmail.delete(0, "end")
        self.txtGioiTinh.set("")
        self.txtNgaySinh.delete(0, "end")
        self.txtDiaChi.delete(0, "end")

    # =====================================================
    # CHỌN DÒNG TRÊN BẢNG
    # =====================================================

    def chon_dong(self, event):

        selected = self.tree.focus()

        if selected == "":
            return

        values = self.tree.item(selected, "values")

        if not values:
            return

        self.lam_trong_o_nhap()

        self.txtMaKhachHang.insert(0, values[0])
        self.txtHoTen.insert(0, values[1])
        self.txtSoDienThoai.insert(0, values[2])
        self.txtEmail.insert(0, values[3])
        self.txtGioiTinh.set(values[4])
        self.txtNgaySinh.insert(0, values[5])
        self.txtDiaChi.insert(0, values[6])

    # =====================================================
    # KIỂM TRA DỮ LIỆU
    # =====================================================

    def kiem_tra_du_lieu(self):

        ma = self.txtMaKhachHang.get().strip()
        ho_ten = self.txtHoTen.get().strip()
        so_dien_thoai = self.txtSoDienThoai.get().strip()
        email = self.txtEmail.get().strip()
        gioi_tinh = self.txtGioiTinh.get().strip()
        ngay_sinh = self.txtNgaySinh.get().strip()
        dia_chi = self.txtDiaChi.get().strip()

        if ma == "" or ho_ten == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập mã khách hàng và họ tên!"
            )
            return None

        if gioi_tinh and gioi_tinh not in ["Nam", "Nữ", "Khác"]:

            messagebox.showwarning(
                "Thông báo",
                "Giới tính chỉ được chọn Nam, Nữ hoặc Khác!"
            )
            return None

        ngay_sinh_sql = None

        if ngay_sinh:

            try:

                ngay_sinh_sql = datetime.strptime(
                    ngay_sinh,
                    "%d/%m/%Y"
                ).date()

                if ngay_sinh_sql > datetime.today().date():

                    messagebox.showwarning(
                        "Thông báo",
                        "Ngày sinh không được lớn hơn ngày hiện tại!"
                    )
                    return None

            except ValueError:

                messagebox.showwarning(
                    "Thông báo",
                    "Ngày sinh phải theo định dạng DD/MM/YYYY!"
                )
                return None

        return (
            ma,
            ho_ten,
            so_dien_thoai,
            email,
            gioi_tinh if gioi_tinh else None,
            ngay_sinh_sql,
            dia_chi
        )

    # =====================================================
    # THÊM KHÁCH HÀNG
    # =====================================================

    def them_khach_hang(self):

        data = self.kiem_tra_du_lieu()

        if data is None:
            return

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute("""
                SELECT COUNT(*)
                FROM KHACHHANG
                WHERE MaKhachHang = ?
            """, (data[0],))

            if cursor.fetchone()[0] > 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Mã khách hàng này đã tồn tại!"
                )
                return

            cursor.execute("""
                INSERT INTO KHACHHANG
                (
                    MaKhachHang,
                    HoTen,
                    SoDienThoai,
                    Email,
                    GioiTinh,
                    NgaySinh,
                    DiaChi
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, data)

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Thêm khách hàng thành công!"
            )

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

        data = self.kiem_tra_du_lieu()

        if data is None:
            return

        ma = data[0]

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute("""
                UPDATE KHACHHANG
                SET
                    HoTen = ?,
                    SoDienThoai = ?,
                    Email = ?,
                    GioiTinh = ?,
                    NgaySinh = ?,
                    DiaChi = ?
                WHERE MaKhachHang = ?
            """, (
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                ma
            ))

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

        ma = self.txtMaKhachHang.get().strip()

        if ma == "":

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

            cursor.execute("""
                DELETE FROM KHACHHANG
                WHERE MaKhachHang = ?
            """, (ma,))

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

        # Xóa toàn bộ ô nhập
        self.lam_trong_o_nhap()

        # Xóa từ khóa tìm kiếm
        self.txtTimKiem.delete(0, "end")

        # Bỏ chọn dòng trên bảng
        for item in self.tree.selection():
            self.tree.selection_remove(item)

        # Hiển thị lại toàn bộ dữ liệu
        self.hien_thi_khach_hang()


# =========================================================
# CHẠY RIÊNG FILE ĐỂ KIỂM TRA
# =========================================================

if __name__ == "__main__":

    app = ctk.CTk()
    app.geometry("1200x700")
    app.configure(fg_color="#F3EBDD")
    app.title("QUẢN LÝ KHÁCH HÀNG")

    giao_dien = QuanLyKhachHang(
        app,
        lambda: messagebox.showinfo(
            "Thông báo",
            "Đây là chế độ chạy thử riêng."
        )
    )

    giao_dien.pack(fill="both", expand=True)

    app.mainloop()
