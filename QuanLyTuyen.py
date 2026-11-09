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
# CLASS QUẢN LÝ TUYẾN DU LỊCH
# =========================================================

class QuanLyTuyen(ctk.CTkFrame):

    def __init__(self, master, quay_lai):
        super().__init__(master, fg_color="#F3EBDD")

        self.quay_lai = quay_lai

        self.create_interface()


    # =====================================================
    # HÀM CHUYỂN CHỨC NĂNG
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

        # ================= THANH ĐIỀU HƯỚNG =================

        nav_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        nav_frame.pack(
            fill="x",
            padx=15,
            pady=(10, 0)
        )

        btn_quay_lai = ctk.CTkButton(
            nav_frame,
            text="QUAY LẠI TRANG CHỦ",
            command=self.quay_lai,
            width=180,
            height=35,
            font=("Times New Roman", 13, "bold"),
            fg_color="#57595A",
            hover_color="#3C3F40"
        )

        btn_quay_lai.pack(side="left", padx=3)

        cac_chuc_nang = [
            ("QUẢN LÝ ĐIỂM ĐẾN", "QUẢN LÝ ĐIỂM ĐẾN"),
            ("QUẢN LÝ KHÁCH HÀNG", "QUẢN LÝ KHÁCH HÀNG"),
            ("QUẢN LÝ ĐẶT TOUR", "QUẢN LÝ ĐẶT TOUR"),
            ("QUẢN LÝ TUYẾN DU LỊCH", "QUẢN LÝ TUYẾN DU LỊCH"),
            ("QUẢN LÝ TÀI KHOẢN", "QUẢN LÝ TÀI KHOẢN")
        ]

        for ten, ma in cac_chuc_nang:

            dang_mo = ma == "QUẢN LÝ TUYẾN DU LỊCH"

            btn = ctk.CTkButton(
                nav_frame,
                text=ten,
                command=lambda m=ma: self.chuyen_chuc_nang(m),
                width=175,
                height=35,
                font=(
                    "Times New Roman",
                    12,
                    "bold" if dang_mo else "normal"
                ),
                fg_color="#D8C7A5" if dang_mo else "#57595A",
                hover_color="#C7B38D" if dang_mo else "#3C3F40",
                text_color="#333333" if dang_mo else "white"
            )

            btn.pack(side="left", padx=3)


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

        input_frame.pack(
            fill="x",
            padx=15,
            pady=5
        )


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

        self.txtMaTuyen.grid(row=0, column=1, padx=8, pady=6)


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

        self.txtTenTuyen.grid(row=0, column=3, padx=8, pady=6)


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

        self.txtMaDiemDen.grid(row=1, column=1, padx=8, pady=6)


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

        self.txtPhuongTien.grid(row=1, column=3, padx=8, pady=6)


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
            justify="center"
        )

        self.txtNgayKhoiHanh.grid(row=2, column=1, padx=8, pady=6)


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

        self.txtSoNgay.grid(row=2, column=3, padx=8, pady=6)


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

        self.txtGia.grid(row=3, column=1, padx=8, pady=6)


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

        self.txtMoTa.grid(row=3, column=3, padx=8, pady=6)


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


        # TÊN CỘT

        self.tree.heading("MaTuyen", text="Mã tuyến", anchor="center")
        self.tree.heading("TenTuyen", text="Tên tuyến", anchor="center")
        self.tree.heading("MaDiemDen", text="Mã điểm đến", anchor="center")
        self.tree.heading("PhuongTien", text="Phương tiện", anchor="center")
        self.tree.heading("NgayKhoiHanh", text="Ngày khởi hành", anchor="center")
        self.tree.heading("SoNgay", text="Số ngày", anchor="center")
        self.tree.heading("Gia", text="Giá", anchor="center")
        self.tree.heading("MoTa", text="Mô tả", anchor="center")


        # ĐỘ RỘNG CỘT

        self.tree.column("MaTuyen", width=90, anchor="center")
        self.tree.column("TenTuyen", width=180, anchor="center")
        self.tree.column("MaDiemDen", width=100, anchor="center")
        self.tree.column("PhuongTien", width=130, anchor="center")
        self.tree.column("NgayKhoiHanh", width=120, anchor="center")
        self.tree.column("SoNgay", width=70, anchor="center")
        self.tree.column("Gia", width=120, anchor="center")
        self.tree.column("MoTa", width=220, anchor="center")


        self.tree.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
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
            command=self.them_tuyen
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
            command=self.sua_tuyen
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
            command=self.xoa_tuyen
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

        self.tree.bind(
            "<ButtonRelease-1>",
            self.chon_dong
        )


        # HIỂN THỊ DỮ LIỆU

        self.hien_thi_tuyen()


    # =====================================================
    # CHUYỂN GIÁ
    # =====================================================

    def chuyen_gia(self, gia):

        try:
            return float(str(gia).replace(".", "").replace(",", ""))
        except:
            return 0


    # =====================================================
    # HIỂN THỊ GIÁ
    # =====================================================

    def hien_thi_gia(self, gia):

        try:
            return f"{float(gia):,.0f}".replace(",", ".")
        except:
            return "0"


    # =====================================================
    # HIỂN THỊ DỮ LIỆU
    # =====================================================

    def hien_thi_tuyen(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

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

                ngay = ""

                if row[4]:
                    ngay = row[4].strftime("%d/%m/%Y")

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3] if row[3] else "",
                        ngay,
                        row[5] if row[5] else "",
                        self.hien_thi_gia(row[6]),
                        row[7] if row[7] else ""
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

        values = self.tree.item(selected, "values")

        if not values:
            return

        self.txtMaTuyen.delete(0, "end")
        self.txtMaTuyen.insert(0, values[0])

        self.txtTenTuyen.delete(0, "end")
        self.txtTenTuyen.insert(0, values[1])

        self.txtMaDiemDen.delete(0, "end")
        self.txtMaDiemDen.insert(0, values[2])

        self.txtPhuongTien.delete(0, "end")
        self.txtPhuongTien.insert(0, values[3])

        self.txtNgayKhoiHanh.delete(0, "end")
        self.txtNgayKhoiHanh.insert(0, values[4])

        self.txtSoNgay.delete(0, "end")
        self.txtSoNgay.insert(0, values[5])

        self.txtGia.delete(0, "end")
        self.txtGia.insert(0, values[6])

        self.txtMoTa.delete(0, "end")
        self.txtMoTa.insert(0, values[7])


    # =====================================================
    # THÊM TUYẾN
    # =====================================================

    def them_tuyen(self):

        MaTuyen = self.txtMaTuyen.get().strip()
        TenTuyen = self.txtTenTuyen.get().strip()
        MaDiemDen = self.txtMaDiemDen.get().strip()
        PhuongTien = self.txtPhuongTien.get().strip()
        NgayKhoiHanh = self.txtNgayKhoiHanh.get().strip()
        SoNgay = self.txtSoNgay.get().strip()
        Gia = self.txtGia.get().strip()
        MoTa = self.txtMoTa.get().strip()

        if MaTuyen == "" or TenTuyen == "" or MaDiemDen == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập mã tuyến, tên tuyến và mã điểm đến!"
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
                FROM TUYEN_DL
                WHERE MaTuyen = ?
                """,
                (MaTuyen,)
            )

            if cursor.fetchone()[0] > 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Mã tuyến này đã tồn tại!"
                )

                return


            cursor.execute(
                """
                SELECT COUNT(*)
                FROM DIEMDEN
                WHERE MaDiemDen = ?
                """,
                (MaDiemDen,)
            )

            if cursor.fetchone()[0] == 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Mã điểm đến không tồn tại!"
                )

                return


            if SoNgay == "":
                SoNgay = 1
            else:
                SoNgay = int(SoNgay)

                if SoNgay < 1:
                    raise ValueError


            Gia = self.chuyen_gia(Gia)


            if NgayKhoiHanh == "":
                ngay_sql = None
            else:
                ngay_sql = datetime.strptime(
                    NgayKhoiHanh,
                    "%d/%m/%Y"
                ).date()


            cursor.execute(
                """
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
                """,
                (
                    MaTuyen,
                    TenTuyen,
                    MaDiemDen,
                    PhuongTien,
                    ngay_sql,
                    SoNgay,
                    Gia,
                    MoTa
                )
            )

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Thêm tuyến du lịch thành công!"
            )

            self.hien_thi_tuyen()
            self.lam_moi()

        except ValueError:

            messagebox.showwarning(
                "Thông báo",
                "Số ngày phải là số nguyên dương và ngày khởi hành phải có dạng dd/mm/yyyy!"
            )

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                f"Không thể thêm tuyến du lịch:\n\n{e}"
            )

        finally:

            conn.close()


    # =====================================================
    # SỬA TUYẾN
    # =====================================================

    def sua_tuyen(self):

        MaTuyen = self.txtMaTuyen.get().strip()
        TenTuyen = self.txtTenTuyen.get().strip()
        MaDiemDen = self.txtMaDiemDen.get().strip()
        PhuongTien = self.txtPhuongTien.get().strip()
        NgayKhoiHanh = self.txtNgayKhoiHanh.get().strip()
        SoNgay = self.txtSoNgay.get().strip()
        Gia = self.txtGia.get().strip()
        MoTa = self.txtMoTa.get().strip()

        if MaTuyen == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn tuyến cần sửa!"
            )

            return

        if TenTuyen == "" or MaDiemDen == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên tuyến và mã điểm đến!"
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
                FROM DIEMDEN
                WHERE MaDiemDen = ?
                """,
                (MaDiemDen,)
            )

            if cursor.fetchone()[0] == 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Mã điểm đến không tồn tại!"
                )

                return


            if SoNgay == "":
                SoNgay = 1
            else:
                SoNgay = int(SoNgay)

                if SoNgay < 1:
                    raise ValueError


            Gia = self.chuyen_gia(Gia)


            if NgayKhoiHanh == "":
                ngay_sql = None
            else:
                ngay_sql = datetime.strptime(
                    NgayKhoiHanh,
                    "%d/%m/%Y"
                ).date()


            cursor.execute(
                """
                UPDATE TUYEN_DL
                SET
                    TenTuyen = ?,
                    MaDiemDen = ?,
                    PhuongTien = ?,
                    NgayKhoiHanh = ?,
                    SoNgay = ?,
                    Gia = ?,
                    MoTa = ?
                WHERE MaTuyen = ?
                """,
                (
                    TenTuyen,
                    MaDiemDen,
                    PhuongTien,
                    ngay_sql,
                    SoNgay,
                    Gia,
                    MoTa,
                    MaTuyen
                )
            )


            if cursor.rowcount == 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy mã tuyến cần sửa!"
                )

                return


            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Sửa tuyến du lịch thành công!"
            )

            self.hien_thi_tuyen()
            self.lam_moi()

        except ValueError:

            messagebox.showwarning(
                "Thông báo",
                "Số ngày phải là số nguyên dương và ngày khởi hành phải có dạng dd/mm/yyyy!"
            )

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                f"Không thể sửa tuyến du lịch:\n\n{e}"
            )

        finally:

            conn.close()


    # =====================================================
    # XÓA TUYẾN
    # =====================================================

    def xoa_tuyen(self):

        MaTuyen = self.txtMaTuyen.get().strip()

        if MaTuyen == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn tuyến cần xóa!"
            )

            return


        xac_nhan = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc muốn xóa tuyến này không?"
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
                DELETE FROM TUYEN_DL
                WHERE MaTuyen = ?
                """,
                (MaTuyen,)
            )


            if cursor.rowcount == 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy mã tuyến cần xóa!"
                )

                return


            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Xóa tuyến du lịch thành công!"
            )

            self.hien_thi_tuyen()
            self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa tuyến này.\n\n"
                "Có thể tuyến đang được sử dụng ở bảng DATTOUR.\n\n"
                f"Chi tiết:\n{e}"
            )

        finally:

            conn.close()


    # =====================================================
    # LÀM MỚI
    # =====================================================

    def lam_moi(self):

        self.txtMaTuyen.delete(0, "end")
        self.txtTenTuyen.delete(0, "end")
        self.txtMaDiemDen.delete(0, "end")
        self.txtPhuongTien.delete(0, "end")
        self.txtNgayKhoiHanh.delete(0, "end")
        self.txtSoNgay.delete(0, "end")
        self.txtGia.delete(0, "end")
        self.txtMoTa.delete(0, "end")