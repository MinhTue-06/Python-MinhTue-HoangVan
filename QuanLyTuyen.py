import customtkinter as ctk
from tkinter import ttk, messagebox
import pyodbc
from datetime import datetime


# =========================================================
# CẤU HÌNH
# =========================================================

SERVER_NAME = r'.\SQLEXPRESS01'
DB_NAME = 'QuanLyCacTuyenDuLich'


# =========================================================
# CLASS QUẢN LÝ TUYẾN DU LỊCH
# =========================================================

class QuanLyTuyen(ctk.CTkFrame):

    def __init__(self, master, quay_lai):
        super().__init__(master, fg_color="#F3EBDD")

        self.quay_lai = quay_lai

        # Lưu mã tuyến ban đầu trước khi chỉnh sửa
        self.ma_tuyen_cu = None

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
                "Không tìm thấy chức năng chuyển trang! "
                "Vui lòng đăng nhập để thực hiện!"
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

        btn_quay_lai.pack(side="left", padx=3)

        cac_chuc_nang = [
            ("QUẢN LÝ ĐIỂM ĐẾN", 165),
            ("QUẢN LÝ TUYẾN DU LỊCH", 165),
            ("QUẢN LÝ KHÁCH HÀNG", 165),
            ("QUẢN LÝ ĐẶT TOUR", 165),
            ("QUẢN LÝ TÀI KHOẢN", 165)
        ]

        for ten, chieu_rong in cac_chuc_nang:

            dang_mo = ten == "QUẢN LÝ TUYẾN DU LỊCH"

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

        title = ctk.CTkLabel(
            self,
            text="QUẢN LÝ CÁC TUYẾN DU LỊCH",
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

        input_frame.pack(fill="x", padx=15, pady=5)

        # MÃ TUYẾN

        ctk.CTkLabel(
            input_frame,
            text="Mã tuyến:",
            font=("Times New Roman", 16)
        ).grid(row=0, column=0, padx=8, pady=6, sticky="w")

        self.txtMaTuyen = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMaTuyen.grid(
            row=0, column=1, padx=8, pady=6
        )

        # TÊN TUYẾN

        ctk.CTkLabel(
            input_frame,
            text="Tên tuyến:",
            font=("Times New Roman", 16)
        ).grid(row=0, column=2, padx=8, pady=6, sticky="w")

        self.txtTenTuyen = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtTenTuyen.grid(
            row=0, column=3, padx=8, pady=6
        )

        # MÃ ĐIỂM ĐẾN

        ctk.CTkLabel(
            input_frame,
            text="Mã điểm đến:",
            font=("Times New Roman", 16)
        ).grid(row=1, column=0, padx=8, pady=6, sticky="w")

        self.txtMaDiemDen = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMaDiemDen.grid(
            row=1, column=1, padx=8, pady=6
        )

        # PHƯƠNG TIỆN

        ctk.CTkLabel(
            input_frame,
            text="Phương tiện:",
            font=("Times New Roman", 16)
        ).grid(row=1, column=2, padx=8, pady=6, sticky="w")

        self.txtPhuongTien = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtPhuongTien.grid(
            row=1, column=3, padx=8, pady=6
        )

        # NGÀY KHỞI HÀNH

        ctk.CTkLabel(
            input_frame,
            text="Ngày khởi hành:",
            font=("Times New Roman", 16)
        ).grid(row=2, column=0, padx=8, pady=6, sticky="w")

        self.txtNgayKhoiHanh = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center",
            placeholder_text="DD/MM/YYYY"
        )

        self.txtNgayKhoiHanh.grid(
            row=2, column=1, padx=8, pady=6
        )

        # SỐ NGÀY

        ctk.CTkLabel(
            input_frame,
            text="Số ngày:",
            font=("Times New Roman", 16)
        ).grid(row=2, column=2, padx=8, pady=6, sticky="w")

        self.txtSoNgay = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtSoNgay.grid(
            row=2, column=3, padx=8, pady=6
        )

        # GIÁ

        ctk.CTkLabel(
            input_frame,
            text="Giá:",
            font=("Times New Roman", 16)
        ).grid(row=3, column=0, padx=8, pady=6, sticky="w")

        self.txtGia = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtGia.grid(
            row=3, column=1, padx=8, pady=6
        )

        # MÔ TẢ

        ctk.CTkLabel(
            input_frame,
            text="Mô tả:",
            font=("Times New Roman", 16)
        ).grid(row=3, column=2, padx=8, pady=6, sticky="w")

        self.txtMoTa = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMoTa.grid(
            row=3, column=3, padx=8, pady=6
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
            "MaTuyen",
            "TenTuyen",
            "MaDiemDen",
            "PhuongTien",
            "NgayKhoiHanh",
            "SoNgay",
            "Gia",
            "MoTa"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.tree.heading("MaTuyen", text="Mã tuyến")
        self.tree.heading("TenTuyen", text="Tên tuyến")
        self.tree.heading("MaDiemDen", text="Mã điểm đến")
        self.tree.heading("PhuongTien", text="Phương tiện")
        self.tree.heading("NgayKhoiHanh", text="Ngày khởi hành")
        self.tree.heading("SoNgay", text="Số ngày")
        self.tree.heading("Gia", text="Giá")
        self.tree.heading("MoTa", text="Mô tả")

        # ĐỘ RỘNG CỘT

        self.tree.column("MaTuyen", width=100, anchor="center")
        self.tree.column("TenTuyen", width=170, anchor="center")
        self.tree.column("MaDiemDen", width=90, anchor="center")
        self.tree.column("PhuongTien", width=100, anchor="center")
        self.tree.column("NgayKhoiHanh", width=120, anchor="center")
        self.tree.column("SoNgay", width=70, anchor="center")
        self.tree.column("Gia", width=120, anchor="center")
        self.tree.column("MoTa", width=400, anchor="center")

        self.tree.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

        # BẮT SỰ KIỆN CHỌN DÒNG
        self.tree.bind(
            "<<TreeviewSelect>>",
            self.chon_dong
        )

        # =================================================
        # KHUNG NÚT CHỨC NĂNG
        # =================================================

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

        # NÚT THÊM

        self.btnThem = ctk.CTkButton(
            left_frame,
            text="THÊM",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#2196F3",
            hover_color="#1976D2",
            command=self.them
        )

        self.btnThem.pack(side="left", padx=4)

        # NÚT SỬA

        self.btnSua = ctk.CTkButton(
            left_frame,
            text="SỬA",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#FF9800",
            hover_color="#E68900",
            command=self.sua
        )

        self.btnSua.pack(side="left", padx=4)

        # NÚT XÓA

        self.btnXoa = ctk.CTkButton(
            left_frame,
            text="XÓA",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#F44336",
            hover_color="#D32F2F",
            command=self.xoa
        )

        self.btnXoa.pack(side="left", padx=4)

        # NÚT LÀM MỚI

        self.btnLamMoi = ctk.CTkButton(
            left_frame,
            text="LÀM MỚI",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#607D8B",
            hover_color="#455A64",
            command=self.lam_moi
        )

        self.btnLamMoi.pack(side="left", padx=4)

        # ĐƯỜNG KẺ PHÂN CÁCH

        vach_ngan = ctk.CTkFrame(
            button_frame,
            width=2,
            height=40,
            fg_color="#B7A582"
        )

        vach_ngan.pack(side="left", padx=8)

        # NÚT TÌM KIẾM

        self.btnTimKiem = ctk.CTkButton(
            button_frame,
            text="⌕  TÌM KIẾM",
            width=130,
            height=40,
            font=("Times New Roman", 13, "bold"),
            fg_color="#D6E8F8",
            hover_color="#B8D8F5",
            text_color="#1565C0",
            command=self.tim_kiem
        )

        self.btnTimKiem.pack(side="left", padx=4)

        # NHÃN TÌM KIẾM

        lblTimKiem = ctk.CTkLabel(
            button_frame,
            text="Tìm kiếm:",
            font=("Times New Roman", 14)
        )

        lblTimKiem.pack(side="left", padx=4)

        # Ô NHẬP TỪ KHÓA

        self.txtTimKiem = ctk.CTkEntry(
            button_frame,
            width=155,
            height=40,
            font=("Times New Roman", 14),
            placeholder_text="Nhập từ khóa..."
        )

        self.txtTimKiem.pack(side="left", padx=4)

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

        self.btnXoaTimKiem.pack(side="right", padx=4)

        # HIỂN THỊ DỮ LIỆU BAN ĐẦU

        self.hien_thi_tuyen()

    # =====================================================
    # CHUYỂN GIÁ
    # =====================================================

    def chuyen_gia(self, gia):

        gia = str(gia).strip()
        gia = gia.replace(".", "").replace(",", "")

        return float(gia)

    # =====================================================
    # HIỂN THỊ GIÁ
    # =====================================================

    def hien_thi_gia(self, gia):

        if gia is None:
            return "0"

        try:
            return f"{float(gia):,.0f}".replace(",", ".")
        except (ValueError, TypeError):
            return "0"

    # =====================================================
    # HIỂN THỊ DỮ LIỆU
    # =====================================================

    def hien_thi_tuyen(self, tu_khoa=None):

        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            if tu_khoa:

                tu_khoa_tim = f"%{tu_khoa}%"

                cursor.execute("""
                    SELECT
                        MaTuyen,
                        TenTuyen,
                        MaDiemDen,
                        PhuongTien,
                        NgayKhoiHanh,
                        SoNgay,
                        Gia,
                        MoTa
                    FROM TUYEN_DL
                    WHERE
                        CAST(MaTuyen AS NVARCHAR(50)) LIKE ?
                        OR TenTuyen LIKE ?
                        OR CAST(MaDiemDen AS NVARCHAR(50)) LIKE ?
                        OR PhuongTien LIKE ?
                        OR CONVERT(NVARCHAR(10), NgayKhoiHanh, 103) LIKE ?
                        OR CAST(SoNgay AS NVARCHAR(50)) LIKE ?
                        OR CAST(Gia AS NVARCHAR(50)) LIKE ?
                        OR MoTa LIKE ?
                    ORDER BY MaTuyen
                """, (
                    tu_khoa_tim,
                    tu_khoa_tim,
                    tu_khoa_tim,
                    tu_khoa_tim,
                    tu_khoa_tim,
                    tu_khoa_tim,
                    tu_khoa_tim,
                    tu_khoa_tim
                ))

            else:

                cursor.execute("""
                    SELECT
                        MaTuyen,
                        TenTuyen,
                        MaDiemDen,
                        PhuongTien,
                        NgayKhoiHanh,
                        SoNgay,
                        Gia,
                        MoTa
                    FROM TUYEN_DL
                    ORDER BY MaTuyen
                """)

            rows = cursor.fetchall()

            for row in rows:

                ngay = row[4]

                if ngay is not None and hasattr(ngay, "strftime"):
                    ngay = ngay.strftime("%d/%m/%Y")

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1] if row[1] else "",
                        row[2],
                        row[3] if row[3] else "",
                        ngay if ngay else "",
                        row[5] if row[5] is not None else "",
                        self.hien_thi_gia(row[6]),
                        row[7] if row[7] else ""
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
    # TÌM KIẾM TUYẾN DU LỊCH
    # =====================================================

    def tim_kiem(self):

        tu_khoa = self.txtTimKiem.get().strip()

        if tu_khoa == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập nội dung cần tìm kiếm!"
            )

            self.txtTimKiem.focus()
            return

        self.hien_thi_tuyen(tu_khoa)

        # Bỏ chọn dòng trên bảng
        for item in self.tree.selection():
            self.tree.selection_remove(item)

        if not self.tree.get_children():
            messagebox.showinfo(
                "Thông báo",
                "Không tìm thấy tuyến du lịch phù hợp!"
            )

    # =====================================================
    # XÓA TÌM KIẾM
    # =====================================================

    def xoa_tim_kiem(self):

        self.txtTimKiem.delete(0, "end")

        for item in self.tree.selection():
            self.tree.selection_remove(item)

        self.hien_thi_tuyen()

    # =====================================================
    # XÓA TRẮNG CÁC Ô NHẬP
    # =====================================================

    def lam_trong_o_nhap(self):

        self.txtMaTuyen.delete(0, "end")
        self.txtTenTuyen.delete(0, "end")
        self.txtMaDiemDen.delete(0, "end")
        self.txtPhuongTien.delete(0, "end")
        self.txtNgayKhoiHanh.delete(0, "end")
        self.txtSoNgay.delete(0, "end")
        self.txtGia.delete(0, "end")
        self.txtMoTa.delete(0, "end")

    # =====================================================
    # CHỌN DÒNG
    # =====================================================

    def chon_dong(self, event=None):

        # Lấy dòng đang được chọn
        selected_items = self.tree.selection()

        if not selected_items:
            return

        selected = selected_items[0]

        values = self.tree.item(selected, "values")

        if not values:
            return

        # Xóa thông tin cũ trong ô nhập
        self.lam_trong_o_nhap()

        # Lưu mã tuyến cũ để dùng khi cập nhật
        self.ma_tuyen_cu = str(values[0])

        # Đưa dữ liệu lên các ô nhập
        self.txtMaTuyen.insert(0, values[0])
        self.txtTenTuyen.insert(0, values[1])
        self.txtMaDiemDen.insert(0, values[2])
        self.txtPhuongTien.insert(0, values[3])
        self.txtNgayKhoiHanh.insert(0, values[4])
        self.txtSoNgay.insert(0, values[5])
        self.txtGia.insert(0, values[6])
        self.txtMoTa.insert(0, values[7])

        # QUAN TRỌNG:
        # Không khóa mã tuyến nữa
        self.txtMaTuyen.configure(state="normal")

    # =====================================================
    # KIỂM TRA DỮ LIỆU
    # =====================================================

    def kiem_tra_du_lieu(self):

        ma_tuyen = self.txtMaTuyen.get().strip()
        ten_tuyen = self.txtTenTuyen.get().strip()
        ma_diem_den = self.txtMaDiemDen.get().strip()
        phuong_tien = self.txtPhuongTien.get().strip()
        ngay_khoi_hanh = self.txtNgayKhoiHanh.get().strip()
        so_ngay = self.txtSoNgay.get().strip()
        gia = self.txtGia.get().strip()
        mo_ta = self.txtMoTa.get().strip()

        if not ma_tuyen or not ten_tuyen or not ma_diem_den:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập mã tuyến, tên tuyến và mã điểm đến!"
            )

            return None

        # KIỂM TRA SỐ NGÀY

        try:

            if so_ngay == "":
                so_ngay = 1
            else:
                so_ngay = int(so_ngay)

            if so_ngay < 1:
                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Thông báo",
                "Số ngày phải là số nguyên lớn hơn hoặc bằng 1!"
            )

            return None

        # KIỂM TRA GIÁ

        try:

            if gia == "":
                gia = 0
            else:
                gia = self.chuyen_gia(gia)

            if gia < 0:
                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Thông báo",
                "Giá phải là số hợp lệ và không được âm!"
            )

            return None

        # KIỂM TRA NGÀY KHỞI HÀNH

        try:

            if ngay_khoi_hanh == "":
                ngay_sql = None
            else:
                ngay_sql = datetime.strptime(
                    ngay_khoi_hanh,
                    "%d/%m/%Y"
                ).date()

        except ValueError:

            messagebox.showwarning(
                "Thông báo",
                "Ngày khởi hành phải có dạng DD/MM/YYYY!"
            )

            return None

        return (
            ma_tuyen,
            ten_tuyen,
            ma_diem_den,
            phuong_tien,
            ngay_sql,
            so_ngay,
            gia,
            mo_ta
        )

    # =====================================================
    # KIỂM TRA MÃ ĐIỂM ĐẾN
    # =====================================================

    def kiem_tra_diem_den(self, cursor, ma_diem_den):

        cursor.execute("""
            SELECT COUNT(*)
            FROM DIEMDEN
            WHERE MaDiemDen = ?
        """, (ma_diem_den,))

        return cursor.fetchone()[0] > 0

    # =====================================================
    # THÊM TUYẾN DU LỊCH
    # =====================================================

    def them(self):

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
                FROM TUYEN_DL
                WHERE MaTuyen = ?
            """, (data[0],))

            if cursor.fetchone()[0] > 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Mã tuyến này đã tồn tại!"
                )

                return

            if not self.kiem_tra_diem_den(cursor, data[2]):

                messagebox.showwarning(
                    "Thông báo",
                    "Mã điểm đến không tồn tại!"
                )

                return

            cursor.execute("""
                INSERT INTO TUYEN_DL
                (
                    MaTuyen,
                    TenTuyen,
                    MaDiemDen,
                    PhuongTien,
                    NgayKhoiHanh,
                    SoNgay,
                    Gia,
                    MoTa
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, data)

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Thêm tuyến du lịch thành công!"
            )

            self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                f"Không thể thêm tuyến du lịch:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # SỬA TUYẾN DU LỊCH
    # =====================================================

    def sua(self):

        # Phải chọn một dòng trước khi sửa
        if self.ma_tuyen_cu is None:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn tuyến cần sửa trong bảng!"
            )

            return

        # Lấy toàn bộ dữ liệu mới trên các ô nhập
        data = self.kiem_tra_du_lieu()

        if data is None:
            return

        ma_tuyen_moi = data[0]

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            # KIỂM TRA MÃ TUYẾN MỚI CÓ BỊ TRÙNG KHÔNG

            if ma_tuyen_moi != self.ma_tuyen_cu:

                cursor.execute("""
                    SELECT COUNT(*)
                    FROM TUYEN_DL
                    WHERE MaTuyen = ?
                """, (ma_tuyen_moi,))

                if cursor.fetchone()[0] > 0:

                    messagebox.showwarning(
                        "Thông báo",
                        "Mã tuyến mới đã tồn tại!\n"
                        "Vui lòng nhập mã tuyến khác."
                    )

                    return

            # KIỂM TRA MÃ ĐIỂM ĐẾN

            if not self.kiem_tra_diem_den(cursor, data[2]):

                messagebox.showwarning(
                    "Thông báo",
                    "Mã điểm đến không tồn tại!"
                )

                return

            # CẬP NHẬT CẢ MÃ TUYẾN VÀ THÔNG TIN KHÁC

            cursor.execute("""
                UPDATE TUYEN_DL
                SET
                    MaTuyen = ?,
                    TenTuyen = ?,
                    MaDiemDen = ?,
                    PhuongTien = ?,
                    NgayKhoiHanh = ?,
                    SoNgay = ?,
                    Gia = ?,
                    MoTa = ?
                WHERE MaTuyen = ?
            """, (
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                self.ma_tuyen_cu
            ))

            if cursor.rowcount == 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy tuyến cần sửa!"
                )

            else:

                conn.commit()

                messagebox.showinfo(
                    "Thông báo",
                    "Cập nhật tuyến du lịch thành công!"
                )

                self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                "Không thể sửa tuyến du lịch.\n\n"
                "Nếu bà đang đổi mã tuyến, có thể mã tuyến cũ "
                "đang được sử dụng ở bảng DATTOUR hoặc bảng liên quan "
                "thông qua khóa ngoại.\n\n"
                f"Chi tiết lỗi:\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # XÓA TUYẾN DU LỊCH
    # =====================================================

    def xoa(self):

        ma_tuyen = self.txtMaTuyen.get().strip()

        if ma_tuyen == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn tuyến cần xóa!"
            )

            return

        xac_nhan = messagebox.askyesno(
            "Xác nhận",
            f"Bạn có chắc muốn xóa tuyến {ma_tuyen} không?"
        )

        if not xac_nhan:
            return

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM TUYEN_DL
                WHERE MaTuyen = ?
            """, (ma_tuyen,))

            if cursor.rowcount == 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy tuyến cần xóa!"
                )

            else:

                conn.commit()

                messagebox.showinfo(
                    "Thông báo",
                    "Xóa tuyến du lịch thành công!"
                )

                self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa tuyến du lịch.\n\n"
                "Có thể tuyến đang được sử dụng trong bảng DATTOUR "
                "hoặc bảng liên quan khác.\n\n"
                f"Chi tiết:\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # LÀM MỚI
    # =====================================================

    def lam_moi(self):

        # Xóa toàn bộ thông tin nhập
        self.lam_trong_o_nhap()

        # Mở khóa ô mã tuyến
        self.txtMaTuyen.configure(state="normal")

        # Xóa mã tuyến cũ đã lưu
        self.ma_tuyen_cu = None

        # Xóa từ khóa tìm kiếm
        self.txtTimKiem.delete(0, "end")

        # Bỏ chọn dòng trên bảng
        for item in self.tree.selection():
            self.tree.selection_remove(item)

        # Hiển thị lại toàn bộ tuyến du lịch
        self.hien_thi_tuyen()


# =========================================================
# CHẠY RIÊNG FILE ĐỂ KIỂM TRA
# =========================================================

if __name__ == "__main__":

    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("1100x650")
    app.title("QUẢN LÝ TUYẾN DU LỊCH")
    app.configure(fg_color="#F3EBDD")

    giao_dien = QuanLyTuyen(
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